import sys
import os
import shutil
import formatter

# for option '-h' or '--help' in command
def display_help():
    print("Usage: python jazztext.py [OPTIONS] [INPUT_FILE] [OUTPUT_FILE]")
    print("Format and correct simple errors in a txt file.")
    print("Example: python jazztext.py -s -r essay.txt essay-edited.txt\n")
    print("  -s, --simple           perform simple format (default)")
    print("  -r, --references       remove references, i.e. any '[x]'")
    print("  -d, --duplicates       remove duplicate lines (not sentences)")
    print("  -n, --newlines         remove all newlines")
    print("  -t, --tags             remove HTML tags")
    print("  -h, --help             view this help file\n")
    print("Note: Chaining of options is not permitted; eg. -tdr")
    print("Simple format will always be performed last, and")
    print("must be specified if other options are included.")

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
    print(msg)
    exit()

# check for file errors
l = len(sys.argv)
input_file = sys.argv[-2]
output_file = sys.argv[-1]
if input_file == output_file:
    print("Error: Source and destination files are the same!")
    exit()
elif os.path.isfile(input_file) == False:
    print("Error: Source does not exist!")
    exit()

# remove output file if it already exists
if os.path.isfile(output_file):
    os.remove(output_file)

allowed_args = ['-s','--simple','-r','--references',
                '-t','--tags','-d','--duplicates',
                '-n','--newlines']

# default simple format (no options in command)
# equivalent to adding option '-s' or '--simple'
if len(sys.argv) == 3:
    formatter.jazztext_default(input_file, output_file)

# options are specified
else:
    shutil.copyfile(input_file, output_file)
    # complete all options other than simple format
    for arg in sys.argv[1 : -2]:
        if arg not in allowed_args:
            print("Error: Invalid arguments")
            exit()
        if arg != '-s' and arg != '--simple':
            os.rename(output_file, 'temp.txt')
            formatter.jazztext_other(output_file, arg)
            os.remove('temp.txt')
    # perform simple format last if specified
    if '-s' in sys.argv or '--simple' in sys.argv:
        os.rename(output_file, 'temp.txt')
        formatter.jazztext_default('temp.txt', output_file)
        os.remove('temp.txt')