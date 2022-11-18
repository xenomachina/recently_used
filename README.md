# recently_used

Add files to the recently-used list


## Overview:

File dialogs and file managers (like Nautilus) have a "Recently Used" file
list. Files are not automatically added to this list when they are created.
Sometimes it would be nice to have scripts that generate files also add
them to this list. For example, a script that takes screenshots can also
add the resulting file(s) to the recently used list, making it easier to
grab a screenshot and then open it in GIMP or Inkscape.

## Usage:

    recently_used.py [-h] [-A APPNAME] [file [file ...]]


## Positional Arguments:

    file                  File to add to recently used list

## Optional Arguments:

    -h, --help            show this help message and exit
    -A APPNAME, --appname APPNAME
                          Application name (defaults to name of this script)


