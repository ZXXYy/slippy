#!/usr/bin/env python3

import re
import sys
import click
import argparse
from io import StringIO

import utils

def get_addr(command):
    def calculate_addr(expr):
        return expr if expr =='$' else(expr[1:-1] if re.match(r'/(.*)/', expr) else int(expr))
            
    if ',' in command:
        (start, end) = command.split(',')
        start = calculate_addr(start)
        end = calculate_addr(end)
    else:
        start = calculate_addr(command)
        end = start
    return (start, end)


def process_command(command, noprint, lines=None):
    res = list()
    cnt = 0
    while line:= sys.stdin.readline():
        cnt += 1
        # Subset 0: quit command
        if re.search(r'.*q', command):
            addr = command[1:-2] if re.match(r'/(.*)/q', command) else (int(command[:-1]) if len(command)>1 else 0)
            if not noprint:
                res.append(line)
            if (isinstance(addr, int)) and (addr == 0 or cnt == addr):
                break
            elif (isinstance(addr, str)) and re.search(addr, line):
                break
       
        # Subset 0: print command
        if re.search(r'.*p', command):
            addr = command[1:-2] if re.match(r'/(.*)/p', command) else (int(command[:-1]) if len(command)>1 else 0)
            if (isinstance(addr, int)) and (addr == 0 or cnt == addr):
                res.append(line)
            elif (isinstance(addr, str)) and re.search(addr, line):
                res.append(line)
            if not noprint:
                res.append(line)
        
        # Subset 0: delete command
        if re.search(r'.*d', command):
            addr = command[1:-2] if re.match(r'/(.*)/d', command) else (int(command[:-1]) if len(command)>1 else 0)
            if (isinstance(addr, int)) and (addr == 0 or cnt == addr):
                continue
            elif (isinstance(addr, str)) and re.search(addr, line):
                continue
            if not noprint:
                res.append(line)

        # Subset 0: substitute command
        if m:= re.search(r'(.*)s(\S)(.*)\2(.*)\2(g?)', command):
            addr = 0 if m.group(1) == "" else (m.group(1)[1:-1] if re.match(r'/(.*)/', m.group(1)) else int(m.group(1)))
            regex = m.group(3)
            replace = m.group(4)
            modifier = 0 if m.group(5) == 'g' else 1
            if (isinstance(addr, int)) and (addr == 0 or cnt == addr):
                line = re.sub(regex, replace, line, modifier)
            elif (isinstance(addr, str)) and re.search(addr, line):
                line = re.sub(regex, replace, line, modifier)
            if not noprint:
                res.append(line)
    return res

class Slippy:

    def __init__(self):
        return None


# slippy [-i] [-n] [-f <script-file> | <sed-command>] [<files>...]
def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", action="store_true", dest="overwrite")
    parser.add_argument("-n", action="store_true", dest="noprint")

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-f", dest="script_file", metavar='sript-file')
    group.add_argument("sed_command", nargs='?', default=None, metavar='sed-command')

    parser.add_argument("files", nargs='*', default=sys.stdin)

    args = parser.parse_args()
    return parser, args

def preprocess_commands(commands):
    cmds = list()
    commands = commands.strip()
    lines = commands.split('\n')
    for line in lines:
        while len(line) > 0:
            i, cmd = parse_cmd(line)
            if cmd:
                cmds.append(cmd)
            line = line[i:]


    return cmds

def parse_cmd(command):
    i = 0
    
    return i, None


def main():
    parser, args = parse_argument()

    sed_commands = args.sed_command
    if args.script_file:
        try:
            with open(args.script_file, 'r') as f:
                sed_commands = f.read()
        except IOError:
            utils.eprint("No such file or directory!")

    if args.files:
        if not (args.files is sys.stdin):
            inputs = ""
            try:
                for file in args.files:
                    with open(file, 'r') as f:
                        inputs = inputs + f.read()
                oldstdin = sys.stdin
                sys.stdin = StringIO(inputs)
                print(inputs)
            except IOError:
                utils.eprint("No such file or directory!")

    # preprocessing sed commands
    cmds = preprocess_commands(sed_commands)

    slippy = Slippy()


    # res = list()
    # if not sys.stdin.isatty():
    #     if noprint:
    #         res = process_command(noprint, True)
    #     else:
    #         commands = commands.strip()
            
    #         commands = re.split(';|\n', commands)
    #         for i, command in enumerate(commands):
    #             if pos := command.find("#") != -1:
    #                 command = command[:pos]
    #             if i != len(commands)-1:
    #                 process_command(command, False)
    #             else:
    #                 process_command(command, False)
    
    # display(res)
if __name__ == "__main__":
    main()