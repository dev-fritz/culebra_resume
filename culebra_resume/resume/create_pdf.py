import pdfkit

def create_pdf():
    # Lê o conteúdo do arquivo HTML
    with open("../../templates/basic.html", "r") as file:
        html_content = file.read()

    # Configurações opcionais
    options = {
        "page-size": "A4",
        "encoding": "UTF-8",
    }

    # Salva o conteúdo HTML como PDF
    pdfkit.from_string(html_content, "guide.pdf", options=options)

create_pdf()
