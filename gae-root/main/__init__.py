"""
ChartIt: A tutorial case study for python web development.

.. moduleauthor:: Craig J Perry, <craigp84@gmail.com>

"""

import os
import sys


def add_to_path(path):
    """Add a dir relative to this file location, to the sys.path"""
    this_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(this_dir, path))


def in_gae_development():
    """As per `App Engine Docs <https://developers.google.com/appengine/docs/
    python/runtime#The_Environment>`_ the ``SERVER_SOFTWARE`` env var
    contains "Google App Engine" in production and "Development" in dev.
    :returns: True when running on Google App Engine production
    """
    if "Development" in os.environ.get('SERVER_SOFTWARE', ''):
        return True
    return False


def running_as_unittest():
    """Verify whether the current execution context is within a unit test run.
    :returns: True when invoked as part of a unit test"""
    return "nosetests" in sys.argv


add_to_path(os.path.join('..', 'lib'))
import bottle
from main.app import app


if in_gae_development():
    bottle.debug(True)

if not running_as_unittest:
    # Avoid complaints about missing GAE libs in virtualenv
    bottle.run(app=app, server='gae')
