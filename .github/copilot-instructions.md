Repository guidelines for Copilot and code review assistants

Context
- This repository no longer uses an OpenAPI or code generation pipeline.
- The file spec.json has been removed and will not be reintroduced.

Authoritative rules
- DO allow direct edits to any files under src/qualer_sdk/**. Treat them as hand-maintained source code, not generated artifacts.
- DO propose concrete fixes and refactors directly in those files when reviewing pull requests.
- DO NOT suggest editing spec.json, running generators, or regenerating the SDK. There is no regeneration step.
- DO NOT block or warn on changes to files that might look generated. They are now maintained manually.

Reviewer/bot hints
- Prefer actionable diffs over high-level “regenerate the SDK” guidance.
- If a change modifies API models or clients, assume it is intentional and in-scope unless tests or types clearly break.
- Use the project’s tests, lint, and type checks as the source of truth, not generator templates.

Examples
- Good: “Update qualer_sdk/types.py to tighten Optional typing and adjust imports.”
- Good: “Fix to_dict/from_dict in models to handle new fields.”
- Avoid: “Edit spec.json and regenerate the client.”
