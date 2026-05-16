# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Create virtualenv and install dependencies
uv venv && source .venv/bin/activate
uv pip install -e .

# Start the MCP server
uv run main.py

# Run tests
uv run pytest

# Run a single test
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

## Architecture

This project is an MCP (Model Context Protocol) server that exposes document-processing tools to AI assistants.

- [main.py](main.py) — Creates a `FastMCP` server instance and registers tools via `mcp.tool()(my_function)`. This is the entry point and the place to wire up new tools.
- [tools/](tools/) — Each file contains one or more tool functions. Currently: `math.py` (addition) and `document.py` (binary document → markdown conversion using `markitdown`).
- [tests/](tests/) — Pytest-based tests. Document conversion tests use real `.docx` and `.pdf` fixture files in `tests/fixtures/`.

## Defining MCP Tools

Tools are plain Python functions registered with the server:

```python
mcp.tool()(my_function)
```

Every tool function must follow this documentation pattern:

```python
from pydantic import Field

def my_tool(
    param1: str = Field(description="Detailed description of this parameter"),
    param2: int = Field(description="Explain what this parameter does"),
) -> ReturnType:
    """One-line summary.

    Detailed explanation of what this tool does.

    When to use (and when NOT to use) this tool.

    Example:
        Input: ...
        Output: ...
    """
```

Use `Field` from pydantic (not plain type annotations) for all parameters so that descriptions are surfaced in the MCP schema.
