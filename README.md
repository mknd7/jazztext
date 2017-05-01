# MkndFormat
A simple Python-based text formatting command-line tool. The word 'text' here can be misleading;
MkndFormat fixes spacing problems and corrects basic sentence structuring errors.

MkndFormat is a text formatting tool which can be used to eliminate the following:
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
Usage: python mformat.py [OPTIONS] [INPUT_FILE] [OUTPUT_FILE]
Format and correct simple errors in a txt file.
Example: python mformat.py -s -r essay.txt essay-edited.txt

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
