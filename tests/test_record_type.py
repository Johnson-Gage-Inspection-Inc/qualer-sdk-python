"""Tests for the unified RecordType enum."""

from qualer_sdk.models.qualer_api_models_asset_to_asset_manage_response_model import (
    AssetToAssetManageResponseModel,
)
from qualer_sdk.models.qualer_api_models_asset_to_client_asset_manager_response_model import (
    AssetToClientAssetManagerResponseModel,
)
from qualer_sdk.models.record_type import RecordType


class TestRecordType:
    """Test suite for RecordType enum."""

    def test_enum_values(self):
        """Test that all enum values are correctly defined."""
        assert RecordType.WAITING_FOR_AGREEMENT.value == "WaitingForAgreement"
        assert RecordType.EQUIPMENT.value == "Equipment"
        assert RecordType.SYSTEM.value == "System"
        assert RecordType.AGREEMENT.value == "Agreement"

    def test_str_representation(self):
        """Test string representation of enum values."""
        assert str(RecordType.EQUIPMENT) == "Equipment"
        assert str(RecordType.SYSTEM) == "System"

    def test_from_api_value_with_integers(self):
        """Test parsing integer codes from API responses."""
        assert RecordType.from_api_value(0) == RecordType.WAITING_FOR_AGREEMENT
        assert RecordType.from_api_value(1) == RecordType.EQUIPMENT
        assert RecordType.from_api_value(2) == RecordType.SYSTEM
        assert RecordType.from_api_value(3) == RecordType.AGREEMENT

    def test_from_api_value_with_strings(self):
        """Test parsing string values from API responses."""
        assert RecordType.from_api_value("Equipment") == RecordType.EQUIPMENT
        assert RecordType.from_api_value("System") == RecordType.SYSTEM
        assert RecordType.from_api_value("Agreement") == RecordType.AGREEMENT
        assert RecordType.from_api_value("WaitingForAgreement") == RecordType.WAITING_FOR_AGREEMENT

    def test_from_api_value_case_insensitive(self):
        """Test case-insensitive parsing of string values."""
        assert RecordType.from_api_value("equipment") == RecordType.EQUIPMENT
        assert RecordType.from_api_value("SYSTEM") == RecordType.SYSTEM
        assert RecordType.from_api_value("agreement") == RecordType.AGREEMENT
        assert RecordType.from_api_value("waitingforagreement") == RecordType.WAITING_FOR_AGREEMENT

    def test_from_api_value_with_whitespace(self):
        """Test parsing with whitespace."""
        assert RecordType.from_api_value(" Equipment ") == RecordType.EQUIPMENT
        assert RecordType.from_api_value(" system ") == RecordType.SYSTEM

    def test_from_api_value_with_none(self):
        """Test that None returns None."""
        assert RecordType.from_api_value(None) is None

    def test_from_api_value_with_invalid_int(self):
        """Test that invalid integer codes return None."""
        assert RecordType.from_api_value(999) is None
        assert RecordType.from_api_value(-1) is None

    def test_from_api_value_with_invalid_string(self):
        """Test that invalid string values return None."""
        assert RecordType.from_api_value("InvalidValue") is None
        assert RecordType.from_api_value("Unknown") is None
        assert RecordType.from_api_value("") is None


class TestBackwardCompatibility:
    """Test backward compatibility with deprecated enum names."""

    def test_deprecated_asset_manager_enum_import(self):
        """Test that the deprecated AssetToClientAssetManagerResponseModelRecordType can still be imported."""
        # Direct import doesn't trigger the deprecation warning, but it still works
        from qualer_sdk.models.qualer_api_models_asset_to_client_asset_manager_response_model_record_type import (
            AssetToClientAssetManagerResponseModelRecordType,
        )
        
        # Should be the same as RecordType
        assert AssetToClientAssetManagerResponseModelRecordType is RecordType

    def test_deprecated_asset_manage_enum_import(self):
        """Test that the deprecated AssetToAssetManageResponseModelRecordType can still be imported."""
        # Direct import doesn't trigger the deprecation warning, but it still works
        from qualer_sdk.models.qualer_api_models_asset_to_asset_manage_response_model_record_type import (
            AssetToAssetManageResponseModelRecordType,
        )
        
        # Should be the same as RecordType
        assert AssetToAssetManageResponseModelRecordType is RecordType

    def test_unified_record_type_import(self):
        """Test that RecordType can be imported from the main models module."""
        from qualer_sdk.models import RecordType as ImportedRecordType
        
        assert ImportedRecordType is RecordType
        assert ImportedRecordType.EQUIPMENT.value == "Equipment"


