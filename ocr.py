import easyocr
import numpy as np

def ocr_plate_number(image_pil):
    """
    Performs OCR on the provided image to extract a plate number.

    Args:
        image_pil: A PIL Image object containing the license plate.

    Returns:
        A string representing the detected plate number, or an empty string if none found.
    """
    try:
        # Convert PIL Image to a NumPy array
        image_np = np.array(image_pil)

        # Initialize EasyOCR reader
        # Specify languages (e.g., ['en'] for English)
        # Consider installing language models if needed: !pip install easyocr[full]
        reader = easyocr.Reader(['en'])

        # Read text from the image
        result = reader.readtext(image_np)

        # Extract and join detected text
        plate_text = "".join([text[1] for text in result])

        # You might want to add some validation or filtering here
        # to ensure the extracted text looks like a license plate.

        return plate_text.strip() # Return the cleaned text
    except Exception as e:
        print(f"Error during OCR: {e}")
        return "" # Return empty string on error
