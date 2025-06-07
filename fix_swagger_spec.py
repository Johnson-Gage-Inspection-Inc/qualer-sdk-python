# Script to fix the multiple schema issues in the OpenAPI specification
import json
import sys


def fix_swagger_spec(input_file, output_file):
    """Fix multiple schema issues in Swagger 2.0 spec.

    When converting Swagger 2.0 to OpenAPI 3.0, multiple media types in "consumes"
    and "produces" arrays get transformed into 'content' objects with multiple schemas.
    This causes warnings like "Multiple schemas found in the OAS 'content' section,
    returning only the first one" during SDK generation.

    This function resolves the issue by keeping only the first content type in each
    consumes/produces array, ensuring consistent behavior when the generator transforms
    the spec to OpenAPI 3.0.

    Args:
        input_file: Path to the input Swagger 2.0 specification file
        output_file: Path where the fixed specification will be saved
    """
    with open(input_file, "r", encoding="utf-8") as f:
        spec = json.load(f)

    # When converting Swagger 2.0 to OpenAPI 3.0, the 'consumes' and 'produces' arrays
    # get transformed into 'content' objects with multiple media types.
    # Let's ensure consistent behavior by keeping only the first content type

    # Global consumes/produces
    if "consumes" in spec and len(spec["consumes"]) > 1:
        spec["consumes"] = [spec["consumes"][0]]  # Keep only the first content type

    if "produces" in spec and len(spec["produces"]) > 1:
        spec["produces"] = [spec["produces"][0]]  # Keep only the first content type

    # For each path and operation
    for path_key, path_item in spec.get("paths", {}).items():
        for method, operation in path_item.items():
            if method in ["get", "post", "put", "delete", "patch", "options", "head"]:
                if "consumes" in operation and len(operation["consumes"]) > 1:
                    operation["consumes"] = [operation["consumes"][0]]
                if "produces" in operation and len(operation["produces"]) > 1:
                    operation["produces"] = [operation["produces"][0]]

    # Write the fixed specification
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2)

    print(f"Fixed specification written to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_file>")
        sys.exit(1)

    fix_swagger_spec(sys.argv[1], sys.argv[2])
