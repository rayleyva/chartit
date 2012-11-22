"""
Unit testing of the app.py module.

.. moduleauthor:: Craig J Perry, <craigp84@gmail.com>

"""


from unittest import TestCase
from application import home


class TestHome(TestCase):
    """Testing inputs and behaviours of the home page handler."""

    def test_home_with_valid_params(self):
        """Ensure home handler responds correctly given valid inputs."""
        result = home()
        self.assertTrue(result != None)
