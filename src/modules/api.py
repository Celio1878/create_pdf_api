from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from src.modules.dtos.HtmlDto import HtmlDto
from src.modules.dtos.JsonToPdfDto import JsonToPdfDto
from src.services.create_pdf_from_html import create_pdf_from_html
from src.services.create_pdf_from_json import create_pdf_from_json

app = FastAPI(
    title="Convert to .PDF",
    version="1.0",
    description="Convertf .json or html string to .pdf and save doc in S3 key",
    docs_url="/docs",
)


@app.get("/", include_in_schema=False, status_code=301)
def docs_redirect() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.post("/create_pdf_from_json")
async def convert_json_to_pdf(dto: JsonToPdfDto) -> JSONResponse:
    """Create a PDF file from JSON data structure"""
    print(dto, "JSON DTO", type(dto), sep="\n")

    [err, success] = create_pdf_from_json(data=dto)

    if err:
        response = JSONResponse(content=err, status_code=400)
        return response

    response = JSONResponse(content=success, status_code=200)
    return response


@app.post("/create_pdf_from_html")
async def convert_html_to_pdf(dto: HtmlDto) -> JSONResponse:
    """Convert html string to pdf file"""
    print(dto, "HTML DTO")

    [err, succes] = create_pdf_from_html(
        html_string=dto.html_string,
        aws_config=dto.aws_config,
        doc_name=dto.doc_name,
        bucket_directory=dto.bucket_directory,
    )

    if err:
        response = JSONResponse(content=err, status_code=400)
        return response

    response = JSONResponse(content=succes, status_code=200)
    return response
