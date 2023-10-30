#!/usr/bin/env python3
"""
Test client module
"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test for Github org client's
    """
    @parameterized.expand([
        ('google', 'google'),
        ('abc', 'abc'),
    ])
    @patch('client.get_json')
    def test_org(
            self,
            org_name: str,
            expected: str,
            mock_get_json: Mock
    ):
        """
        Method that retrieves the desired results
        """
        client = GithubOrgClient(org_name)
        mock_get_json.return_value = expected
        result = client.org
        mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{org_name}'
        )
        self.assertEqual(result, expected)
    def test_public_repos_url(self) -> None:
        """
        Method to set up the mock org
        """
        new_payload = [
                {"name": "repo1", "html_url": "https://github.com/org/repo1"},
                {"name": "repo2", "html_url": "https://github.com/org/repo2"},
        ]
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = new_payload
            client = GithubOrgClient('org')
            result = client._public_repos_url()
        expected = [
                "https://github.com/org/repo1",
                "https://github.com/org/repo2"
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
