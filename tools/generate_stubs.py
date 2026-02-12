#!/usr/bin/env python
"""Generate __init__.pyi stub file for qualer_sdk.models to help IDE type checking."""

import re
from pathlib import Path


def generate_models_stub():
    """Generate a .pyi stub file for the models package."""
    models_dir = Path(__file__).parent.parent / "src" / "qualer_sdk" / "models"
    
    # Use same regexes as the runtime discovery
    class_re = re.compile(r"^\s*class\s+([A-Za-z_][A-Za-z0-9_]*)\b", re.M)
    alias_re = re.compile(r"^([A-Z][A-Za-z0-9_]*)\s*=\s*[A-Za-z]", re.M)
    
    exports = {}  # name -> module_name
    
    for py_file in sorted(models_dir.glob("*.py")):
        if py_file.name == "__init__.py":
            continue
            
        text = py_file.read_text(encoding="utf-8", errors="replace")
        
        # Skip deprecated files
        if "DeprecationWarning" in text:
            continue
            
        module_name = py_file.stem
        
        # Find all class definitions
        for cls_name in class_re.findall(text):
            exports.setdefault(cls_name, module_name)
            
        # Find all module-level aliases
        for alias_name in alias_re.findall(text):
            exports.setdefault(alias_name, module_name)
    
    # Also include deprecated package exports
    deprecated_init = models_dir / "deprecated" / "__init__.py"
    if deprecated_init.exists():
        text = deprecated_init.read_text(encoding="utf-8", errors="replace")
        # Extract __all__ = [...] list
        all_match = re.search(r"__all__\s*=\s*\[(.*?)\]", text, re.DOTALL)
        if all_match:
            deprecated_names = re.findall(r'"([^"]+)"', all_match.group(1))
            for name in deprecated_names:
                exports.setdefault(name, f"deprecated.{name.lower()}")
    
    # Generate the stub file
    stub_lines = [
        '"""Type stubs for qualer_sdk.models package.',
        "",
        "This file is auto-generated to help IDEs understand the available exports.",
        '"""',
        "",
        "from typing import Any",
        "",
        "# Explicit exports for IDE support",
    ]
    
    # Add imports grouped by module
    modules = {}
    for name, module in sorted(exports.items()):
        if module not in modules:
            modules[module] = []
        modules[module].append(name)
    
    for module, names in sorted(modules.items()):
        stub_lines.append(f"from .{module} import (")
        for name in sorted(names):
            stub_lines.append(f"    {name} as {name},")
        stub_lines.append(")")
        stub_lines.append("")
    
    # Add __all__
    stub_lines.append("__all__ = [")
    for name in sorted(exports.keys()):
        stub_lines.append(f'    "{name}",')
    stub_lines.append("]")
    stub_lines.append("")
    
    # Add __getattr__ for type checkers
    stub_lines.append("def __getattr__(name: str) -> Any: ...")
    stub_lines.append("def __dir__() -> list[str]: ...")
    stub_lines.append("")
    
    # Write the stub file
    stub_file = models_dir / "__init__.pyi"
    stub_file.write_text("\n".join(stub_lines), encoding="utf-8")
    
    print(f"✓ Generated {stub_file}")
    print(f"  {len(exports)} exports")
    print(f"  {len(modules)} modules")


if __name__ == "__main__":
    generate_models_stub()
