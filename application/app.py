#!/usr/bin/env python

"""
.. module:: app
    :platform: Google App Engine, GAE Dev Server
    :synopsis: Home of the main application logic

.. moduleauthor:: Craig J Perry <craigp84@gmail.com>

"""

from bottle import Bottle


app = Bottle()


@app.route('/', method='GET')
def setup_complete():
    return "Environment Configured Correctly."