class TestRecordTypeIntegration:
    """Test RecordType integration with model deserialization."""

    def test_asset_to_asset_manage_response_model_integer_mapping(self):
        """Test AssetToAssetManageResponseModel handles integer RecordType values."""
        # Test known integer mappings (0-3)
        test_cases = [
            (0, "WaitingForAgreement"),
            (1, "Equipment"),
            (2, "System"),
            (3, "Agreement"),
        ]

        for integer_value, expected_string in test_cases:
            data = {"AssetId": 1, "RecordType": integer_value}
            model = AssetToAssetManageResponseModel.from_dict(data)

            assert model.record_type is not None
            assert model.record_type.value == expected_string

    def test_asset_to_asset_manage_response_model_string_mapping(self):
        """Test AssetToAssetManageResponseModel handles string RecordType values."""
        # Test string values work correctly
        test_strings = [
            "WaitingForAgreement",
            "Equipment",
            "System",
            "Agreement",
        ]

        for string_value in test_strings:
            data = {"AssetId": 1, "RecordType": string_value}
            model = AssetToAssetManageResponseModel.from_dict(data)

            assert model.record_type is not None
            assert model.record_type.value == string_value

    def test_asset_to_asset_manage_response_model_zero_value(self):
        """Test AssetToAssetManageResponseModel correctly handles RecordType value 0 (WAITING_FOR_AGREEMENT).
        
        This is a critical test to ensure that value 0 is not treated as falsy
        and is correctly mapped to WAITING_FOR_AGREEMENT.
        """
        data = {"AssetId": 1, "RecordType": 0}
        model = AssetToAssetManageResponseModel.from_dict(data)

        # RecordType 0 should be correctly parsed, not treated as falsy
        assert model.record_type is not None
        assert model.record_type == RecordType.WAITING_FOR_AGREEMENT
        assert model.record_type.value == "WaitingForAgreement"

    def test_asset_to_asset_manage_response_model_unknown_integer(self):
        """Test AssetToAssetManageResponseModel handles unknown integer RecordType values gracefully."""
        data = {"AssetId": 1, "RecordType": 999}  # Unknown integer
        model = AssetToAssetManageResponseModel.from_dict(data)

        # Should not crash and should set to None for unknown values
        assert model.record_type is None

    def test_asset_to_asset_manage_response_model_invalid_string(self):
        """Test AssetToAssetManageResponseModel handles invalid string RecordType values gracefully."""
        data = {"AssetId": 1, "RecordType": "InvalidType"}
        model = AssetToAssetManageResponseModel.from_dict(data)

        # Should not crash and should set to None for invalid strings
        assert model.record_type is None

    def test_asset_to_asset_manage_response_model_none_values(self):
        """Test AssetToAssetManageResponseModel handles None and missing RecordType values."""
        # Test None value
        data = {"AssetId": 1, "RecordType": None}
        model = AssetToAssetManageResponseModel.from_dict(data)
        assert model.record_type is None

        # Test missing field
        data = {"AssetId": 1}
        model = AssetToAssetManageResponseModel.from_dict(data)
        assert model.record_type is None

    def test_asset_to_client_asset_manager_response_model_integer_mapping(self):
        """Test AssetToClientAssetManagerResponseModel handles integer RecordType values."""
        # Test known integer mappings (0-3)
        test_cases = [
            (0, "WaitingForAgreement"),
            (1, "Equipment"),
            (2, "System"),
            (3, "Agreement"),
        ]

        for integer_value, expected_string in test_cases:
            data = {"AssetId": 1, "RecordType": integer_value}
            model = AssetToClientAssetManagerResponseModel.from_dict(data)

            assert model.record_type is not None
            assert model.record_type.value == expected_string

    def test_asset_to_client_asset_manager_response_model_string_mapping(self):
        """Test AssetToClientAssetManagerResponseModel handles string RecordType values."""
        # Test string values work correctly
        test_strings = [
            "WaitingForAgreement",
            "Equipment",
            "System",
            "Agreement",
        ]

        for string_value in test_strings:
            data = {"AssetId": 1, "RecordType": string_value}
            model = AssetToClientAssetManagerResponseModel.from_dict(data)

            assert model.record_type is not None
            assert model.record_type.value == string_value

    def test_asset_to_client_asset_manager_response_model_zero_value(self):
        """Test AssetToClientAssetManagerResponseModel correctly handles RecordType value 0 (WAITING_FOR_AGREEMENT).
        
        This is a critical test to ensure that value 0 is not treated as falsy
        and is correctly mapped to WAITING_FOR_AGREEMENT.
        """
        data = {"AssetId": 1, "RecordType": 0}
        model = AssetToClientAssetManagerResponseModel.from_dict(data)

        # RecordType 0 should be correctly parsed, not treated as falsy
        assert model.record_type is not None
        assert model.record_type == RecordType.WAITING_FOR_AGREEMENT
        assert model.record_type.value == "WaitingForAgreement"

    def test_asset_to_client_asset_manager_response_model_unknown_integer(self):
        """Test AssetToClientAssetManagerResponseModel handles unknown integer RecordType values gracefully."""
        data = {"AssetId": 1, "RecordType": 999}  # Unknown integer
        model = AssetToClientAssetManagerResponseModel.from_dict(data)

        # Should not crash and should set to None for unknown values
        assert model.record_type is None

    def test_asset_to_client_asset_manager_response_model_invalid_string(self):
        """Test AssetToClientAssetManagerResponseModel handles invalid string RecordType values gracefully."""
        data = {"AssetId": 1, "RecordType": "InvalidType"}
        model = AssetToClientAssetManagerResponseModel.from_dict(data)

        # Should not crash and should set to None for invalid strings
        assert model.record_type is None

    def test_asset_to_client_asset_manager_response_model_none_values(self):
        """Test AssetToClientAssetManagerResponseModel handles None and missing RecordType values."""
        # Test None value
        data = {"AssetId": 1, "RecordType": None}
        model = AssetToClientAssetManagerResponseModel.from_dict(data)
        assert model.record_type is None

        # Test missing field
        data = {"AssetId": 1}
        model = AssetToClientAssetManagerResponseModel.from_dict(data)
        assert model.record_type is None

