from pydantic import BaseModel
from src.repo.save_pdf import AWSConfig


class HtmlDto(BaseModel):
    html_string: str
    aws_config: AWSConfig
    doc_name: str
    bucket_directory: str
