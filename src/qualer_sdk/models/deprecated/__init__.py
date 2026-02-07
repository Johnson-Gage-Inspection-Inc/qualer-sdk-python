from __future__ import annotations

import importlib
import re
import warnings
from pathlib import Path
from typing import Any

_THIS_DIR = Path(__file__).resolve().parent

# Matches the standard message your warnings show:
# "<OldName> is deprecated ... Please use <NewName> instead."
_MSG_RE = re.compile(
    r"""["'](?P<old>[A-Za-z_][A-Za-z0-9_]*)\s+is\s+deprecated\b.*?
         Please\s+use\s+(?P<new>[A-Za-z_][A-Za-z0-9_]*)\s+instead\.
     """,
    re.IGNORECASE | re.DOTALL | re.VERBOSE,
)

# old_symbol -> (module_stem, replacement_symbol)
_DEPRECATED: dict[str, tuple[str, str]] = {}
_ALL: set[str] = set()


def _discover_deprecated() -> None:
    if _DEPRECATED:
        return

    for py in _THIS_DIR.glob("*.py"):
        if py.name == "__init__.py":
            continue

        text = py.read_text(encoding="utf-8", errors="replace")
        if "DeprecationWarning" not in text:
            continue

        # Many generated files have exactly one message, but we allow multiple.
        for m in _MSG_RE.finditer(text):
            old = m.group("old")
            new = m.group("new")
            _DEPRECATED.setdefault(old, (py.stem, new))
            _ALL.add(old)


def __getattr__(name: str) -> Any:
    _discover_deprecated()

    hit = _DEPRECATED.get(name)
    if hit is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    module_stem, replacement = hit

    # The deprecated module itself will emit the warning when imported.
    # We don't need to emit it here to avoid duplicate warnings.
    m = importlib.import_module(f".{module_stem}", __name__)
    return getattr(m, name)


def __dir__() -> list[str]:
    _discover_deprecated()
    return sorted(set(globals().keys()) | _ALL)


_discover_deprecated()
__all__ = sorted(_ALL)  # pyright: ignore[reportUnsupportedDunderAll]
