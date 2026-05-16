# Features

## Images

An aproximate formula for estimating token usage from images is `width px * height px / 750`.

Additional considerations when working with images can be found at https://platform.claude.com/docs/en/build-with-claude/vision.

## Documents

Common document types are PDFs and text files.

Considerations for PDFs are documented at https://platform.claude.com/docs/en/build-with-claude/pdf-support.

Optimization suggestions:
- Place PDFs before instructions
- Split large PDFs into smaller parts

For larger files or files that are reused more frequently, the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) can be used to upload the files and then reference the file by the file ID.

## Prompt Caching

Caching can be enabled by adding a cache breakpoint to a block. That block and all previous block will then be cached.
Up to 4 cache breakpoints can be specified.
Content of all messages must be at least 1024 tokens long to be cached.

Supported blocks are:
- Text
- System prompt
- Tool definition, use and result
- Image

Block order:
1. Tool
2. System
3. Message

## Code Execution

Code execution can be enabled by passing in a code execution tool. See https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool for the appropriate tool for each model.

Code execution combines well with the Files API to work with files either as inputs or outputs.

The code is executed in containers, which are isolated from the network and focused on running Python.
They can be reused and expire 30 days after creation.
