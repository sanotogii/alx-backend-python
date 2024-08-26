#!/usr/bin/env python3
"""
TestAccessNestedMap
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        with self.assertRaises(KeyError) as context:
            actual = access_nested_map(nested_map, path)
            self.assertEqual(actual, expected)
    @parameterized.expand(
            [
                ({}, ("a",)),
                ({"a", 1}, ("a", "b"))
            ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
