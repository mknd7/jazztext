import re

# defaut format (no options in command)
def mformat_default(input, output):
    with open(input,'r') as ip, open(output,'w') as op:
        newlines = ['\n','\r']
        newline = False
        for line in ip:
            line.expandtabs(4)
            if line[0] not in newlines:
                line = line.strip()
            if line:
                if line[0] in newlines:
                    if not newline:
                        op.write(line)
                        newline = True
                else:
                    s = simple_format(line)
                    s = s.strip()
                    op.write(s + '\n')
                    newline = False

# perform a simple format
def simple_format(line):
    res = ''                                            # formatted string for each line
    punc_marks_all = ['.','!','?',',',':',';','%']

    # loop over every character in line
    i = 0
    while i < len(line):
        # for handling a single space
        if line[i] == ' ':
            if line[i + 1] not in punc_marks_all + [' '] and res[-1] != ' ':
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
                if line[i + 1] not in [')',']','"',"'"] and line[i + 1 : i + 4] != 'NET':
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

# remove all newlines
def remove_newlines(output):
    with open('temp.txt','r') as ip, open(output,'w') as op:
        for line in ip:
            line = line.expandtabs(4)
            line = line.strip()
            op.write(line)

# perform other operations based on command options
def mformat_other(output, arg):
    removal_block = ''
    if arg == '-r' or arg == '--references':
        removal_block = '\[.*?\]'
        remove_blocks(output, removal_block)
    elif arg == '-t' or arg == '--tags':
        removal_block = '<.*?>'
        remove_blocks(output, removal_block)
    elif arg == '-d' or arg == '--duplicates':
        remove_dups(output)
    elif arg == '-n' or arg == '--newlines':
        remove_newlines(output)