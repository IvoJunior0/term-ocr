from PIL import Image
from pathlib import Path
import pytesseract

def extract_text(image_input, lang="por+eng"):
    try:
        # Paths
        if isinstance(image_input, (str, Path)):
            with Image.open(image_input) as img:
                img = img.convert("L")
                img = img.point(lambda x: 0 if x < 140 else 255, '1')
                return pytesseract.image_to_string(img, lang=lang)

        # PIL.Image (Caso de clipboard ou url)
        elif isinstance(image_input, Image.Image):
            img = image_input.convert("L")
            img = img.point(lambda x: 0 if x < 140 else 255, '1')
            return pytesseract.image_to_string(img, lang=lang)

        else:
            raise TypeError(f"Formato inválido: {type(image_input)}")

    except FileNotFoundError:
        raise

    except Exception as e:
        raise RuntimeError(f"Erro ao processar imagem: {e}")