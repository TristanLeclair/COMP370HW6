import argparse
import datetime
import os

def valid_date(s):
    """Validate date format"""
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def dir_path(s):
    if os.path.isdir(s):
        return s
    elif os.path.isfile(s):
        raise NotADirectoryError(s)
    else:
        os.makedirs(s)
        return s
