# term-ocr

CLI para extração de texto de imagens diretamente pelo terminal utilizando OCR.

O **term-ocr** permite reconhecer texto a partir de imagens locais, URLs ou imagens disponíveis no clipboard, sem a necessidade de abrir ferramentas gráficas.

## Funcionalidades

* OCR de imagens locais
* OCR de imagens através de URL
* OCR diretamente do clipboard
* Salvar o texto reconhecido em um arquivo
* Suporte a diferentes idiomas do Tesseract
* Interface totalmente via terminal

## Tecnologias

* **Python**
* **Tesseract OCR**
* **Pytesseract**
* **Pillow**
* **Requests**
* **xclip / wl-paste** — clipboard no Linux

## Instalação

O `term-ocr` pode ser instalado como um comando global através do `pip`. Depois da instalação, o comando `termocr` fica disponível diretamente no terminal.

### Pré-requisitos

É necessário ter:

* Python 3.9 ou superior
* Tesseract OCR

### Linux

#### Fedora

Instale o Tesseract:

```bash
sudo dnf install tesseract tesseract-langpack-por
```

Para utilizar o recurso de clipboard:

```bash
sudo dnf install xclip wl-clipboard
```

#### Ubuntu / Debian

```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-por
```

Para clipboard:

```bash
sudo apt install xclip wl-clipboard
```

### Windows

Instale o **Python 3** e certifique-se de marcar a opção **"Add Python to PATH"** durante a instalação.

Em seguida, instale o **Tesseract OCR** e adicione o diretório de instalação do Tesseract ao `PATH` do Windows.

Depois de instalar os pré-requisitos, abra o PowerShell ou Prompt de Comando.

### Instalar globalmente

Clone o repositório:

```bash
git clone https://github.com/IvoJunior0/term-ocr.git
cd term-ocr
```

Instale o pacote:

```bash
pip install .
```

A partir desse momento, o comando `termocr` estará disponível globalmente no terminal.

Verifique a instalação:

```bash
termocr
```

Ou:

```bash
termocr --help
```

### Atualizar

Caso já tenha uma versão instalada e queira atualizar para a versão mais recente do código:

```bash
git pull
pip install --upgrade .
```

## Utilidades

### Imagem local

Passe o caminho da imagem como argumento:


```bash
termocr documento.png
```

O texto reconhecido será exibido diretamente no terminal.

Também é possível utilizar caminhos completos:

```bash
termocr /home/usuario/documentos/documento.png
```

No Windows:

```powershell
termocr "C:\Users\Usuario\Documents\documento.png"
```

---

### Imagem através de URL

Use a flag `--url`:

```bash
termocr --url "https://site.com/imagem.png"
```

Exemplo:

```bash
termocr --url "https://exemplo.com/documento.png"
```

> Recomenda-se colocar a URL entre aspas. Para melhores resultados, evite utilizar imagens SVG.

---

### Clipboard

Copie uma imagem para o clipboard e execute:

```bash
termocr --clipboard
```

Ou utilizando a forma curta:

```bash
termocr -c
```

O programa utilizará a imagem presente no clipboard como entrada para o OCR.

> No Linux, o recurso de clipboard depende do `xclip` ou `wl-paste`.

---

##  Flags

O `termocr` possui as seguintes opções:

| Flag                | Descrição                                |
| ------------------- | ---------------------------------------- |
| `-l`, `--lang`      | Define o idioma utilizado pelo Tesseract |
| `-o`, `--output`    | Salva o resultado do OCR em um arquivo   |
| `-c`, `--clipboard` | Utiliza a imagem presente no clipboard   |
| `--url`             | Utiliza uma imagem hospedada em uma URL  |

### `-l` / `--lang`

Define manualmente o idioma utilizado pelo Tesseract.

Por padrão, o `termocr` utiliza:

```text
por+eng
```

Ou seja, português e inglês.

Exemplo:

```bash
termocr documento.png --lang por
```

Ou:

```bash
termocr documento.png -l eng
```

Os idiomas disponíveis dependem dos pacotes de idioma instalados no Tesseract.

Para visualizar os idiomas disponíveis:

```bash
tesseract --list-langs
```

---

### `-o` / `--output`

Salva o texto reconhecido em um arquivo.

```bash
termocr documento.png -o resultado.txt
```

Também pode ser utilizado:

```bash
termocr documento.png --output resultado.txt
```

O texto continuará sendo exibido no terminal e também será salvo no arquivo especificado.

---

### `-c` / `--clipboard`

Utiliza a imagem presente no clipboard:

```bash
termocr -c
```

ou:

```bash
termocr --clipboard
```

---

### `--url`

Realiza OCR de uma imagem hospedada em uma URL:

```bash
termocr --url "https://site.com/imagem.png"
```

---



## Como funciona

O `term-ocr` possui três formas principais de entrada:

```text
                   ┌───────────────┐
                   │    termocr    │
                   └───────┬───────┘
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
        Imagem local      URL        Clipboard
             │             │             │
             └─────────────┼─────────────┘
                           ↓
                    Processamento
                     da imagem
                           ↓
                     Tesseract OCR
                           ↓
                     Texto extraído
                           ↓
                  ┌────────┴────────┐
                  ↓                 ↓
               Terminal          Arquivo
```

O Python é responsável pela interface de linha de comando e pelo gerenciamento das entradas, enquanto o **Tesseract OCR** realiza o reconhecimento óptico dos caracteres.

## Estrutura do projeto

```text
term-ocr/
├── termocr/
│   ├── cli/
│   │   └── args.py
│   ├── core/
│   │   ├── io.py
│   │   ├── ocr.py
│   │   └── source.py
│   ├── utils/
│   │   └── banner.py
│   ├── __init__.py
│   └── main.py
│
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Licença

Este projeto está disponível para fins de estudo e desenvolvimento pessoal.
