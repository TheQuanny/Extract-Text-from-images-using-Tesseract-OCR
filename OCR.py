import argparse
import pytesseract
from PIL import Image, ImageEnhance
import re


pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        # Pre-processing for clearer images (resize, convert to grayscale, and enhance contrast)
        image = image.resize((image.width * 2, image.height * 2))
        image = image.convert("L")
        #image = ImageEnhance.Contrast(image).enhance(0.1) 
        
        extracted_text = pytesseract.image_to_string(image, lang='eng', config='--psm 6') # --oem 1 -c preserve_interword_spaces=1


        #cleaned_text = re.sub(r'[^\w\s\n]', '', extracted_text)
        
        return extracted_text.strip()
    
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from images using Tesseract OCR")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    args = parser.parse_args()

    extracted_text = extract_text_from_image(args.image_path)
    
    # Display the extracted text
    if extracted_text:
        print("Extracted Text:\n")
        print(extracted_text)
    else:
        print("Text extraction failed.")