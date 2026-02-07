import re
from pathlib import Path

import qualer_sdk.models as models

_THIS_DIR = Path(__file__).resolve().parent.parent / "src" / "qualer_sdk" / "models"
_CLASS_RE = re.compile(r"^\s*class\s+([A-Za-z_][A-Za-z0-9_]*)\b", re.M)


def test_all_non_deprecated_models_are_package_attributes():
    """Every class in a non-deprecated model module should be importable from the package.

    This ensures downstream users can do `from qualer_sdk.models import Name`.
    """
    for py in _THIS_DIR.glob("*.py"):
        if py.name == "__init__.py":
            continue
        text = py.read_text(encoding="utf-8", errors="replace")
        # Skip files that are themselves deprecated
        if "DeprecationWarning" in text:
            continue

        for cls in _CLASS_RE.findall(text):
            assert hasattr(
                models, cls
            ), f"models package missing exported name: {cls} (from {py.name})"
            # retrieving it should not raise
            attr = getattr(models, cls)
            assert attr is not None
