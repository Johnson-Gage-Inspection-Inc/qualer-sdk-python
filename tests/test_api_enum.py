"""Test the ApiEnum mixin functionality."""

import pytest

from qualer_sdk.models.api_enum import ApiEnum
from qualer_sdk.models.service_order_status import ServiceOrderStatus
from qualer_sdk.models.service_result_status import ServiceResultStatus
from qualer_sdk.models.work_status import WorkStatus


class TestApiEnumMixin:
    """Test the ApiEnum mixin provides consistent behavior across enums."""

    def test_service_order_status_api_enum_behavior(self):
        """Test ServiceOrderStatus inherits ApiEnum behavior."""
        # Integer parsing
        assert ServiceOrderStatus.from_api_value(15) == ServiceOrderStatus.COMPLETED
        assert ServiceOrderStatus.from_api_value(11) == ServiceOrderStatus.PROCESSING
        assert ServiceOrderStatus.from_api_value(999) is None
        
        # String parsing
        assert ServiceOrderStatus.from_api_value("Completed") == ServiceOrderStatus.COMPLETED
        assert ServiceOrderStatus.from_api_value("completed") == ServiceOrderStatus.COMPLETED  # case insensitive
        assert ServiceOrderStatus.from_api_value("COMPLETED") == ServiceOrderStatus.COMPLETED  # case insensitive
        assert ServiceOrderStatus.from_api_value("InvalidStatus") is None
        
        # None handling
        assert ServiceOrderStatus.from_api_value(None) is None
        
        # Direct construction via _missing_
        assert ServiceOrderStatus(15) == ServiceOrderStatus.COMPLETED
        assert ServiceOrderStatus("Completed") == ServiceOrderStatus.COMPLETED
        assert ServiceOrderStatus("completed") == ServiceOrderStatus.COMPLETED

    def test_service_result_status_api_enum_behavior(self):
        """Test ServiceResultStatus inherits ApiEnum behavior."""
        # Integer parsing
        assert ServiceResultStatus.from_api_value(21) == ServiceResultStatus.PASS
        assert ServiceResultStatus.from_api_value(1) == ServiceResultStatus.FAIL
        assert ServiceResultStatus.from_api_value(999) is None
        
        # String parsing
        assert ServiceResultStatus.from_api_value("Pass") == ServiceResultStatus.PASS
        assert ServiceResultStatus.from_api_value("pass") == ServiceResultStatus.PASS  # case insensitive
        assert ServiceResultStatus.from_api_value("PASS") == ServiceResultStatus.PASS  # case insensitive
        assert ServiceResultStatus.from_api_value("InvalidStatus") is None
        
        # None handling
        assert ServiceResultStatus.from_api_value(None) is None
        
        # Direct construction via _missing_
        assert ServiceResultStatus(21) == ServiceResultStatus.PASS
        assert ServiceResultStatus("Pass") == ServiceResultStatus.PASS
        assert ServiceResultStatus("pass") == ServiceResultStatus.PASS
        
        # Test to_code method still works
        assert ServiceResultStatus.PASS.to_code() == 21
        assert ServiceResultStatus.FAIL.to_code() == 1

    def test_work_status_api_enum_behavior(self):
        """Test WorkStatus inherits ApiEnum behavior."""
        # Integer parsing
        assert WorkStatus.from_api_value(2) == WorkStatus.COMPLETED
        assert WorkStatus.from_api_value(1) == WorkStatus.INPROGRESS
        assert WorkStatus.from_api_value(999) is None
        
        # String parsing
        assert WorkStatus.from_api_value("Completed") == WorkStatus.COMPLETED
        assert WorkStatus.from_api_value("completed") == WorkStatus.COMPLETED  # case insensitive
        assert WorkStatus.from_api_value("COMPLETED") == WorkStatus.COMPLETED  # case insensitive
        assert WorkStatus.from_api_value("InvalidStatus") is None
        
        # None handling
        assert WorkStatus.from_api_value(None) is None
        
        # Direct construction via _missing_
        assert WorkStatus(2) == WorkStatus.COMPLETED
        assert WorkStatus("Completed") == WorkStatus.COMPLETED
        assert WorkStatus("completed") == WorkStatus.COMPLETED
        
        # Test to_code method works
        assert WorkStatus.COMPLETED.to_code() == 2
        assert WorkStatus.INPROGRESS.to_code() == 1

    def test_enum_string_representation(self):
        """Test that string representation works correctly."""
        assert str(ServiceOrderStatus.COMPLETED) == "Completed"
        assert str(ServiceResultStatus.PASS) == "Pass"
        assert str(WorkStatus.COMPLETED) == "Completed"

    def test_numeric_string_parsing(self):
        """Test parsing of numeric strings."""
        # Should work for ServiceResultStatus which has from_code method
        assert ServiceResultStatus.from_api_value("21") == ServiceResultStatus.PASS
        assert ServiceResultStatus.from_api_value("1") == ServiceResultStatus.FAIL
        
        # For WorkStatus and ServiceOrderStatus, numeric strings are not supported 
        # since they don't have from_code methods
        assert WorkStatus.from_api_value("2") is None  
        assert ServiceOrderStatus.from_api_value("15") is None

    def test_unknown_values_handled_gracefully(self):
        """Test that all enums handle unknown values gracefully."""
        for enum_class in [ServiceOrderStatus, ServiceResultStatus, WorkStatus]:
            assert enum_class.from_api_value(99999) is None
            assert enum_class.from_api_value("UnknownValue") is None
            assert enum_class.from_api_value("") is None
            assert enum_class.from_api_value(None) is None