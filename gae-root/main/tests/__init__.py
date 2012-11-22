"""
Package level test setup. Run once for the whole package.

.. moduleauthor:: Craig J Perry, <craigp84@gmail.com>

"""


import os
import sys


def add_to_path(path):
    """Add a dir relative to this file location, to the sys.path"""
    this_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(this_dir, path))


def setup():
    """Package level test fixture setup."""
    pass
    #add_to_path('..')
    #add_to_path(os.path.join('..', '..', 'lib'))


def teardown():
    """Package level test fixture teardown."""
    pass

