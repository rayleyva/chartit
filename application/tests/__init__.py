"""
Package level test setup. Run once for the whole package.

.. moduleauthor:: Craig J Perry, <craigp84@gmail.com>

"""


import sys


def add_to_path(path='..'):
    """Prepend a given path to the python sys.path.

    >>> add_to_path('../a_module')

    :param path: directory location relative to this file
    :type path: str"""
    sys.path.insert(0, path)


def setup():
    """Package level test fixture setup."""
    add_to_path()


def teardown():
    """Package level test fixture teardown."""
    pass
