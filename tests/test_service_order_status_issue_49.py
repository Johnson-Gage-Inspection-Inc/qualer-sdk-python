"""Test for specific issue #49: ServiceOrderStatus=15 should not cause ValueError."""

from qualer_sdk.models.qualer_api_models_asset_to_asset_manage_response_model import (
    AssetToAssetManageResponseModel,
)


class TestIssue49ServiceOrderStatus:
    """Test that specific issue #49 is resolved - ServiceOrderStatus=15 should work."""

    def test_service_order_status_15_completed(self):
        """Test that ServiceOrderStatus=15 (Completed) works without ValueError."""
        # This is the exact scenario from issue #49
        # API returns service_order_status=15 which should map to "Completed"
        mock_api_response_item = {
            "ServiceOrderStatus": 15,
            "AssetId": 12345,
            "AssetName": "Thermocouple Wire Set",
            # Add other minimal required fields if needed
        }

        # This should not raise ValueError anymore
        model = AssetToAssetManageResponseModel.from_dict(mock_api_response_item)

        # Verify the mapping worked correctly
        assert model.service_order_status is not None
        assert model.service_order_status.value == "Completed"
        assert str(model.service_order_status) == "Completed"

    def test_all_observed_integer_mappings_from_issue(self):
        """Test all integer mappings observed in the issue report."""
        # From the issue description, these mappings were observed:
        from qualer_sdk.models.service_order_status import _INT_TO_STR

        for integer_value, expected_string in _INT_TO_STR.items():
            mock_api_response = {
                "ServiceOrderStatus": integer_value,
                "AssetId": 12345,
                "AssetName": "Test Asset",
            }

            # Should not raise ValueError
            model = AssetToAssetManageResponseModel.from_dict(mock_api_response)

            # Should correctly map to the expected string
            assert model.service_order_status is not None
            assert model.service_order_status.value == expected_string

    def test_simulate_get_asset_manager_list_with_service_order_status_15(self):
        """Simulate the get_asset_manager_list.sync scenario from the issue."""
        # Simulate what the API would return for get_asset_manager_list
        mock_api_response_list = [
            {
                "ServiceOrderStatus": 15,  # The problematic value from the issue
                "AssetId": 1001,
                "AssetName": "Thermocouple Wire Set",
                "AssetDescription": "Test thermocouple wire set",
            },
            {
                "ServiceOrderStatus": 11,  # Another observed value
                "AssetId": 1002,
                "AssetName": "Another Asset",
                "AssetDescription": "Another test asset",
            },
        ]

        # This simulates what happens in get_asset_manager_list._parse_response
        parsed_models = []
        for response_item_data in mock_api_response_list:
            # This is the line that was failing in the original issue
            model = AssetToAssetManageResponseModel.from_dict(response_item_data)
            parsed_models.append(model)

        # Verify both models were created successfully
        assert len(parsed_models) == 2

        # Verify the first model (the one that was failing)
        assert parsed_models[0].service_order_status is not None
        assert parsed_models[0].service_order_status.value == "Completed"

        # Verify the second model
        assert parsed_models[1].service_order_status is not None
        assert parsed_models[1].service_order_status.value == "Processing"

    def test_backward_compatibility_with_string_values(self):
        """Ensure we didn't break backward compatibility with string values."""
        # Test that string values still work as before
        mock_api_response = {
            "ServiceOrderStatus": "Completed",  # String value as before
            "AssetId": 12345,
            "AssetName": "Test Asset",
        }

        model = AssetToAssetManageResponseModel.from_dict(mock_api_response)

        assert model.service_order_status is not None
        assert model.service_order_status.value == "Completed"

    def test_unknown_integer_values_handled_gracefully(self):
        """Test that unknown integer values don't crash the application."""
        # Test with an integer that's not in our mapping
        mock_api_response = {
            "ServiceOrderStatus": 999,  # Unknown integer
            "AssetId": 12345,
            "AssetName": "Test Asset",
        }

        # Should not crash
        model = AssetToAssetManageResponseModel.from_dict(mock_api_response)

        # Should set to None for unknown values instead of crashing
        assert model.service_order_status is None
