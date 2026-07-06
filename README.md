# agent-patterns

Reference implementations of common agentic AI orchestration patterns in Python.

## Overview

Modern LLM applications often need multi-step orchestration, not just single prompts.
This repository provides small, readable pattern implementations that make those orchestration strategies explicit.

## Current Status

The current pattern classes are intentionally minimal placeholders.
Each class exposes a stable interface (`name` + `run(...)`) and returns a TODO message that marks where full logic should be implemented.

## Patterns Included

- ReAct loop (`react`)
- Plan and execute (`plan_execute`)
- Supervisor-worker delegation (`supervisor`)
- Router-to-specialists (`router`)
- Reflection and revision (`reflection`)

Pattern docs live in `docs/patterns/`:

- `docs/patterns/react.md`
- `docs/patterns/plan_execute.md`
- `docs/patterns/supervisor.md`
- `docs/patterns/router.md`
- `docs/patterns/reflection.md`

## Goals

- Provide clear, minimal pattern implementations with predictable interfaces
- Serve as a reference for agent orchestration design choices
- Reduce ambiguity when prototyping multi-step LLM systems

## Non-Goals

- This is not a full agent framework
- This is not tied to any specific model provider
- This is not a production deployment platform

## Quickstart

### Requirements

- Python 3.11+
- `uv`

### Install

```bash
uv sync --group dev
```

### Run Checks

```bash
uv run ruff check .
uv run pyright
uv run pytest
```

## Usage

```python
from agent_patterns import (
	PlanExecutePattern,
	ReActPattern,
	ReflectionPattern,
	RouterPattern,
	SupervisorPattern,
)

patterns = [
	ReActPattern(),
	PlanExecutePattern(),
	SupervisorPattern(),
	RouterPattern(),
	ReflectionPattern(),
]

for pattern in patterns:
	print(pattern.run("example task"))
```

## Project Layout

```text
src/agent_patterns/
  react/
  plan_execute/
  supervisor/
  router/
  reflection/
tests/
docs/patterns/
```

## License

Apache 2.0