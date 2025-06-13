#!/usr/bin/env python3
"""
Show version information for the Qualer SDK.
"""
import sys
from pathlib import Path

# Add the src directory to the path so we can import without installing
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    import qualer_sdk
    print(f"📦 Qualer SDK version: {qualer_sdk.__version__}")
except ImportError as e:
    print(f"❌ Could not import qualer_sdk: {e}")

# Also show Git version info
try:
    from get_version import get_version_from_git_with_commits
    git_version = get_version_from_git_with_commits()
    print(f"🔖 Git version: {git_version}")
except ImportError as e:
    print(f"❌ Could not get Git version: {e}")

# Show setuptools-scm version if available
try:
    from setuptools_scm import get_version
    scm_version = get_version()
    print(f"⚙️  setuptools-scm version: {scm_version}")
except Exception as e:
    print(f"❌ setuptools-scm version unavailable: {e}")
