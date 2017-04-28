import re
import os

# defaut format (no options in command)
def mformat_default(input, output):
    with open(input,'r') as ip, open(output,'w') as op:
        newlines = ['\n','\r']
        prev_line = None
        for line in ip:
            if line[0] in newlines and line != prev_line:
                op.write(line)
                prev_line = line
            else:
                s = simple_format(line)
                if s[0] not in newlines:
                    if s[-3] == ' ':
                        s = s[:-3] + s[-2:]
                        op.write(s)
                    else:
                        op.write(s)
                    prev_line = s

# perform a simple format
def simple_format(line):
    res = ''                                            # formatted string for each line
    punc_marks_all = ['.','!','?',',',':',';','%']
    newlines = ['\n','\r']

    # loop over every character in line
    i = 0
    while i < len(line):
        if line[i] in newlines:
            res += line[i]
        # for handling a single space
        elif line[i] == ' ':
            if i + 1 < len(line):
                if line[i + 1] not in punc_marks_all + [' ']:
                    if len(res) >= 1:
                        if res[-1] != ' ':
                            res += ' '
        elif line[i] in punc_marks_all:
            # for ellipsis (...)
            if line[i : i + 3] == '...':
                if res[-3:] != '...':
                    res += '...'
                i += 3
                continue
            # to eliminate duplicate punctuation marks
            if len(res) >= 2:
                if res[-2] == line[i] and res[-1] == ' ':
                    i += 1
                    continue
            res += line[i]
            # ensuring no comma spaces after commas in-between digits (e.g. 7,000)
            if line[i] == ',':
                if i + 1 < len(line):
                    if line[i + 1].isdigit():
                        i += 1
                        continue
            # ensuring no spaces after fullstops in version numbers (e.g. v1.0)
            elif line[i] == '.':
                if i + 1 < len(line):
                    if line[i - 1].isdigit() and line[i + 1].isdigit():
                        i += 1
                        continue
                    elif line[i - 1].isdigit() and line[i + 1] == 'x':
                        i += 1
                        continue
            # single space after punctuation mark
            if i + 1 < len(line):
                if line[i + 1] not in newlines + [')',']','"',"'"] and line[i + 1 : i + 4] != 'NET':
                    if res[-1] != ' ':
                        res += ' '
        # for any other character or phrases
        else:
            if line[i : i + 3] == "i'm":
                res += line[i].upper()
            elif line[i : i + 2] == 'i ':
                res += line[i].upper()
            elif line[i : i + 2] == 'i.':
                res += line[i].upper()
            elif line[i : i + 2] == 'i,':
                res += line[i].upper()
            elif line[i : i + 4] == 'i.e.' or line[i : i + 4] == 'i.e ':
                res += 'i.e. '
                i += 4
                continue
            elif line[i : i + 3] == 'ie.':
                res += 'i.e.'
                i += 3
                continue
            elif line[i : i + 4] == 'e.g.' or line[i : i + 4] == 'e.g ':
                res += 'e.g. '
                i += 4
                continue
            elif line[i : i + 3] == 'eg.':
                res += 'e.g. '
                i += 3
                continue
            elif line[i : i + 4] == 'etc.':
                res += 'etc.'
                i += 4
                continue
            elif line[i : i + 3] == 'etc':
                res += 'etc.'
                i += 3
                continue
            elif line[i : i + 2] == 'v.':
                res += 'v.'
                i += 2
                continue
            # for handling parens
            elif line[i : i + 2] == '()':
                res += '()'
                i += 2
                continue
            elif line[i] == '(':
                if res[-1] == ' ':
                    res += '('
                else:
                    res += ' ('
            else:
                res += line[i]
        i += 1
    return res

# remove blocks of data, like [num]s and <tag>s
def remove_blocks(output, removal_block):
    with open('temp.txt','r') as ip, open(output,'w') as op:
        for line in ip:
            match = re.search(removal_block, line)
            if match:
                l = re.sub(removal_block, '', line)
                if l[0] not in ['\n','\r']:
                    op.write(l)
            else:
                op.write(line)

# remove duplicate lines (not sentences)
def remove_dups(output):
    lines = []
    with open('temp.txt','r') as ip, open(output,'w') as op:
        for line in ip:
            if line not in lines:
                op.write(line)
                lines.append(line)
            elif line[0] in ['\r','\n']:
                op.write(line)

# perform other operations based on command options
def mformat_other(output, arg):
    os.rename(output, 'temp.txt')
    removal_block = ''
    if arg == '-r' or arg == '--references':
        removal_block = '\[.*?\]'
        remove_blocks(output, removal_block)
    if arg == '-t' or arg == '--tags':
        removal_block = '<.*?>'
        remove_blocks(output, removal_block)
    if arg == '-d' or arg == '--duplicates':
        remove_dups(output)
    os.remove('temp.txt')