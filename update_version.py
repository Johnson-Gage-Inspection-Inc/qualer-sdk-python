#!/usr/bin/env python3
"""
Update version references across the project.
This script updates version strings in template files to match the current Git tag.
"""
import os
import re
from get_version import get_version_from_git_with_commits


def update_template_version():
    """Update the version in template files."""
    current_version = get_version_from_git_with_commits()

    # Clean version (remove dev/dirty suffixes for templates)
    clean_version = re.sub(r"\.(dev\d+.*|post\d+.*)$", "", current_version)

    template_files = ["templates/init_template.py", "src/qualer_sdk/__init__.py"]

    for template_file in template_files:
        if os.path.exists(template_file):
            print(f"Updating {template_file}...")

            with open(template_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Update hardcoded version strings if any exist
            content = re.sub(
                r'__version__ = "[^"]*"', f'__version__ = "{clean_version}"', content
            )

            with open(template_file, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"✅ Updated {template_file} to version {clean_version}")
        else:
            print(f"⚠️  {template_file} not found")


def show_current_version():
    """Show the current version from Git."""
    version = get_version_from_git_with_commits()
    print(f"Current version from Git: {version}")

    try:
        from setuptools_scm import get_version

        scm_version = get_version()
        print(f"setuptools-scm version: {scm_version}")
    except Exception as e:
        print(f"Could not get setuptools-scm version: {e}")


if __name__ == "__main__":
    show_current_version()
    print()
    update_template_version()
