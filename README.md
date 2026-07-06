# agent-patterns

Reference implementations of common agentic AI orchestration patterns in Python.

## Development

This project is structured as a modern `src/` Python package managed with `uv`.

```bash
uv sync --group dev
uv run ruff check .
uv run pyright
uv run pytest
```

## Patterns

Each orchestration pattern lives in its own package under `src/agent_patterns/`.
See `docs/patterns/README.md` for the pattern index.
