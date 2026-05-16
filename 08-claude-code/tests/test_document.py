import os
import pytest
from tools.document import binary_document_to_markdown, document_path_to_markdown


class TestBinaryDocumentToMarkdown:
    # Define fixture paths
    FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
    DOCX_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.docx")
    PDF_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.pdf")

    def test_fixture_files_exist(self):
        """Verify test fixtures exist."""
        assert os.path.exists(self.DOCX_FIXTURE), (
            f"DOCX fixture not found at {self.DOCX_FIXTURE}"
        )
        assert os.path.exists(self.PDF_FIXTURE), (
            f"PDF fixture not found at {self.PDF_FIXTURE}"
        )

    def test_binary_document_to_markdown_with_docx(self):
        """Test converting a DOCX document to markdown."""
        # Read binary content from the fixture
        with open(self.DOCX_FIXTURE, "rb") as f:
            docx_data = f.read()

        # Call function
        result = binary_document_to_markdown(docx_data, "docx")

        # Basic assertions to check the conversion was successful
        assert isinstance(result, str)
        assert len(result) > 0
        # Check for typical markdown formatting - this will depend on your actual test file
        assert "#" in result or "-" in result or "*" in result

    def test_binary_document_to_markdown_with_pdf(self):
        """Test converting a PDF document to markdown."""
        # Read binary content from the fixture
        with open(self.PDF_FIXTURE, "rb") as f:
            pdf_data = f.read()

        # Call function
        result = binary_document_to_markdown(pdf_data, "pdf")

        # Basic assertions to check the conversion was successful
        assert isinstance(result, str)
        assert len(result) > 0
        # Check for typical markdown formatting - this will depend on your actual test file
        assert "#" in result or "-" in result or "*" in result


class TestDocumentPathToMarkdown:
    FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
    DOCX_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.docx")
    PDF_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.pdf")

    def test_docx_returns_markdown(self):
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_docx_contains_expected_content(self):
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        assert "#" in result or "-" in result or "*" in result

    def test_pdf_returns_markdown(self):
        result = document_path_to_markdown(self.PDF_FIXTURE)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_pdf_contains_expected_content(self):
        result = document_path_to_markdown(self.PDF_FIXTURE)
        assert "#" in result or "-" in result or "*" in result

    def test_uppercase_extension_docx(self, tmp_path):
        upper_path = tmp_path / "mcp_docs.DOCX"
        import shutil
        shutil.copy(self.DOCX_FIXTURE, upper_path)
        result = document_path_to_markdown(str(upper_path))
        assert isinstance(result, str)
        assert len(result) > 0

    def test_uppercase_extension_pdf(self, tmp_path):
        upper_path = tmp_path / "mcp_docs.PDF"
        import shutil
        shutil.copy(self.PDF_FIXTURE, upper_path)
        result = document_path_to_markdown(str(upper_path))
        assert isinstance(result, str)
        assert len(result) > 0

    def test_file_not_found_raises(self):
        with pytest.raises(FileNotFoundError):
            document_path_to_markdown("/nonexistent/path/file.docx")

    def test_empty_path_raises(self):
        with pytest.raises((FileNotFoundError, ValueError)):
            document_path_to_markdown("")

    def test_unsupported_extension_raises(self):
        txt_path = os.path.join(self.FIXTURES_DIR, "dummy.txt")
        with open(txt_path, "w") as f:
            f.write("hello")
        try:
            with pytest.raises((ValueError, Exception)):
                document_path_to_markdown(txt_path)
        finally:
            os.unlink(txt_path)

    def test_corrupted_file_returns_string(self, tmp_path):
        # markitdown is lenient and returns a (possibly empty) string for corrupt files
        bad_path = tmp_path / "corrupt.docx"
        bad_path.write_bytes(b"not a real docx")
        result = document_path_to_markdown(str(bad_path))
        assert isinstance(result, str)

    def test_path_with_spaces(self, tmp_path: str):
        dest = tmp_path / "my docs" / "mcp_docs.docx"
        dest.parent.mkdir()
        import shutil
        shutil.copy(self.DOCX_FIXTURE, dest)
        result = document_path_to_markdown(str(dest))
        assert isinstance(result, str)
        assert len(result) > 0
