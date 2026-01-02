import warnings

from qualer_sdk.models.asset_status import AssetStatus

AssetToAssetResponseModelAssetStatus = AssetStatus

warnings.warn(
    "AssetToAssetResponseModelAssetStatus is deprecated and will be removed in a future release. Please use AssetStatus instead.",
    DeprecationWarning,
    stacklevel=2,
)
