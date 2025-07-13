import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text

def extract_text_from_txt(file):
    return file.read().decode("utf-8")
