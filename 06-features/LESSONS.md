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