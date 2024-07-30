#!/usr/bin/env python3
"""
Integration tests for GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient

# Import fixtures from fixtures.py
from fixtures import TEST_PAYLOAD

@parameterized_class([
    {"TEST_PAYLOAD": TEST_PAYLOAD}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment by patching requests.get to return predefined responses.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define the side_effect function to return the correct fixture based on the URL
        def side_effect(url):
            if 'orgs' in url:
                return MockResponse(cls.org_payload)
            elif 'repos' in url:
                return MockResponse(cls.repos_payload)
            else:
                raise ValueError("Unexpected URL")

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Stop patching after tests are done.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test the public_repos method in an integration test.
        """
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """
        Test the public_repos method with a license filter.
        """
        client = GithubOrgClient("test_org")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
        self.mock_get.assert_called()

class MockResponse:
    """
    A mock response class to simulate requests.get().json() behavior.
    """
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data

if __name__ == '__main__':
    unittest.main()
