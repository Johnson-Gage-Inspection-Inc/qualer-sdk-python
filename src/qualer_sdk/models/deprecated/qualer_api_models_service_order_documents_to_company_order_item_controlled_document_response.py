import warnings

from .service_order_document_response import ServiceOrderDocumentResponse

ServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse = ServiceOrderDocumentResponse

warnings.warn(
    "ServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse is deprecated and will be removed in a future release. Please use ServiceOrderDocumentResponse instead.",
    DeprecationWarning,
    stacklevel=2,
)
