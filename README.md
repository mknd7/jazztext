# JazzText
A Python-based text formatting command-line tool. The word 'formatting' here can be misleading - JazzText fixes spacing problems and corrects basic sentence structuring errors.

JazzText is a text formatting tool that can be used to eliminate the following:
* unnecessary whitespaces
* extra empty lines
* trailing whitespaces
* consecutive punctuation marks

It also takes care of:
* adding spaces (after punctuation marks)
* removing spaces (before punctuation marks)
* correct usage of common phrases (like e.g.)

Other options include:
* removing references (any [x])
* removing HTML tags
* removing duplicate lines

```
Usage: python jazztext.py [OPTIONS] [INPUT_FILE] [OUTPUT_FILE]
Format and correct simple errors in a txt file.
Example: python jazztext.py -s -r essay.txt essay-edited.txt

  -s, --simple           perform simple format (default)
  -r, --references       remove references, i.e. any '[x]'
  -d, --duplicates       remove duplicate lines (not sentences)
  -n, --newlines         remove all newlines
  -t, --tags             remove HTML tags
  -h, --help             view this help file

Note: Chaining of options is not permitted; eg. -tdr
Simple format will always be performed last, and
must be specified if other options are included.
````

### TODO:

- ~~Give it a proper name!~~
- Overhaul the whole thing
- Add comprehensive tests
- Add more documentation and examples
  - Explain what a simple format is
- Remove unnecessarily extra options
- Properly parse command and options
  - Make this a CLI app using [Click](https://click.palletsprojects.com/en/8.1.x/)
- Add spell check (with option of dictionary)
- Remove references option
  - Add a generic replace option
- Make a GUI app over underlying functionality
