import pytesseract
from PIL import Image

# ✅ Optional: Set tesseract path if not in system PATH
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path: str) -> str: # type: ignore
    """
    Extracts text from the image at the given path using Tesseract OCR.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Extracted text or error message.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        return f"❌ Image OCR Error: {str(e)}"


from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"❌ Image OCR Error: {str(e)}"
