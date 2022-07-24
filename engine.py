#!/usr/bin/env python3
import re

class VM:
    def __init__(self, overwrite, noprint, cmds, input) -> None:
        self.noprint = noprint
        self.overwrite = overwrite
        self.cmds = cmds
        self.input = input
    
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
        print(self.current_line, end="")


    def run(self):
        self.current_line = self.input.readline()
        self.lineno = 1

        # apply commands to current line
        while self.current_line:
            self.next_line = self.input.readline()
            for cmd in self.cmds:
                cmd.execute_cmd(self)

            # output the current line
            if not self.noprint:
                if self.current_line:
                    self.printline()

            self.current_line = self.next_line
            self.lineno += 1

        
        