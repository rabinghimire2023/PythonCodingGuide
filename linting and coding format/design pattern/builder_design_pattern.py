"""Builder design pattern"""
from abc import ABC, abstractmethod


class Document:
    """
    Document
    """
    def __init__(self):
        self.header = ""
        self.body = ""
        self.footer = ""

    def __str__(self):
        return f"{self.header}\n\n{self.body}\n\n{self.footer}"


class DocumentBuilder(ABC):
    """
    Document builder
    """
    @abstractmethod
    def set_header(self):
        """Set header
        """

    @abstractmethod
    def set_body(self):
        """Set body
        """
    @abstractmethod
    def set_footer(self):
        """Set footer
        """
    @abstractmethod
    def get_document(self):
        """Get document
        """


class PDFDocumentBuilder(DocumentBuilder):
    """PDF Dcoument builder

    Args:
        DocumentBuilder (class): Inherited base class Document Builder
    """
    def __init__(self):
        self.document = Document()

    def set_header(self):
        self.document.header = "PDF Header"

    def set_body(self):
        self.document.body = "This is the PDF document body."

    def set_footer(self):
        self.document.footer = "PDF Footer"

    def get_document(self):
        return self.document


class HTMLDocumentBuilder(DocumentBuilder):
    """
    HTML Dcoument Builder

    Args:
        DocumentBuilder (class): Inherited base class Document Builder
    """
    def __init__(self):
        self.document = Document()

    def set_header(self):
        self.document.header = "<html><head><title>TITLE</title></head>"

    def set_body(self):
        self.document.body = "<body><h1>Document body.</h1></body>"

    def set_footer(self):
        self.document.footer = "</html>"

    def get_document(self):
        return self.document


class PlainTextDocumentBuilder(DocumentBuilder):
    """Plain Text Document Builder

    Args:
        DocumentBuilder (class): Inherited base class document builder
    """
    def __init__(self):
        self.document = Document()

    def set_header(self):
        self.document.header = "Plain Text Document"

    def set_body(self):
        self.document.body = "This is the plain text document body."

    def set_footer(self):
        self.document.footer = "End of Plain Text Document"

    def get_document(self):
        return self.document


class DocumentGenerator:
    """Document Generator
    """
    def __init__(self, builder):
        self.builder = builder

    def generate_document(self):
        """Generate document
        """
        self.builder.set_header()
        self.builder.set_body()
        self.builder.set_footer()

    def get_document(self):
        """Get document
        """
        return self.builder.get_document()


if __name__ == "__main__":
    pdf_builder = PDFDocumentBuilder()
    html_builder = HTMLDocumentBuilder()
    plaintext_builder = PlainTextDocumentBuilder()

    generator = DocumentGenerator(pdf_builder)
    generator.generate_document()
    pdf_document = generator.get_document()
    print("PDF Document:\n", pdf_document)

    generator = DocumentGenerator(html_builder)
    generator.generate_document()
    html_document = generator.get_document()
    print("HTML Document:\n", html_document)

    generator = DocumentGenerator(plaintext_builder)
    generator.generate_document()
    plaintext_document = generator.get_document()
    print("Plain Text Document:\n", plaintext_document)
