import warnings

from qualer_sdk.models.reading_entry_math import ReadingEntryMath

ReportDatasetsToMeasurementAllResponseAsLeftReadingEntryMath = ReadingEntryMath

warnings.warn(
    "ReportDatasetsToMeasurementAllResponseAsLeftReadingEntryMath is deprecated and will be removed in a future release. Please use ReadingEntryMath instead.",
    DeprecationWarning,
    stacklevel=2,
)
