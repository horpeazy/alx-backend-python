#!/usr/bin/env python3
"""module for testing client module."""
import unittest
from unittest.mock import (
    patch, 
    Mock, 
    MagicMock, 
    PropertyMock
)
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from requests import HTTPError

TEST_PAYLOAD = TEST_PAYLOAD[0]


class TestGithubOrgClient(unittest.TestCase):
    """ test the githuborgclient """
    @parameterized.expand([
        ("google", {"repos_url": "http://github.com/google"}),
        ("abc", {"repos_url": "http://github.com/abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, org_data, mock_func):
        """ test the org method of GithubOrgClient
        Parameters
        ----------
        org_name: str
            name of the organization
        org_data: Dict
            organization data
        mock_func: MagicMock
            mocked function
        """
        mock_func.return_value = MagicMock(
                return_value=org_data)
        org_client = GithubOrgClient(org_name)
        self.assertEqual(org_client.org(), org_data)
        mock_func.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """ test the public_repos_url property """
        with patch("client.GithubOrgClient.org", 
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/users/google/repos"
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos"
            )

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json):
        """ test public repos method """
        repos_payload = [
            {"name": "first-repo"},
            {"name": "second-repo"}    
        ]
        mocked_get_json.return_value = repos_payload
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mocked_repos_url:
            mocked_repos_url.return_value = "https://api.github.com/users/google/repos"
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                ["first-repo","second-repo"]
            )
            mocked_get_json.assert_called_once()
            mocked_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ test has license """
        org_client = GithubOrgClient("google")
        self.assertEqual(org_client.has_license(repo, license_key), expected_result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [(TEST_PAYLOAD[0], TEST_PAYLOAD[1], TEST_PAYLOAD[2], TEST_PAYLOAD[3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """integration test for githuborgclient"""
    @classmethod
    def setUpClass(cls):
        """setup fixture for test"""
        route_payload = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }
        def get_payload(url):
            """gets the payload for a route"""
            if url in route_payload:
                return Mock(**{"json.return_value": route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """teardown fixture for test"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test public repos"""
        org_client = GithubOrgClient("google")
        result = org_client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """test public repos with license"""
        org_client = GithubOrgClient("google")
        result = org_client.public_repos("apache-2.0")
        self.assertEqual(result, self.apache2_repos)
