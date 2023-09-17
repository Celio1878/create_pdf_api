from typing import Any

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

styles = getSampleStyleSheet()


def pdf_templates() -> bytes:
    Story = [Spacer(1, 0.5 * cm)]

    doc = SimpleDocTemplate("templates.pdf", pagesize=A4)
    style = styles[
        "Normal",
        "BodyText",
    ]

    for i in range(100):
        text = ("This is Paragraph number %s. " % i) * 20
        paragraph: Any = Paragraph(text, style)
        Story.append(paragraph)
        Story.append(Spacer(1, 1 * cm))

    doc.build(Story, onFirstPage=first_page, onLaterPages=later_pages)

    return b""


def first_page(canvas, doc):
    title: str = "PDF Templates"
    page_info = "Templates"

    canvas.saveState()
    canvas.setFont("Helvetica", 14)
    canvas.drawCentredString(doc.width / 2, doc.height - 50, title)
    canvas.setFont("Helvetica", 10)
    canvas.drawCentredString(doc.width / 2, doc.height - 80, page_info)
    canvas.restoreState()


def later_pages(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 14)
    canvas.drawCentredString(doc.width / 2, doc.height - 50, "Page %d" % doc.page)
    canvas.restoreState()
