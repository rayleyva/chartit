"""
ChartIt: A tutorial case study for python web development.

.. moduleauthor:: Craig J Perry, <craigp84@gmail.com>

"""

import os
import bottle
from application.app import app


def in_gae_production():
    """As per `App Engine Docs <https://developers.google.com/appengine/docs/python/runtime#The_Environment>`_
    the ``SERVER_SOFTWARE`` env var contains "Google App Engine" in production.
    :returns: True when running on Google App Engine production
    """
    return True if "Google App Engine" in os.environ.get('SERVER_SOFTWARE', '') else False


if not in_gae_production():
    bottle.debug(True)

bottle.run(app=app, server='gae')
