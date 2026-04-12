def save_text(text, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)