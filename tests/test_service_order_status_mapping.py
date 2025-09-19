"""Test ServiceOrderStatus integer to string mapping."""

from qualer_sdk.models.qualer_api_models_asset_to_asset_manage_response_model import (
    AssetToAssetManageResponseModel,
)
from qualer_sdk.models.qualer_api_models_asset_to_asset_manage_response_model_service_order_status import (
    AssetToAssetManageResponseModelServiceOrderStatus,
)
from qualer_sdk.models.qualer_api_models_asset_to_client_asset_manager_response_model import (
    AssetToClientAssetManagerResponseModel,
)
from qualer_sdk.models.qualer_api_models_asset_to_client_asset_manager_response_model_service_order_status import (
    AssetToClientAssetManagerResponseModelServiceOrderStatus,
)
from qualer_sdk.models.qualer_api_models_service_orders_from_change_service_order_status_model import (
    ServiceOrdersFromChangeServiceOrderStatusModel,
)
from qualer_sdk.models.qualer_api_models_service_orders_from_change_service_order_status_model_service_order_status import (
    ServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus,
)


class TestServiceOrderStatusMapping:
    """Test that ServiceOrderStatus handles both integer and string values correctly."""

    def test_asset_to_asset_manage_response_model_integer_mapping(self):
        """Test AssetToAssetManageResponseModel handles integer ServiceOrderStatus values."""
        # Test known integer mappings
        test_cases = [
            (9, "WaitingForApproval"),
            (11, "Processing"),
            (12, "QualityControl"),
            (13, "Cancelled"),
            (15, "Completed"),
            (16, "Denied"),
            (17, "Delayed"),
            (18, "Scheduling"),
            (19, "Closed"),
            (20, "WaitingForVendorSignOff"),
        ]

        for integer_value, expected_string in test_cases:
            data = {"ServiceOrderStatus": integer_value}
            model = AssetToAssetManageResponseModel.from_dict(data)

            assert model.service_order_status is not None
            assert model.service_order_status.value == expected_string

    def test_asset_to_asset_manage_response_model_string_mapping(self):
        """Test AssetToAssetManageResponseModel handles string ServiceOrderStatus values."""
        # Test string values work as before
        test_strings = [
            "WaitingForApproval",
            "Processing",
            "QualityControl",
            "Cancelled",
            "Completed",
            "Denied",
            "Delayed",
            "Scheduling",
            "Closed",
            "WaitingForVendorSignOff",
        ]

        for string_value in test_strings:
            data = {"ServiceOrderStatus": string_value}
            model = AssetToAssetManageResponseModel.from_dict(data)

            assert model.service_order_status is not None
            assert model.service_order_status.value == string_value

    def test_asset_to_asset_manage_response_model_unknown_integer(self):
        """Test AssetToAssetManageResponseModel handles unknown integer values gracefully."""
        data = {"ServiceOrderStatus": 999}  # Unknown integer
        model = AssetToAssetManageResponseModel.from_dict(data)

        # Should not crash and should set to None for unknown values
        assert model.service_order_status is None

    def test_asset_to_asset_manage_response_model_invalid_string(self):
        """Test AssetToAssetManageResponseModel handles invalid string values gracefully."""
        data = {"ServiceOrderStatus": "InvalidStatus"}
        model = AssetToAssetManageResponseModel.from_dict(data)

        # Should not crash and should set to None for invalid strings
        assert model.service_order_status is None

    def test_asset_to_asset_manage_response_model_none_values(self):
        """Test AssetToAssetManageResponseModel handles None and missing values."""
        # Test None value
        data = {"ServiceOrderStatus": None}
        model = AssetToAssetManageResponseModel.from_dict(data)
        assert model.service_order_status is None

        # Test missing field
        data = {}
        model = AssetToAssetManageResponseModel.from_dict(data)
        assert model.service_order_status is None

    def test_asset_to_client_asset_manager_response_model_integer_mapping(self):
        """Test AssetToClientAssetManagerResponseModel handles integer ServiceOrderStatus values."""
        # Test known integer mappings
        test_cases = [
            (9, "WaitingForApproval"),
            (11, "Processing"),
            (12, "QualityControl"),
            (13, "Cancelled"),
            (15, "Completed"),
            (16, "Denied"),
            (17, "Delayed"),
            (18, "Scheduling"),
            (19, "Closed"),
            (20, "WaitingForVendorSignOff"),
        ]

        for integer_value, expected_string in test_cases:
            data = {"ServiceOrderStatus": integer_value}
            model = AssetToClientAssetManagerResponseModel.from_dict(data)

            assert model.service_order_status is not None
            assert model.service_order_status.value == expected_string

    def test_asset_to_client_asset_manager_response_model_string_mapping(self):
        """Test AssetToClientAssetManagerResponseModel handles string ServiceOrderStatus values."""
        # Test string values work as before
        test_strings = [
            "WaitingForApproval",
            "Processing",
            "QualityControl",
            "Cancelled",
            "Completed",
            "Denied",
            "Delayed",
            "Scheduling",
            "Closed",
            "WaitingForVendorSignOff",
        ]

        for string_value in test_strings:
            data = {"ServiceOrderStatus": string_value}
            model = AssetToClientAssetManagerResponseModel.from_dict(data)

            assert model.service_order_status is not None
            assert model.service_order_status.value == string_value

    def test_asset_to_client_asset_manager_response_model_unknown_integer(self):
        """Test AssetToClientAssetManagerResponseModel handles unknown integer values gracefully."""
        data = {"ServiceOrderStatus": 999}  # Unknown integer
        model = AssetToClientAssetManagerResponseModel.from_dict(data)

        # Should not crash and should set to None for unknown values
        assert model.service_order_status is None

    def test_asset_to_client_asset_manager_response_model_invalid_string(self):
        """Test AssetToClientAssetManagerResponseModel handles invalid string values gracefully."""
        data = {"ServiceOrderStatus": "InvalidStatus"}
        model = AssetToClientAssetManagerResponseModel.from_dict(data)

        # Should not crash and should set to None for invalid strings
        assert model.service_order_status is None

    def test_service_orders_from_change_service_order_status_model_integer_mapping(self):
        """Test ServiceOrdersFromChangeServiceOrderStatusModel handles integer ServiceOrderStatus values."""
        # Test known integer mappings
        test_cases = [
            (9, "WaitingForApproval"),
            (11, "Processing"),
            (12, "QualityControl"),
            (13, "Cancelled"),
            (15, "Completed"),
            (16, "Denied"),
            (17, "Delayed"),
            (18, "Scheduling"),
            (19, "Closed"),
            (20, "WaitingForVendorSignOff"),
        ]

        for integer_value, expected_string in test_cases:
            data = {"ServiceOrderStatus": integer_value}
            model = ServiceOrdersFromChangeServiceOrderStatusModel.from_dict(data)

            assert model.service_order_status is not None
            assert model.service_order_status.value == expected_string

    def test_service_orders_from_change_service_order_status_model_string_mapping(self):
        """Test ServiceOrdersFromChangeServiceOrderStatusModel handles string ServiceOrderStatus values."""
        # Test string values work as before
        test_strings = [
            "WaitingForApproval",
            "Processing",
            "QualityControl",
            "Cancelled",
            "Completed",
            "Denied",
            "Delayed",
            "Scheduling",
            "Closed",
            "WaitingForVendorSignOff",
        ]

        for string_value in test_strings:
            data = {"ServiceOrderStatus": string_value}
            model = ServiceOrdersFromChangeServiceOrderStatusModel.from_dict(data)

            assert model.service_order_status is not None
            assert model.service_order_status.value == string_value

    def test_service_orders_from_change_service_order_status_model_unknown_integer(self):
        """Test ServiceOrdersFromChangeServiceOrderStatusModel handles unknown integer values gracefully."""
        data = {"ServiceOrderStatus": 999}  # Unknown integer
        model = ServiceOrdersFromChangeServiceOrderStatusModel.from_dict(data)

        # Should not crash and should set to None for unknown values
        assert model.service_order_status is None

    def test_enum_completeness(self):
        """Test that all mapped integers correspond to actual enum values."""
        # Check AssetToAssetManageResponseModelServiceOrderStatus
        mapped_values = [
            "WaitingForApproval",
            "Processing",
            "QualityControl",
            "Cancelled",
            "Completed",
            "Denied",
            "Delayed",
            "Scheduling",
            "Closed",
            "WaitingForVendorSignOff",
        ]

        for value in mapped_values:
            # Should not raise exception
            AssetToAssetManageResponseModelServiceOrderStatus(value)
            AssetToClientAssetManagerResponseModelServiceOrderStatus(value)
            ServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus(value)
