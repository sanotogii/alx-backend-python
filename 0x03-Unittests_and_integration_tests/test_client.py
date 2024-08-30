#!/usr/bin/env python3
"""
Test case for GithubOrgClient
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""

    @parameterized.expand([("google",), ("abc",)])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"login": org_name})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the correct value"""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"}
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/google/repos")

    @patch('client.get_json', return_value=[{'name': 'repo1'},
                                            {'name': 'repo2'}])
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repos"""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            link = "https://api.github.com/orgs/google/repos"
            mock_public_repos_url.return_value = link
            client = GithubOrgClient("google")
            repos = client.public_repos()
            self.assertEqual(repos, ['repo1', 'repo2'])
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos")
            mock_public_repos_url.assert_called_once()


if __name__ == "__main__":
    unittest.main()
