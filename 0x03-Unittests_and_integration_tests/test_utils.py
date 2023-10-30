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

if __name__ == '__main__':
    unittest.main()