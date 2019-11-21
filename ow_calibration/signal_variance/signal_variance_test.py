"""
-----LSignal Variance Test File-----

Written by: Edward Small
When: 21/11/2019

Contains unit tests to check the functionality of the `signal_variance` function

To run this test specifically, look at the documentation at:
https://gitlab.noc.soton.ac.uk/edsmall/bodc-dmqc-python
"""

import unittest
from .signal_variance import signal_variance


class SignalVarianceTestCase(unittest.TestCase):
    """
    Test cases for signal_variance function
    """

    def test_returns_float(self):
        """
        Check that we return a float if given some data
        :return: Nothing
        """
        print("Testing that signal_variance returns a float")

        var = signal_variance([1, 2, 3, 4, 5])
        self.assertTrue(isinstance(var, float), "signal variance is not a float")

    def test_throws_exception(self):
        """
        Check that we thrown an exception if no valid salinities are given
        :return: Nothing
        """
        print("Testing that signal_variance throws an exception for no valid salinities")

        with self.assertRaises(Exception) as no_valid_sal:
            signal_variance([0, 0, float('nan'), float('nan')])

        self.assertTrue('Received no valid salinity values when calculating signal variance'
                        in str(no_valid_sal.exception))

    def test_nans_are_ignored(self):
        """
        Check that we ignore 0's and nan values
        :return: Nothing
        """
        print("Testing that")

        expected = signal_variance([1, 2, 3, 4, 5])
        zeroes = signal_variance([1, 0, 2, 0, 3, 0, 4, 0, 5, 0])
        nans = signal_variance([1, 2, 3, 4, 5, float('nan'), float('nan')])

        self.assertEqual(expected, zeroes, "signal variance is not ignoring 0's")
        self.assertEqual(expected, nans, "sign_variance is not ignoring NaN's")


if __name__ == '__main__':
    unittest.main()
