"""
ChartIt: A tutorial case study for python web development.

.. moduleauthor:: Craig J Perry, <craigp84@gmail.com>

"""

import os
import sys
import bottle
from application.app import app


def in_gae_production():
    """As per `App Engine Docs <https://developers.google.com/appengine/docs/python/runtime#The_Environment>`_
    the ``SERVER_SOFTWARE`` env var contains "Google App Engine" in production.
    :returns: True when running on Google App Engine production
    """
    return True if "Google App Engine" in os.environ.get('SERVER_SOFTWARE', '') else False


def running_as_unittest():
    """Verify whether the current execution context is within a unit test run.
    :returns: True when invoked as part of a unit test"""
    return "nosetests" in sys.argv


if not in_gae_production():
    bottle.debug(True)

if not running_as_unittest:
    # Avoid complaints about missing GAE libs in virtualenv
    bottle.run(app=app, server='gae')
