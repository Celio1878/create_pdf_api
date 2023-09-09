from typing import Any, List

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from src.repo.save_pdf import AWSConfig, save_pdf
from src.utils.mm_to_points import mm_to_points


class CreatePdfFromJson:
    json_data: List
    aws_config: AWSConfig
    doc_name: str
    bucket_directory: str


pdf_max_height = mm_to_points(280)
pdf_min_height = mm_to_points(5)


def create_pdf_from_json(
    data: CreatePdfFromJson | Any,
) -> tuple[str | None, str | None]:
    left_space = mm_to_points(20)

    pdf = canvas.Canvas("./test.pdf", pagesize=A4)
    pdf.drawString(left_space, pdf_max_height, "PDF created")
    pdf.setAuthor("Celio Vieira")
    pdf.setFont("Helvetica", size=18)

    pdf.showPage()
    pdf_data = pdf.getpdfdata()
    save_pdf(
        pdf_data,
        config=data.aws_config,
        bucket_directory=data.bucket_directory,
        doc_name=data.doc_name,
    )

    err = None
    success = "Created Doc"

    return err, success
