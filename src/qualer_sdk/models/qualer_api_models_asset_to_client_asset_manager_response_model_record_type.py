# Backward compatibility: import from the unified RecordType
import warnings

from .record_type import RecordType as _RecordType

__all__ = ["AssetToClientAssetManagerResponseModelRecordType"]


def __getattr__(name: str):
    if name == "AssetToClientAssetManagerResponseModelRecordType":
        warnings.warn(
            "AssetToClientAssetManagerResponseModelRecordType is deprecated. "
            "Use RecordType instead (from qualer_sdk.models import RecordType).",
            DeprecationWarning,
            stacklevel=2,
        )
        return _RecordType
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


# For direct import: from module import AssetToClientAssetManagerResponseModelRecordType
AssetToClientAssetManagerResponseModelRecordType = _RecordType
