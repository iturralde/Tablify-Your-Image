Tablify-Your-Image
==================

Introduction
------------

Tablify Your Image is a (mostly useless) python script that converts images into HTML tables.

Usage
-----

```
usage: TablifyYourImage.py [-h] [-v] [-s] [-x WIDTH] [-y HEIGHT] [-o OUTPUT] [-d ID] input

positional arguments:
    input                 the path to the file that you want to tablify

optional arguments:
    -h, --help                  show this help message and exit
    -v, --version               print the version number and exit
    -s, --stdout                print the html to the standard output
    -x WIDTH, --width WIDTH     the width of each td in pixels (default = 1)
    -y HEIGHT, --height HEIGHT  the height of each td in pixels (default = 1)
    -o OUTPUT, --output OUTPUT  the path to the output file. If omitted, the name of
                                the input file is used. It doesn't work when the
                                --stdout option is specified.
    -d ID, --id ID              the id of the table
```

License
-------

Tablify Your Image is free software/open source, and is distributed under the GNU General Public License (GPL) version 3 license.
