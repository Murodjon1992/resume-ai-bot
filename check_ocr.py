import pytesseract
from PIL import Image
import os

# Tesseract'ning o'rnatilgan yo‘lini belgilash (faqat kerak bo‘lsa, Windows uchun)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Qabul qilingan rasm orqali to‘lovni aniqlovchi funksiya
def check_payment_from_image(image_path: str, expected_card_last4="2846", min_amount=10000) -> bool:
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='eng+uzb+rus')

        text_lower = text.lower()

        # Karta raqami va minimal summa mavjudligini tekshiramiz
        card_match = expected_card_last4 in text_lower
        amount_match = any(str(amt) in text_lower for amt in [str(min_amount), f"{min_amount//1000} 000"])

        return card_match and amount_match
    except Exception as e:
        print(f"[OCR ERROR] {e}")
        return False
