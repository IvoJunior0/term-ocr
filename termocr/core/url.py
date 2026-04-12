import requests
from PIL import Image
from io import BytesIO

def get_image_from_url(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        if "image" not in response.headers["Content-Type"]:
            print("URL não contém imagem")
            return None

        return Image.open(BytesIO(response.content))

    except Exception as e:
        print(f"Erro ao baixar imagem: {e}")
        return None

    except requests.exceptions.Timeout:
        print("Erro: a requisição demorou muito (timeout).")

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")