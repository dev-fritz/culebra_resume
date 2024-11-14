import pdfkit


def generate_pdf(
        data,
        template=1,
        page_size: str = "A4",
        encoding: str = "UTF-8"
) -> None:
    html_content = merge_data_in_template(data, template)

    options = {
        "page-size": page_size,
        "encoding": encoding,
    }

    pdfkit.from_string(html_content, "guide.pdf", options=options)


def merge_data_in_template(data: str, template: int) -> str:
    return 'html file modified'
