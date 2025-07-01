# Versioning Guide

This project uses **dynamic versioning** that automatically syncs with GitHub tags, eliminating the need to manually update version numbers in multiple files.

## How It Works

The version is automatically determined from Git tags using `setuptools-scm`:

- **Latest tag**: Determines the base version
- **Commits ahead**: Automatically adds `.dev{count}` for unreleased changes  
- **Git hash**: Includes commit identifier for precise tracking
- **Dirty state**: Adds `+dirty` if there are uncommitted changes

## Version Examples

| Git State | Package Version | Description |
|-----------|----------------|-------------|
| `v3.0b1` (exact tag) | `3.0b1` | Official beta release |
| `v3.0b1` + 5 commits | `3.0b2.dev5+gad8b4ab` | Development version |
| `v3.0b1` + uncommitted changes | `3.0b2.dev5+gad8b4ab.dirty` | Local modifications |

## Creating a New Release

1. **Commit all changes** and push to the main branch
2. **Create and push a new tag**:
   ```bash
   git tag v3.1.0
   git push origin v3.1.0
   ```
3. **Build and publish**:
   ```bash
   python -m build
   python -m twine upload dist/*
   ```

The version will automatically be `3.1.0` in the published package.

## Version Checking

Use the `show_version.py` script to check current version information:

```bash
python show_version.py
```

Output example:
```
📦 Qualer SDK version: 3.0b2.dev5+gad8b4ab.d20250613
🔖 Git version: 3.0b1-5-gad8b4ab-dirty  
⚙️  setuptools-scm version: 3.0b2.dev5+gad8b4ab.d20250613
```

## Implementation Details

### Files Using Dynamic Versioning

- `pyproject.toml` - Uses `dynamic = ["version"]` and `setuptools-scm`
- `setup.py` - Uses `use_scm_version` parameter
- `src/qualer_sdk/__init__.py` - Imports version from package metadata
- `templates/init_template.py` - Template for regenerated code

### Version Detection Code

The `__init__.py` files use this pattern:

```python
try:
    from importlib.metadata import version
    __version__ = version("qualer-sdk")
except ImportError:
    # Fallback for Python < 3.8 or if package not installed
    try:
        import pkg_resources
        __version__ = pkg_resources.get_distribution("qualer-sdk").version
    except Exception:
        __version__ = "unknown"
```

### Build Configuration

`pyproject.toml` configuration:
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel", "setuptools-scm"]

[project]
dynamic = ["version"]

[tool.setuptools_scm]
version_scheme = "python-simplified-semver"
local_scheme = "node-and-date"
tag_regex = "^v(?P<version>.*)$"
```

## Benefits

✅ **Single source of truth** - Versions come from Git tags only  
✅ **No manual updates** - No more hunting down hardcoded version strings  
✅ **Development versions** - Automatic `.dev` versions between releases  
✅ **Git integration** - Version includes commit hash and dirty state  
✅ **CI/CD friendly** - Works seamlessly with automated builds

## Migration from Manual Versioning

All hardcoded version references have been replaced with dynamic detection:

- ~~`pyproject.toml`: `version = "2.2.1"`~~ → `dynamic = ["version"]`
- ~~`setup.py`: `version="2.2.1"`~~ → `use_scm_version=...`  
- ~~`__init__.py`: `__version__ = "2.2.1"`~~ → Dynamic import from metadata
- ~~`regenerate_sdk.py`: Hardcoded insertion~~ → Uses `get_version_from_git_with_commits()`

## Versioning Tests

### Dirty-Tag Scheme

The `dirty-tag` local scheme ensures that version strings include `+dirty` when the working directory has uncommitted changes. This behavior is verified by the `test_versioning.py` test file.

To run the test:

```bash
pytest tests/test_versioning.py
```

Expected output:

- The test passes if the version string includes `+dirty` when the repository is in a dirty state.
- The test fails if the version string does not include `+dirty` or if there are errors in version resolution.
