import logging
import os

import boto3
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
REGION = os.getenv("REGION")
BUCKET = os.getenv("BUCKET")
AUTHOR = os.getenv("AUTHOR")
CREATOR = os.getenv("CREATOR")

app = FastAPI(
    title="Convert to .PDF",
    version="1.0",
    description="Create .pdf docs",
)


@app.get("/", include_in_schema=False)
def docs_redirect() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.get("/test")
def test() -> str:
    message = "Endpoint Testing"

    return message


@app.get("/create_pdf")
async def create_pdf() -> str:
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

    aws_session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=REGION,
    )
    s3_client = aws_session.client("s3")
    s3_client.put_object(Bucket=BUCKET, Key="test.pdf", Body=pdf_data)

    message = "Doc created"
    logging.info(message)

    return message


def mm_to_points(mm: float) -> float:
    return mm / 0.352777
