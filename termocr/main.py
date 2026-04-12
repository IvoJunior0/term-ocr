from termocr.core.ocr import extract_text
from termocr.core.io import save_text
from termocr.cli.args import get_args
from termocr.utils.banner import BANNER
from termocr.core.source import get_input_source
import sys

def main():
    if len(sys.argv) == 1:
        print(BANNER)
        return
    try:
        args = get_args()
        
        image = get_input_source(args)
        if image is None:
            return
        
        text = extract_text(image, args.lang).strip()
        
        print(text)

        if args.output:
            save_text(text, args.output)
            print(f"Salvo em: {args.output}")
        
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {image}")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()