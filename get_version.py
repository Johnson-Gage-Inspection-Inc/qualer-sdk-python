#!/usr/bin/env python3
"""
Get version from Git tags or fallback to a default version.
This ensures all version references stay in sync with GitHub releases.
"""
import subprocess
import re
from pathlib import Path


def get_version_from_git():
    """Get the current version from Git tags."""
    try:
        # Get the most recent tag
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent,
            check=True,
        )
        tag = result.stdout.strip()

        # Remove 'v' prefix if present (e.g., 'v3.0b1' -> '3.0b1')
        if tag.startswith("v"):
            tag = tag[1:]

        return tag

    except (subprocess.CalledProcessError, FileNotFoundError):
        # Fallback if git is not available or no tags exist
        return "0.0.0"


def get_version_from_git_with_commits():
    """Get version with commit info if not on a tagged commit."""
    try:
        # Get the current commit description
        result = subprocess.run(
            ["git", "describe", "--tags", "--dirty"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent,
            check=True,
        )
        description = result.stdout.strip()

        # Remove 'v' prefix if present
        if description.startswith("v"):
            description = description[1:]

        # If it's exactly a tag, return just the version
        if re.match(r"^[\d\w\.\-]+$", description):
            return description

        # If it has commits after tag, convert to development version
        # e.g., "3.0b1-5-g1234567" -> "3.0b1.dev5"
        match = re.match(r"^([\d\w\.\-]+)-(\d+)-g[a-f0-9]+(-dirty)?$", description)
        if match:
            version, commits, dirty = match.groups()
            dev_version = f"{version}.dev{commits}"
            if dirty:
                dev_version += "+dirty"
            return dev_version

        return description

    except (subprocess.CalledProcessError, FileNotFoundError):
        return get_version_from_git()


if __name__ == "__main__":
    print(get_version_from_git_with_commits())
