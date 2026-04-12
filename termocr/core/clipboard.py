import sys
import io
import subprocess
from PIL import ImageGrab, Image

def get_clipboard_image_linux():
    commands = [
        ["wl-paste", "--type", "image/png"],
        ["xclip", "-selection", "clipboard", "-t", "image/png", "-o"]
    ]

    for cmd in commands:
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.stdout:
                return Image.open(io.BytesIO(result.stdout))
        except FileNotFoundError:
            continue
    print("Erro: Nenhuma imagem foi encontrada. Caso de Linux, verifique se xclip ou wl-paste estão instalados.")
    return None

def get_clipboard_image():
    if sys.platform.startswith("linux"):
        return get_clipboard_image_linux()
    else:
        return ImageGrab.grabclipboard()