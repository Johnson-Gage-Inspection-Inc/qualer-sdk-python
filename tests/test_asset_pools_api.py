# coding: utf-8

"""
Qualer.Web.Mvc

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

OpenAPI spec version: v1

Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import qualer_sdk
from qualer_sdk.api.asset_pools_api import AssetPoolsApi  # noqa: E501
from qualer_sdk.rest import ApiException


class TestAssetPoolsApi(unittest.TestCase):
    """AssetPoolsApi unit test stubs"""

    def setUp(self):
        self.api = qualer_sdk.api.asset_pools_api.AssetPoolsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get(self):
        """Test case for get"""
        pass

    def test_get_all(self):
        """Test case for get_all"""
        pass


if __name__ == "__main__":
    unittest.main()
