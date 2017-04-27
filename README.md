# M-Format
A simple text formatting command-line tool. The word 'text' here can be misleading;
M-Format fixes spacing problems and corrects basic sentence structuring errors.

M-Format is a Python-based text formatting tool which can be used to eliminate the following:
* unnecessary whitespaces
* extra empty lines
* trailing whitespaces
* multiple consecutive chars

It also takes care of:
* capitalization
* adding spaces (after punctuation marks)
* removing spaces (before punctuation marks)

Other options include:
* removing references (any [x])
* removing HTML tags
* removing duplicate lines

```
Usage: python mformat.py [OPTIONS] [INPUT_FILE] [OUTPUT_FILE]
Format and correct simple errors in a txt file.
Example: python mformat.py -s -r essay.txt essay-edited.txt

  -s, --simple           perform simple format (default)
  -r, --references       remove references, i.e. any '[x]'
  -d, --duplicates       remove duplicate lines (not sentences)
  -t, --tags             remove HTML tags
  -h, --help             view this help file

Note: Chaining of options is not permitted; eg. -tdr
Simple format will always be performed last, and
must be specified if other options are included.
````
