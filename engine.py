#!/usr/bin/env python3
import re

from Cmd import Command_label, Command_quit

class VM:
    def __init__(self, overwrite, noprint, cmds, input) -> None:
        self.noprint = noprint
        self.overwrite = overwrite
        self.cmds = cmds
        self.input = input
        self.subsuccess = False
        self.symtable = dict()
        self.pc = 0
    
    def match(self, addr):
        # addr is regex
        if m:= re.match(r'/(.*)/', addr):
            if re.search(m.group(1), str(self.current_line)):
                return True
        # addr is line number
        elif m:= re.match('[0-9]+', addr):
            if int(addr) == self.lineno:
                return True
        # addr is last line
        elif addr == '$':
            if self.next_line == "":
                return True
        return False

    def printline(self):
        if self.current_line:
            print(self.current_line, end="")

    def form_symtable(self):
        self.pc = 0
        for cmd in self.cmds:
            if isinstance(cmd, Command_label):
                cmd.execute_cmd(self)
            self.pc += 1

    def run(self):
        self.form_symtable()
        self.current_line = self.input.readline()
        self.lineno = 1
        self.pc = 0
        quited = False

        # apply commands to current line
        while self.current_line:
            self.next_line = self.input.readline()
            while self.pc < len(self.cmds):
                # print(self.pc)
                cmd = self.cmds[self.pc]
                executed = cmd.execute_cmd(self)
                if executed and isinstance(cmd, Command_quit):
                    quited = True
                    break
                self.pc += 1

            # output the current line
            if not self.noprint:
                self.printline()

            if quited:
                break

            self.current_line = self.next_line
            self.lineno += 1
            self.pc = 0

        
        