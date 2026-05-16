from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pathlib import Path
from pydantic import Field

SUPPORTED_EXTENSIONS = {".docx", ".pdf"}


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    path: str = Field(description="Absolute or relative path to a PDF or DOCX file"),
) -> str:
    """Convert a PDF or DOCX file at the given path to markdown text.

    Reads the file from disk, converts its contents to markdown, and returns
    the result as a string.

    When to use:
    - When you have a local file path and need its content as markdown
    - Supports .pdf and .docx files (case-insensitive extension)

    When NOT to use:
    - When you already have the file's binary content (use binary_document_to_markdown)
    - For unsupported file types

    Example:
        Input: path="/docs/report.pdf"
        Output: "# Report\\n\\nContent of the report..."
    """
    p = Path(path)

    if not path:
        raise ValueError("path must not be empty")

    if not p.exists():
        raise FileNotFoundError(f"No file found at: {path}")

    ext = p.suffix.lower()
    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type '{ext}'. Supported: {SUPPORTED_EXTENSIONS}")

    return binary_document_to_markdown(p.read_bytes(), ext.lstrip("."))
