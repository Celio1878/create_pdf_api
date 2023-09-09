from typing import List

from src.repo.save_doc import AWSConfig


class JsonToPdfDto:
    json_data: List
    aws_config: AWSConfig
    doc_name: str
    bucket_directory: str
