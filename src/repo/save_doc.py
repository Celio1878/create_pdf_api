from typing import Any

import boto3


class AWSConfig:
    aws_access_key_id: str
    aws_secret_access_key: str
    region_name: str
    bucket_name: str


def save_pdf(pdf: Any, doc_name: str, bucket_directory: str, config: AWSConfig):
    aws_session = boto3.Session(
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key,
        region_name=config.region_name,
    )

    key = bucket_directory + "/" + doc_name + ".pdf"

    s3_client = aws_session.client("s3")
    s3_client.put_object(Bucket=config.bucket_name, Key=key, Body=pdf)
