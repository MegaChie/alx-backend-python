#!/usr/bin/env python3
"""Task 0. Parameterize a unit test"""
from parameterized import parameterized
from typing import Mapping, Sequence, Any
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class to do test multiple functions"""
    @parameterized.expand([
                           ({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ]
                          )
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """Tests that the method returns what it is supposed to"""
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)

    @parameterized.expand([
                           ({}, ("a",)),
                           ({"a": 1}, ("a", "b"))
                           ]
                          )
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """Tests that the method returns what it is supposed to"""
        with self.assertRaises(Exception) as err:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test class to do test multiple functions"""
    @parameterized.expand([
                           ("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})
                           ]
                          )
    @patch("requests.get")
    def test_get_json(self, test_url: str,
                      test_payload: str, moke_requests_get: Any) -> None:
        """Tests that the method returns what it is supposed to"""
        moke_requests_get.return_value.json.return_value = test_payload
        res = get_json(test_url)
        self.assertEqual(res, test_payload)
        moke_requests_get.assert_called_once_with(test_url)
