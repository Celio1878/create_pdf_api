import os.path
from typing import Any, List

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from src.repo.save_pdf import AWSConfig, save_pdf


class CreatePdfFromJson:
    json_data: List
    aws_config: AWSConfig
    doc_name: str
    bucket_directory: str


pdf_max_height = cm * 29.7 - cm * 3.7
pdf_min_height = cm * 3.7
pdf_paragraph_width = cm * 21 - cm * 2.5

file_name = os.path.join(os.getcwd(), "src", "assets", "bys.jpeg")


def create_pdf_from_json(
    data: CreatePdfFromJson | Any,
) -> tuple[str | None, str | None]:
    """
    A4 size - 21cm x 29.7cm
    Border Top 3.7cm
    Border Bottom 3.7cm
    Border Left 2.5cm
    Border Right 2.5cm
    """

    pdf = canvas.Canvas("./test.pdf", pagesize=A4)
    pdf.drawImage(file_name, 0, pdf_max_height, width=cm * 3, height=cm * 3)
    pdf.drawString(pdf_paragraph_width, pdf_max_height, "PDF created")
    pdf.setAuthor("Celio Vieira")
    pdf.setFont("Helvetica", size=18)

    pdf.showPage()
    pdf.save()
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
