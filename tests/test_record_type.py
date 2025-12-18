"""Tests for the unified RecordType enum."""

import pytest

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
