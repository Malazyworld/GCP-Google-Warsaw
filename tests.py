"""
Unit Tests Module.

This module contains the unit tests for the various features of the application,
including algorithms and core logic.
"""

import unittest
from bubble_sort import bubble_sort
from binary_search import binary_search
from feature_x import perform_feature_x_logic


class TestAlgorithms(unittest.TestCase):
    """
    Test suite for sorting and searching algorithms.
    """

    def test_bubble_sort(self):
        """Test that bubble_sort correctly sorts various integer lists."""
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([5]), [5])
        self.assertEqual(bubble_sort([4, -1, 0, 9, 2]), [-1, 0, 2, 4, 9])

    def test_binary_search_found(self):
        """Test that binary_search finds the correct index of an existing element."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 3), 2)
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 5), 4)

    def test_binary_search_not_found(self):
        """Test that binary_search returns None for missing elements."""
        arr = [1, 2, 4, 5]
        self.assertIsNone(binary_search(arr, 3))
        self.assertIsNone(binary_search(arr, 0))
        self.assertIsNone(binary_search(arr, 6))
        self.assertIsNone(binary_search([], 1))


class TestFeatureX(unittest.TestCase):
    """
    Test suite for Feature X logic.
    """

    def test_perform_feature_x_logic(self):
        """Test that feature X logic returns the expected formatted string."""
        name = "TestUser"
        result = perform_feature_x_logic(name)
        self.assertIn(name, result)
        self.assertIn("Feature X processed", result)


def run_all_tests():
    """
    Execute all unit tests defined in this module.
    """
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestAlgorithms)
    suite.addTests(loader.loadTestsFromTestCase(TestFeatureX))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()
