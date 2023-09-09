from io import BytesIO

from src.repo.save_pdf import AWSConfig, save_pdf
from xhtml2pdf import pisa


def create_pdf_from_html(
    html_string: str, aws_config: AWSConfig, doc_name: str, bucket_directory: str
) -> tuple:
    file = BytesIO()
    src_file = BytesIO(html_string.encode("UTF-8"))
    pisa.pisaDocument(src_file, file)

    pdf = file.getvalue()
    save_pdf(
        pdf=pdf,
        config=aws_config,
        doc_name=doc_name,
        bucket_directory=bucket_directory,
    )

    file.seek(0)

    err = None
    success = "Created Doc"

    return err, success
