#!/usr/bin/env python3
class Cmd:
    def __init__(self, addr1, addr2, op) -> None:
        self.addr1 = addr1
        self.addr2 = addr2
        self.op = op

    @staticmethod
    def factory(addr1, addr2, op):
        ops = { 'q' : Cmd_quit,
                'p' : Cmd_print,
                'd' : Cmd_delete,
                's' : Cmd_substitute,
                'b' : Cmd_branch,
                't' : Cmd_to,
                'a' : Cmd_append,
                'i' : Cmd_insert,
                'c' : Cmd_change,
        }
        if op in ops:
            return ops[op](addr1, addr2, op)

class Cmd_quit(Cmd):
    def execute(self, vm):
        return None

class Cmd_print(Cmd):
    def execute(self, vm):
        return None

class Cmd_delete(Cmd):
    def execute(self, vm):
        return None

class Cmd_substitute(Cmd):
    def execute(self, vm):
        return None

class Cmd_branch(Cmd):
    def execute(self, vm):
        return None

class Cmd_to(Cmd):
    def execute(self, vm):
        return None

class Cmd_append(Cmd):
    def execute(self, vm):
        return None

class Cmd_insert(Cmd):
    def execute(self, vm):
        return None

class Cmd_change(Cmd):
    def execute(self, vm):
        return None