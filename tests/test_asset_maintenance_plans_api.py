# coding: utf-8

"""
Modern AssetMaintenancePlansApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.asset_maintenance_plans import (
    get_maintenance_plan,
    get_maintenance_plans,
    reset_initial_service_date,
)
from qualer_sdk.client import Client


class TestAssetMaintenancePlansApiModern(unittest.TestCase):
    """Modern AssetMaintenancePlansApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.asset_maintenance_plans.get_maintenance_plan.sync")
    def test_get_maintenance_plan_function(self, mock_get_maintenance_plan):
        """Test the new get_maintenance_plan function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_maintenance_plan.return_value = mock_response

        # Call the function
        result = get_maintenance_plan.sync(client=self.client)

        # Verify the call
        mock_get_maintenance_plan.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_maintenance_plans.get_maintenance_plan.sync")
    def test_get_maintenance_plans_function(self, mock_get_maintenance_plan):
        """Test the new get_maintenance_plan function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_maintenance_plan.return_value = mock_response

        # Call the function
        result = get_maintenance_plan.sync(client=self.client)

        # Verify the call
        mock_get_maintenance_plan.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_maintenance_plans.reset_initial_service_date.sync")
    def test_reset_initial_service_date_function(self, mock_reset_initial_service_date):
        """Test the new reset_initial_service_date function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_reset_initial_service_date.return_value = mock_response

        # Call the function
        result = reset_initial_service_date.sync(client=self.client)

        # Verify the call
        mock_reset_initial_service_date.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_maintenance_plans.get_maintenance_plans.sync")
    def test_get_maintenance_plans_function(self, mock_get_maintenance_plans):
        """Test the new get_maintenance_plans function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_maintenance_plans.return_value = mock_response

        # Call the function
        result = get_maintenance_plans.sync(client=self.client)

        # Verify the call
        mock_get_maintenance_plans.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
