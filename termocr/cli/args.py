import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", nargs="?", help="Imagem a ser analisada.")
    parser.add_argument("-l", "--lang", default="por+eng", help="Definir linguagem da imagem manualmente. Linaguens aceitas do Tesseract.")
    parser.add_argument("-o", "--output", help="Imprimir o resultado em um arquivo separado.")
    parser.add_argument("-c", "--clipboard", action="store_true", help="Extrair texto da última print tirada (clipboard). No caso de sistemas Linux é necessário xclip ou wl-paste para funcionar.")
    parser.add_argument("--url", help="Extrair texto de uma imagem em URL. Para melhores resultados, não use SVG e/ou coloque a URL entras aspas.")
    return parser.parse_args()