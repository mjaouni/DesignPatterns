# Document Converter Interface
class DocumentConverter:
    def convert(self):
        pass


class PDFConverter(DocumentConverter):
    def convert(self):
        print("Document Converted to PDF")


class WordConverter(DocumentConverter):
    def convert(self):
        print("Document Converted to Word")


class ExcelConverter(DocumentConverter):
    def convert(self):
        print("Document Converted to Excel")


class DocumentConversionFactory():
    @staticmethod
    def create_converter(converter_type):
        if converter_type == "PDF":
            return PDFConverter()
        elif converter_type == "Word":
            return WordConverter()
        elif converter_type == "Excel":
            return ExcelConverter()


# Usage
converter = DocumentConversionFactory.create_converter("PDF")
converter.convert()
