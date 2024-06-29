#!/usr/bin/env python3
"""Project Unittests and Integration Tests"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class to do test multiple functions"""
    @parameterized.expand([
                           ("google", {"login": "google"}),
                           ("abc", {"login": "abc"})
                           ]
                          )
    @patch("client.get_json",)
    def test_org(self, ORG_URL: str, res: Dict,
                 mocked_fxn: MagicMock) -> None:
        """Tests that the method returns what it is supposed to"""
        mocked_fxn.return_value = MagicMock(return_value=res)
        gh_client = GithubOrgClient(ORG_URL)
        self.assertEqual(gh_client.org(), res)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(ORG_URL)
        )
