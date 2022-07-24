#!/usr/bin/env python3
import re
class Command:
    def __init__(self, addr1, addr2, op, detail) -> None:
        self.addr1 = addr1
        self.addr2 = addr2
        self.op = op
        self.detail = detail
        self.matched = False

    def __str__(self) -> str:
        return "addr1:{}\naddr2:{}\nop:{}\ndetail:{}".format(self.addr1, self.addr2, self.op, self.detail)

    @staticmethod
    def factory(addr1, addr2, op, detail):
        ops = { 'q' : Command_quit,
                'p' : Command_print,
                'd' : Command_delete,
                's' : Command_substitute,
                'b' : Command_branch,
                't' : Command_to,
                'a' : Command_append,
                'i' : Command_insert,
                'c' : Command_change,
                ':' : Command_label,
        }
        if op in ops:
            return ops[op](addr1, addr2, op, detail)

    def execute_cmd(self, vm):
        if self.addr1 is None:
            self.execute(vm)
            return True
        elif self.addr2 is None:
            if vm.match(self.addr1):
                self.execute(vm)
                return True
        else:
            if self.matched:
                if vm.match(self.addr2):
                    self.matched = False
                self.execute(vm)
                return True
            else:
                if vm.match(self.addr1):
                    self.execute(vm)
                    self.matched = True
                    return True
        return False
                
class Command_quit(Command):
    def execute(self, vm):
        return None

class Command_print(Command):
    def execute(self, vm):
        vm.printline()
        return None

class Command_delete(Command):
    def execute(self, vm):
        vm.current_line = None
        return None

class Command_substitute(Command):
    def execute(self, vm):
        m = re.search(r'(\S)(.*?)\1(.*?)\1(g?)', self.detail)
        regex = m.group(2)
        replace = m.group(3)
        g = 0 if m.group(4) else 1
        
        subline =  re.sub(regex, replace, vm.current_line, g)
        if subline != vm.current_line:
            vm.current_line = subline
            vm.subsuccess = True
        return None

class Command_branch(Command):
    def execute(self, vm):
        if self.detail:
            vm.pc = vm.symtable[self.detail]
        else:
            vm.pc = len(vm.cmds)
        return None

class Command_to(Command):
    def execute(self, vm):
        if vm.subsuccess:
            if self.detail:
                vm.pc = vm.symtable[self.detail]
            else:
                vm.pc = len(vm.cmds)
            vm.subsuccess = False
        return None

class Command_append(Command):
    def execute(self, vm):
        vm.current_line = vm.current_line +self.detail + "\n"
        return None

class Command_insert(Command):
    def execute(self, vm):
        vm.current_line = self.detail + "\n"+vm.current_line
        return None

class Command_change(Command):
    def execute(self, vm):
        vm.current_line = self.detail + "\n"
        return None

class Command_label(Command):
    def execute(self, vm):
        vm.symtable[self.detail] = vm.pc
        return None