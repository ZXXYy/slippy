#!/usr/bin/env python3

import re
import sys
import argparse
from io import StringIO

from Cmd import *
import utils

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
    commands = commands.replace(' ', '')
    lines = commands.split('\n')
    for line in lines:
        while len(line) > 0:
            i, cmd = parse_cmd(line)
            if cmd:
                cmds.append(cmd)
            line = line[i:]

    for cmd in cmds:
        print(str(cmd))
    return cmds

def parse_cmd(command):
    addr1, addr2, addr_len = get_addr(command)
    op = command[addr_len]
    command = command[addr_len:]
    detail, detail_len = get_detail(command)
    command = command[detail_len:]
    comment_len = get_comment(command)

    # deal with ;
    if comment_len < len(command):
        if command[comment_len]==';':
            comment_len += 1
        else:
            utils.eprint("no semicolon between commands")
            exit()

    cmd = Command.factory(addr1, addr2, op, detail)
    
    return addr_len + detail_len+comment_len, cmd


def get_addr(command):
    m = re.search('([0-9]+|/.*?/|\$)?((,)([0-9]+|/.*?/|\$))?', command)
    # print(m.group(0))
    if m.group(0) == None:
        return None, None, 0
    else:
        if m.group(2) == None:
            return m.group(1), None, len(m.group(0))
        else:
            return m.group(1), m.group(4), len(m.group(0))

def get_detail(command):
    invalid = False
    op = command[0]
    if op in 'dpq':
        return None, 1
    elif op in 'aci':
        return command[1:], len(command)
    elif op in 'bt':
        if (pos := command.find(';')) != -1:
            return command[1:pos], pos
        else:
            return command[1:], len(command)
    elif op in 's':
        m = re.search(r'(\S)(.*?)\1(.*?)\1(g?)', command)
        if m:
            return command[m.start():m.end()], m.end()
        invalid = True
    elif op in '#':
        return None, len(command)
    else:
        invalid = True

    if invalid:
        utils.eprint("command line: invalid command")
        exit()

    return None

def get_comment(command):
    if command[0] == '#':
        if (pos:= command.find(';')) != -1:
            return pos
        else:
            return len(command)
    return 0

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