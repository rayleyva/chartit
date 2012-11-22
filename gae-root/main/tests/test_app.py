"""
Unit testing of the app.py module.

.. moduleauthor:: Craig J Perry, <craigp84@gmail.com>

"""


import unittest
from main.app import home


class TestHome(unittest.TestCase):
    """Testing inputs and behaviours of the home page handler."""

    def test_home_with_valid_params(self):
        """Ensure home handler responds with a complete html output given
        valid inputs."""
        result = home()
        self.assertTrue("</html>" in result)



