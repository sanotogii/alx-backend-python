#!/usr/bin/env python3
"""
TestAccessNestedMap
"""
from unittest.mock import patch, Mock
from utils import get_json, memoize
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
        actual = access_nested_map(nested_map, path)
        self.assertEqual(actual, expected)

    @parameterized.expand([({}, ("a",)), ({"a", 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload

        result = get_json(test_url)

        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """test memoize"""

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        mock_a_method.return_value = 42

        result_1 = TestClass().a_property()
        result_2 = TestClass().a_property()

        self.assertEqual(result_1, 42)
        self.assertEqual(result_2, 42)
        mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
