import warnings

from qualer_sdk.models.asset_status import AssetStatus

ClientsFromAssetModelAssetStatus = AssetStatus

warnings.warn(
    "ClientsFromAssetModelAssetStatus is deprecated and will be removed in a future release. "
    "Please use AssetStatus instead.",
    DeprecationWarning,
    stacklevel=2,
)
