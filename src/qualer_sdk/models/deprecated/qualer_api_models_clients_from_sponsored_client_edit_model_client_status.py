import warnings

from qualer_sdk.models.client_status import ClientStatus

ClientsFromSponsoredClientEditModelClientStatus = ClientStatus

warnings.warn(
    "ClientsFromSponsoredClientEditModelClientStatus is deprecated and will be removed in a future release. Please use ClientStatus instead.",
    DeprecationWarning,
    stacklevel=2,
)
