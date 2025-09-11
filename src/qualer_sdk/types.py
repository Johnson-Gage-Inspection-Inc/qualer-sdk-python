"""Core types and utilities for the Qualer SDK

We no longer use a custom ``Unset`` sentinel. ``None`` represents both
"missing" and "null" values across the SDK.
"""

from collections.abc import Mapping
from typing import IO, BinaryIO, List, Optional, Tuple, TypeVar, Union

from attrs import define

# Public type aliases to simplify annotations in user code.
# MaybeUnset[T] expresses a value that may be absent (None) or present.
T = TypeVar("T")

# The types that `httpx.Client(files=)` can accept, copied from that library.
FileContent = Union[IO[bytes], bytes, str]
FileTypes = Union[
    # (filename, file (or bytes), content_type)
    Tuple[Optional[str], FileContent, Optional[str]],
    # (filename, file (or bytes), content_type, headers)
    Tuple[Optional[str], FileContent, Optional[str], Mapping[str, str]],
]
RequestFiles = List[Tuple[str, FileTypes]]


@define
class File:
    """Contains information for file uploads"""

    payload: BinaryIO
    file_name: Optional[str] = None
    mime_type: Optional[str] = None

    def to_tuple(self) -> FileTypes:
        """Return a tuple representation that httpx will accept for multipart/form-data"""
        return self.file_name, self.payload, self.mime_type


__all__ = [
    "File",
    "FileTypes",
    "RequestFiles",
]
