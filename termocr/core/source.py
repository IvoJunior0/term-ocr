from termocr.core.clipboard import get_clipboard_image
from termocr.core.url import get_image_from_url

def get_input_source(args):
    if args.clipboard:
        image = get_clipboard_image()

    elif args.url:
        image = get_image_from_url(args.url)

    elif args.image:
        image = args.image

    else:
        print("Erro: informe uma imagem, URL ou use --clipboard.")
        return None
    
    return image