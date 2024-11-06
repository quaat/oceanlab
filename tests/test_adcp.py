import unittest

from util.adcp import depth

class TestDepthFunction(unittest.TestCase):

    def test_typical_case(self):
        # Test typical input values
        blinding = 2.0
        cell_size = 0.5
        expected = [2.25, 2.75, 3.25, 3.75, 4.25, 4.75]
        self.assertEqual(depth(blinding, cell_size), expected)

    def test_zero_blinding(self):
        # Test with zero blinding
        blinding = 0.0
        cell_size = 1.0
        expected = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
        self.assertEqual(depth(blinding, cell_size), expected)

    def test_large_cell_size(self):
        # Test with large cell size
        blinding = 1.0
        cell_size = 10.0
        expected = [6.0, 16.0, 26.0, 36.0, 46.0, 56.0]
        self.assertEqual(depth(blinding, cell_size), expected)

    def test_non_positive_cell_size(self):
        # Test with non-positive cell size (should raise an error)
        with self.assertRaises(ValueError):
            depth(1.0, 0)
        with self.assertRaises(ValueError):
            depth(1.0, -1.0)

    def test_negative_blinding(self):
        # Test with negative blinding (should raise an error)
        with self.assertRaises(ValueError):
            depth(-2.0, 1.0)