# ocr_pdf_image_parser.py

from PIL import Image
import pytesseract
import PyPDF2

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                text += page_text if page_text else ""
        print("📄 Extracted PDF Text:\n", text.strip())
    except Exception as e:
        print("❌ PDF Error:", e)

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        print("🖼️ Extracted Image Text:\n", text.strip())
    except Exception as e:
        print("❌ Image OCR Error:", e)

# 🔍 Run both extractors
extract_text_from_pdf("automation/sample.pdf")
extract_text_from_image("automation/sample_image.png")
