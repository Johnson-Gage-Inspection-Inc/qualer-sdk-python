import warnings

from .service_order_document_response import ServiceOrderDocumentResponse

ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse = ServiceOrderDocumentResponse

warnings.warn(
    "ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse is deprecated and will be removed in a future release. Please use ServiceOrderDocumentResponse instead.",
    DeprecationWarning,
    stacklevel=2,
)
