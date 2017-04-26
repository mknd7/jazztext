import sys
import os
import shutil
import formatter

# for option '-h' or '--help' in command
def display_help():
    print "Usage: python mformat.py [OPTIONS] [INPUT_FILE] [OUTPUT_FILE]"
    print "Format and correct simple errors in a txt file."
    print "Note: Chaining of options is not permitted. For eg. -rts"
    print "Example: python mformat.py -r essay.txt essay-edited.txt\n"
    print "  -s, --simple           perform simple format (default), not"
    print "                         default if other options are included"
    print "  -r, --references       remove references, i.e. any '[no.]'"
    print "  -t, --tags             remove HTML tags"
    print "  -d, --duplicates       remove duplicate lines"
    print "  -h, --help             view this help file\n"

# check if command usage is correct
try:
    if len(sys.argv) == 1:
        raise Exception("Error: No file arguments found!\nUse '--help' for more information")
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        display_help()
        exit()
    elif len(sys.argv) == 2:
        raise Exception("Error: Specify both source and destination files!")
except Exception as msg:
    print msg
    exit()

# check for file errors
l = len(sys.argv)
input_file = sys.argv[-2]
output_file = sys.argv[-1]
if input_file == output_file:
    print "Error: Source and destination files are the same!"
    exit()
elif os.path.isfile(input_file) == False:
    print "Error: Source does not exist!"
    exit()

# remove output file if it already exists
if os.path.isfile(output_file):
    os.remove(output_file)

allowed_args = ['-s','--simple','-r','--references',
                '-t','--tags','-d','--duplicates']

# default simple format (no options in command)
# equivalent to adding option '-s' or '--simple'
if len(sys.argv) == 3:
    formatter.mformat_default(input_file, output_file)

# options are specified
else:
    shutil.copyfile(input_file, output_file)
    # complete all options other than simple format
    for arg in sys.argv[1 : -2]:
        if arg not in allowed_args:
            print "Error: Invalid arguments"
            exit()
        if arg != '-s' and arg != '--simple':
            formatter.mformat_other(output_file, arg)
    # perform simple format if specified
    if '-s' in sys.argv or '--simple' in sys.argv:
        os.rename(output_file, 'temp.txt')
        formatter.mformat_default('temp.txt', output_file)
        os.remove('temp.txt')