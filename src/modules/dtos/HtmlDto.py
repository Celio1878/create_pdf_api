from src.repo.save_doc import AWSConfig


class HtmlDto:
    html_string: str
    aws_config: AWSConfig
    doc_name: str
    bucket_directory: str
