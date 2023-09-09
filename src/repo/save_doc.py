import boto3

AWS_ACCESS_KEY = "AKIARXYCRBD3RRJL2YFF"
AWS_SECRET_KEY = "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"
REGION = "sa-east-1"
BUCKET = "beyourstories"


def save_doc(doc):
    aws_session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=REGION,
    )
    s3_client = aws_session.client("s3")
    s3_client.put_object(Bucket=BUCKET, Key="test.pdf", Body=doc)
