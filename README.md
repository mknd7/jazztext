# M-Format
A simple text formatting command-line tool. The word 'text' here can be rather misleading;
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
* removing references (any [num])
* removing HTML tags
* removing duplicate lines (upcoming)

```
Usage: python mformat.py [OPTIONS] [INPUT_FILE] [OUTPUT_FILE]
Format and correct simple errors in a txt file.
Note: Chaining of options is not permitted. For eg. -rts
Example: python mformat.py -r essay.txt essay-edited.txt

  -s, --simple           perform simple format (default), not
                         default if other options are included
  -r, --references       remove references, i.e. any '[no.]'
  -t, --tags             remove HTML tags
  -d, --duplicates       remove duplicate lines
  -h, --help             view this help file
````
