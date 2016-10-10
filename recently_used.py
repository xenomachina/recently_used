#!/usr/bin/env python3
# coding=utf-8

"""
Add files to the recently-used list

Add files to the recently used list that appears in file dialogs and file
managers (like Nautilus).
"""

import argparse
import os.path
import sys

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import Gtk

class UserError(Exception):
    def __init__(self, message):
        self.message = message


def create_argparser():
    description, epilog = __doc__.strip().split('\n', 1)
    parser = argparse.ArgumentParser(description=description, epilog=epilog,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('files',
        help="Files to add to recently used list",
        nargs='*')
    return parser


def warn(msg):
    print('WARNING: ' + msg, file=sys.stderr)


def main(args):
    # Add files to list
    recent_mgr = Gtk.RecentManager.get_default()
    for path in args.files:
        file = Gio.File.new_for_path(path)
        if not file.query_exists():
            warn("%r doesn't exist" % path)
        else:
            uri = file.get_uri()
            recent_mgr.add_item(uri)
            print("Adding %r" % uri)

    # RecentManager.add_item is async, so we need to start the main loop for
    # those calls to actually do something. We want to quit as soon as they are
    # complete, so after scheduling them, we schedule an idle task to quit the
    # loop. Note that the order here is important. If the idle task is
    # scheduled first it will execute first!
    GLib.idle_add(Gtk.main_quit)
    Gtk.main()


if __name__ == '__main__':
    error = None
    argparser = create_argparser()
    try:
        main(argparser.parse_args())
    except FileExistsError as exc:
        error = '%s: %r' % (exc.strerror, exc.filename)
    except FileNotFoundError as exc:
        error = '%s: %r' % (exc.strerror, exc.filename)
    except UserError as exc:
        error = exc.message

    if error is not None:
        print('%s: ERROR: %s' % (argparser.prog, error), file=sys.stderr)
        sys.exit(1)
