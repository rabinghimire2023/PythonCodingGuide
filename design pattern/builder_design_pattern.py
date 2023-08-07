class Document:
    def __init__(self):
        self.header = ""
        self.body = ""
        self.footer = ""

    def __str__(self):
        return f"{self.header}\n\n{self.body}\n\n{self.footer}"
from abc import ABC, abstractmethod

class DocumentBuilder(ABC):
    @abstractmethod
    def set_header(self):
        pass

    @abstractmethod
    def set_body(self):
        pass

    @abstractmethod
    def set_footer(self):
        pass

    @abstractmethod
    def get_document(self):
        pass
class PDFDocumentBuilder(DocumentBuilder):
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
    def __init__(self):
        self.document = Document()

    def set_header(self):
        self.document.header = "<html><head><title>HTML Document</title></head>"

    def set_body(self):
        self.document.body = "<body><h1>This is the HTML document body.</h1></body>"

    def set_footer(self):
        self.document.footer = "</html>"

    def get_document(self):
        return self.document


class PlainTextDocumentBuilder(DocumentBuilder):
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
    def __init__(self, builder):
        self.builder = builder

    def generate_document(self):
        self.builder.set_header()
        self.builder.set_body()
        self.builder.set_footer()

    def get_document(self):
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
