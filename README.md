# agent-patterns

Reference implementations of common agentic AI orchestration patterns in Python.

## Overview

Modern LLM applications increasingly rely on multi-step agent systems rather than single prompts. This repo documents and implements common patterns used to build reliable, extensible agent architectures.

## Patterns Included

- Planner–Executor decomposition
- Tool-using agents
- Reflection loops
- Multi-agent collaboration
- Retrieval-augmented reasoning flows
- State-driven orchestration
- Failure recovery patterns

## Goals

- Provide clear, minimal implementations of agent design patterns
- Serve as a reference for building production-grade agent systems
- Reduce ambiguity in multi-step LLM orchestration design

## Non-Goals

- This is not a full agent framework
- This is not tied to any specific model provider
- This is not intended as a production deployment system

## Example Use Cases

- Designing research assistants
- Building automated workflows
- Structuring tool-using LLM systems
- Prototyping orchestration logic

## License

Apache 2.0

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
This repository focuses on *architectural patterns* rather than a single framework or product. The goal is to explore how complex behaviors can be structured from simple, reusable agent components.