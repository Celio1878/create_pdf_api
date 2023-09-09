import boto3
from pydantic import BaseModel


class AWSConfig(BaseModel):
    aws_access_key_id: str
    aws_secret_access_key: str
    region_name: str
    bucket_name: str


def s3_config(config: AWSConfig):
    aws_session = boto3.Session(
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key,
        region_name=config.region_name,
    )

    s3_client = aws_session.client("s3")

    return s3_client


def save_pdf(pdf: bytes, doc_name: str, bucket_directory: str, config: AWSConfig):
    key = bucket_directory + "/" + doc_name

    repo_client = s3_config(config)
    repo_client.put_object(Bucket=config.bucket_name, Key=key, Body=pdf)
