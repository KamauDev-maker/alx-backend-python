#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from typing import Any, Dict, Tuple
from unittest.mock import patch, Mock

from utils import (
        access_nested_map,
        get_json,
        memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for nested function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict[str, Any],
            path: Tuple[str],
            expected_result: Any
    ) -> None:
        """
        Method for testing the expecte result
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict[str, Any],
            path: Tuple[str],
            expected_exception_message: Exception,
    ) -> None:
        """
        Method for testing the exception message error
        """
        with self.assertRaises(expected_exception_message):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """
    class for testing a mock http
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(
            self,
            test_url: str,
            test_payload: [str, Any],
            mock_get: Mock
    ):
        """
        Method to create a mock obj
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
