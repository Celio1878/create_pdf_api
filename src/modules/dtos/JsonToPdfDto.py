from typing import List

from pydantic import BaseModel
from src.repo.save_pdf import AWSConfig


class JsonToPdfDto(BaseModel):
    json_data: List
    aws_config: AWSConfig
    doc_name: str
    bucket_directory: str
