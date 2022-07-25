#!/usr/bin/env python3

import re
import sys
from sys import exit
import os
import argparse
from io import StringIO

from Cmd import *
from engine import *
import utils

def preprocess_commands(commands):
    cmds = list()
    # commands = commands.replace(' ', '')
    commands = commands.strip()
    lines = commands.split('\n')
    for line in lines:
        while len(line) > 0:
            line = line.strip()
            i, cmd = parse_cmd(line)
            if cmd:
                cmds.append(cmd)
            line = line[i:]

    # for cmd in cmds:
    #     print(str(cmd))
    return cmds
def escape_space(command, i):
    while i < len(command):
        if command[i] == ' ':
            i += 1
        else:
            break
    return i

def parse_cmd(command):
    # FIXME seq 1 5 | python3 -s -S slippy 's/[15]/z\\/z\\/z/'
    # FIXME seq 1 5 | python3 -s -S slippy 's_[15]_z\\_z\\_z_'
    # FIXME seq 1 5 | python3 -s -S slippy 's1[\\15]1zzz1'
    addr1, addr2, addr_len = get_addr(command)
    addr_len = escape_space(command, addr_len)
    op = command[addr_len]
    addr_len = escape_space(command, addr_len+1)
    command = command[addr_len:]
    detail, detail_len = get_detail(command, op, addr1)
    detail_len = escape_space(command, detail_len)
    command = command[detail_len:]

    comment_len = get_comment(command)
    # deal with ;
    if comment_len < len(command):
        if command[comment_len]==';':
            comment_len += 1
        else:
            utils.eprint("slippy: command line: invalid command")
            exit(1)

    cmd = Command.factory(addr1, addr2, op, detail)
    
    return addr_len + detail_len+comment_len, cmd


def get_addr(command):
    m = re.match('([0-9]+|/.*?/|\$)?((\s*,\s*)([0-9]+|/.*?/|\$))?', command)
    if m.group(0) == None:
        return None, None, 0
    else:
        if m.group(2) == None:
            return m.group(1), None, len(m.group(0))
        else:
            return m.group(1), m.group(4), len(m.group(0))

def get_detail(command, op, addr1):
    invalid = False
    # op = command[0]
    if op in 'dpq':
        return None, 0
    elif op in 'aci':
        return command[0:], len(command)
    elif op in 'bt':
        if (pos := command.find(';')) != -1:
            return command[0:pos], pos
        else:
            return command[0:], len(command)
    elif op in 's':
        # get regex & replacement string
        regex, replace, g, i = get_regex_replacement(command)
        try:
            re.compile(regex)
        except re.error:
            invalid = True
        res = list()
        res.append(regex)
        res.append(replace)
        res.append(g)
        return res, i
        # m = re.match(r'(\S)([^\\]*?)\1(.*?[^\\])\1(g?)', command[0:])
        # if m:
        #     return command[m.start():m.end()], m.end()
        # invalid = True

    elif op in '#':
        return None, len(command)
    elif op in ':':
        if addr1 is not None:
            invalid = True
        elif (pos := command.find(';')) != -1:
            return command[0:pos], pos
        else:
            return command[0:], len(command)
    else:
        invalid = True

    if invalid:
        utils.eprint("slippy: command line: invalid command")
        exit(1)

    return None

# FIXME python3 -s -S slippy 's/[15]/z\/z\/z/'
def get_regex_replacement(command):
    delimiter = command[0]
    g = 1
    i = 1
    def get_str(command,  i):
        regex = ""
        while i < len(command) and command[i] != delimiter:
            if command[i] == '\\' and i+1 < len(command) and command[i+1] == delimiter:
                i += 1
                regex = regex + command[i]
                i += 1
            else:
                regex = regex + command[i]
                i += 1
        i += 1
        return regex, i

    regex, i = get_str(command, i)
    replace, i = get_str(command, i)
    if i < len(command) and command[i] == 'g':
        g = 0
        i += 1
    return regex, replace, g, i

def get_comment(command):
    if len(command) == 0:
        return 0
    if command[0] == '#':
        if (pos:= command.find(';')) != -1:
            return pos
        else:
            return len(command)
    return 0

# slippy [-i] [-n] [-f <script-file> | <sed-command>] [<files>...]
def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", action="store_true", dest="overwrite")
    parser.add_argument("-n", action="store_true", dest="noprint")
    

    group = parser.add_argument_group()
    group.add_argument("-f", dest="script_file", metavar='<sript-file>')
    group.add_argument("sed_command", nargs='?', default=None, metavar='<sed-command>')

    # FIXME python3 slippy.py -f commands.slippy two.txt five.txt
    parser.add_argument("files", nargs='*', default=sys.stdin)

    args = parser.parse_args()
    return parser, args

def main():
    parser, args = parse_argument()
    if args.script_file:
        try:
            with open(args.script_file, 'r') as f:
                sed_commands = f.read()
        except IOError:
            utils.eprint("No such file or directory!")
        if args.sed_command:
            if args.files is sys.stdin:
                args.files = [args.sed_command]
            else:
                args.files.insert(0, args.sed_command)
    else:
        sed_commands = args.sed_command

    # preprocessing sed commands
    cmds = preprocess_commands(sed_commands)

    if args.files:
        if not args.overwrite:
            oldstdin = sys.stdin
            if not (args.files is sys.stdin):
                inputs = ""
                try:
                    for file in args.files:
                        with open(file, 'r') as f:
                            inputs = inputs + f.read()
                    sys.stdin = StringIO(inputs)
                    # print(inputs)
                except IOError:
                    utils.eprint("No such file or directory!")
                
            slippy = VM(args.overwrite, args.noprint, cmds, sys.stdin)
            slippy.run()
            sys.stdin = oldstdin
        else:
            oldstdin = sys.stdin
            for file in args.files:
                with open(file, 'r') as f:
                    sys.stdin = StringIO(f.read())
                slippy = VM(args.overwrite, args.noprint, cmds, sys.stdin)
                slippy.run()
                slippy.output.close()
                with open('temp', 'r') as src:
                    contents = src.read()

                with open(args.files[0], 'w') as dst:
                    dst.write(contents)
                os.remove('temp')
   

    # slippy = VM(args.overwrite, args.noprint, cmds, sys.stdin)
    # slippy.run()
    # sys.stdin = oldstdin

if __name__ == "__main__":
    main()