#!/usr/bin/env python3
"""Task 0. Parameterize a unit test"""
import unittest
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test class to do test multiple functions"""
    @parameterized.expand([
                           ({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ]
                          )
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int):
        """Tests that the method returns what it is supposed to"""
        
