import os
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
pdf_max_width = cm * 21 - cm * 2.5
pdf_paragraph_width = cm * 2.5

image_file_name = os.path.join(os.getcwd(), "src", "assets", "bys.jpeg")


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
    page_number = pdf.getPageNumber()
    pdf.setFont("Helvetica", size=10)
    pdf.drawString(
        pdf_max_width - cm * 1, pdf_max_height + cm * 1.2, "Page: " + str(page_number)
    )
    pdf.drawImage(image_file_name, 0, pdf_max_height, width=cm * 3, height=cm * 3)
    pdf.setFont("Helvetica-Bold", size=18, leading=15)
    pdf.drawString(pdf_paragraph_width, pdf_max_height - cm * 2, "PDF created")
    pdf.line(
        pdf_max_width,
        pdf_max_height - cm * 5,
        pdf_paragraph_width,
        pdf_max_height - cm * 5,
    )
    pdf.setFont("Helvetica", size=14, leading=5)
    pdf.drawCentredString(cm * 21 / 2, pdf_min_height * 5.3, "Centralizado")
    pdf.drawString(
        pdf_paragraph_width,
        pdf_min_height * 5,
        "-" * 98,
    )
    pdf.setAuthor("Celio Vieira")

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
