#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from typing import Any, Dict, Tuple

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
        ({}, ("a",), "Key not found: 'a' in {}"),
        ({"a": 1}, ("a", "b"), "Key not found: 'b' in {'a': 1}")
    ])

    def test_access_nested_map_exception(
            self,
            nested_map: Dict[str, Any],
            path: Tuple[str],
            expected_exception_message: str
    ) -> None:
        """
        Method for testing the exception message error
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_exception_message)



if __name__ == '__main__':
    unittest.main()
