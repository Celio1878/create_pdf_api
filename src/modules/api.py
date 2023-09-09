from io import BytesIO

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from repo.save_doc import save_doc
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from utils.mm_to_points import mm_to_points
from xhtml2pdf import pisa

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
    pdf_data = pdf.getpdfdata()
    save_doc(pdf_data)

    message = "Doc created"
    return message


@app.get("/create_pdf_from_html")
async def create_pdf_from_html(source_html: str) -> str:
    """Convert html string to pdf"""

    file = BytesIO()
    pisa.pisaDocument(BytesIO(source_html.encode("UTF-8")), file)

    pdf = file.getvalue()
    save_doc(pdf)

    file.seek(0)

    message = "Doc converted"
    return message
