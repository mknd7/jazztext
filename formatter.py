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
                    # remove extra white space at line end
                    if s[-2] == ' ':
                        op.write(s[:-2] + '\n')
                    else:
                        op.write(s)
                    prev_line = s

# perform a simple format
def simple_format(line):
    res = ''                                            # formatted string for each line
    first_letter = False                                # first letter occurence for every sentence in a line
    punc_marks_capitalize = ['.','!','?']               # marks after which the first letter must be capitalized
    punc_marks_normal = [',',':',';','%']               # other punctuation marks
    newlines = ['\n','\r']                              # newline characters

    # list of all punctuation marks
    punc_marks_all = punc_marks_capitalize + punc_marks_normal

    # loop over every character in line
    i = 0
    while i < len(line): 

        # first letter not occurred yet
        if line[i] != ' ' and not first_letter:
            first_letter = True
            if line[i] in newlines:
                res += line[i]
            if line[i].isalnum():
                res += line[i].upper()
            else:
                if line[i] in ['.','(',')']:
                    if line[i] == '.':
                        if res[-3:] != '...':
                            res += '.'
                    else:
                        res += line[i]
                    # for ellipsis
                    if line[i + 1] == ' ':
                        res += ' '
                elif line[i] in punc_marks_all and line[i + 1] in newlines:
                    res += line[i]
                # to eliminate duplicates
                if len(res) >= 2:
                    if res[-2] == line[i]:
                        first_letter = False

        # first letter has already occured
        elif first_letter:
            # if any char in ['.','!','?'] is encountered
            if line[i] in punc_marks_capitalize:
                if line[i] == '.' and line[i-3 : i] == 'etc':
                    res += '.'
                    i += 1
                    continue
                first_letter = False
            # if any punctuation mark is encountered
            if line[i] in punc_marks_all:
                # to eliminate duplicates
                if len(res) >= 2:
                    if res[-2] == line[i]:
                        i += 1
                        continue
                res += line[i]
                # ignore comma spaces for commas between numbers (eg. 7,000)
                if line[i] == ',':
                    if i + 1 < len(line):
                        if line[i + 1].isdigit() or line[i + 1] == ' ':
                            i += 1
                            continue
                if i + 1 < len(line):
                    if line[i + 1] not in newlines + ['.',')'] and res[-1] != ' ':
                        res += ' '

            # for any other character or phrases
            elif line[i] != ' ':
                if line[i : i + 3] == "i'm":
                    res += line[i].upper()
                elif line[i : i + 2] == 'i ':
                    res += line[i].upper()
                elif line[i : i + 4] == 'i.e.' or line[i : i + 4] == 'i.e ':
                    res += 'i.e. '
                    i += 4
                elif line[i : i + 3] == 'ie.':
                    res += 'i.e. '
                    i += 3
                elif line[i : i + 2] == 'i.':
                    res += line[i].upper()
                elif line[i] == '(':
                    if res[-1] == ' ':
                        res += '('
                    else:
                        res += ' ('
                else:
                    res += line[i]

            # check for single space character
            elif line[i] == ' ':
                if i + 1 < len(line):
                    if line[i + 1] not in (punc_marks_all + [' ']) and res[-1] != ' ':
                        res += ' '
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

# perform other operations based on command options
def mformat_other(output, arg):
    os.rename(output, 'temp.txt')
    removal_block = ''
    if arg == '-r' or arg == '--references':
        removal_block = '\[\d+\]'
        remove_blocks(output, removal_block)
    if arg == '-t' or arg == '--tags':
        removal_block = '<.*?>'
        remove_blocks(output, removal_block)
    os.remove('temp.txt')