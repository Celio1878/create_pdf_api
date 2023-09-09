import logging
from io import BytesIO

import boto3
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa

AWS_ACCESS_KEY = "AKIARXYCRBD3RRJL2YFF"
AWS_SECRET_KEY = "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"
REGION = "sa-east-1"
BUCKET = "beyourstories"
AUTHOR = "Celio Vieira"
CREATOR = "Celio Vieira"

app = FastAPI(
    title="Create .PDF doc",
    version="1.0",
    description="Create .pdf docs",
)


@app.get("/", include_in_schema=False)
def docs_redirect() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.get("/create_pdf_from_json")
async def create_pdf_from_json() -> str:
    """Create a PDF file"""

    left_space = mm_to_points(20)
    text_pdf_height = mm_to_points(280)

    pdf = canvas.Canvas("./test.pdf", pagesize=A4)
    pdf.drawString(left_space, text_pdf_height, "PDF created")
    pdf.setAuthor(AUTHOR)
    pdf.setCreator(CREATOR)
    pdf.setFont("Helvetica", size=18)

    pdf.showPage()

    # Create a file in S3 bucket

    pdf_data = pdf.getpdfdata()

    save_doc(pdf_data)

    message = "Doc created"
    logging.info(message)

    return message


@app.get("/create_pdf_from_html")
async def create_pdf_from_html() -> str:
    """Convert html string to pdf"""

    source_html = "<p style='color: #ff33aa'><strong>A big man create a new world</strong></p>\n<p>But, at a moment, he <ins>dies</ins></p>"

    file = BytesIO()

    if file:
        pisa.pisaDocument(BytesIO(source_html.encode("UTF-8")), file)

        save_doc(file.getvalue())

        file.seek(0)

        message = "Doc converted"
        logging.info(message)

        return message

    return "Error"


def mm_to_points(mm: float) -> float:
    return mm / 0.352777


def save_doc(doc):
    aws_session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=REGION,
    )
    s3_client = aws_session.client("s3")
    s3_client.put_object(Bucket=BUCKET, Key="test.pdf", Body=doc)
