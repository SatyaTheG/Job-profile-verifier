# Import necessary packages for text extraction
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re

def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    string_io = StringIO()
    pdf_converter = TextConverter(resource_manager, string_io, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, pdf_converter)

    with open(pdf_path, 'rb') as file:
        for page in PDFPage.get_pages(file, caching=True, check_extractable=True):
            page_interpreter.process_page(page)

    text = string_io.getvalue()
    pdf_converter.close()
    string_io.close()
    text = re.sub(r'\s+', ' ', text)

    return text