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


    def test_public_repos_url(self) -> None:
        """Tests that the method returns what it is supposed to"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                    'repos_url': "https://api.github.com/users/google/repos",
                                     }
            self.assertEqual(
                    GithubOrgClient("google")._public_repos_url,
                    "https://api.github.com/users/google/repos",
                             )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests that the method returns what it is supposed to"""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()