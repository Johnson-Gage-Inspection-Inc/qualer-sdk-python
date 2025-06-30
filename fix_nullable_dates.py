#!/usr/bin/env python3
"""
Script to fix nullable date fields in the OpenAPI spec.json file.
This addresses the issue where date fields like NextServiceDate can be null/None
but the spec doesn't properly declare them as nullable.
"""

import json
from typing import Any


def fix_nullable_date_fields(spec_path: str) -> None:
    """
    Fix nullable date fields in the OpenAPI spec.

    For Swagger 2.0, we use the x-nullable extension to indicate that a field can be null.
    """

    # Read the spec file
    with open(spec_path, "r", encoding="utf-8") as f:
        spec = json.load(f)

    # List of date field names that should be nullable
    nullable_date_fields = [
        "NextServiceDate",
        "CertificateNextServiceDate",
        "PrimaryToolNextServiceDate",
        "SecondaryToolNextServiceDate",
        "AsLeftPrimaryToolNextServiceDate",
        "AsFoundPrimaryToolNextServiceDate",
        "AsLeftSecondaryToolNextServiceDate",
        "AsFoundSecondaryToolNextServiceDate",
        "DueDate",
        "CertificateDueDate",
        "ServiceDate",
    ]

    changes_made = 0

    def fix_date_field_recursive(obj: Any, path: str = "") -> None:
        nonlocal changes_made

        if isinstance(obj, dict):
            # Check if this is a properties object containing date fields
            if "properties" in obj and isinstance(obj["properties"], dict):
                for field_name, field_def in obj["properties"].items():
                    if (
                        isinstance(field_def, dict)
                        and field_name in nullable_date_fields
                        and field_def.get("type") == "string"
                        and field_def.get("format") == "date-time"
                    ):

                        # Check if x-nullable is not already set to true
                        if not field_def.get("x-nullable", False):
                            field_def["x-nullable"] = True
                            changes_made += 1
                            print(
                                f"Fixed nullable date field: {path}.properties.{field_name}"
                            )

            # Recursively process nested objects
            for key, value in obj.items():
                fix_date_field_recursive(value, f"{path}.{key}" if path else key)

        elif isinstance(obj, list):
            # Recursively process list items
            for i, item in enumerate(obj):
                fix_date_field_recursive(item, f"{path}[{i}]")

    # Process the entire spec
    fix_date_field_recursive(spec)

    # Write the updated spec back to file
    with open(spec_path, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)

    print(f"\nCompleted! Made {changes_made} changes to nullable date fields.")
    print(f"Updated spec file: {spec_path}")


if __name__ == "__main__":
    spec_file = "spec.json"
    fix_nullable_date_fields(spec_file)
