import os
from typing import Any

from save_pdf import s3_config, save_pdf

aws_access_key_id = os.getenv("AWS_ACCESS_KEY") or "test"
aws_secret_access_key = os.getenv("AWS_SECRET_KEY") or "test"
region_name = os.getenv("REGION") or "test"
bucket_name = os.getenv("BUCKET") or "test"


# Test if pdf doc is saved in aws s3 bucket
def test_pdf_doc_saved_in_s3():
    client_config: Any = {
        aws_access_key_id,
        aws_secret_access_key,
        region_name,
        bucket_name,
    }

    pdf_bytes: bytes = b"test"

    save_pdf(pdf_bytes, "test.pdf", "", config=client_config)

    assert (
        s3_config(client_config).list_objects(Bucket=bucket_name)["Contents"][0]["Key"]
        == "test.pdf"
    )

    s3_config(client_config).delete_object(Bucket="beyourstories", Key="test.pdf")

    assert (
        s3_config(client_config).list_objects(Bucket="beyourstories")["Contents"] == []
    )
    assert s3_config(client_config).list_buckets()["Buckets"] == []
    assert (
        s3_config(client_config).list_objects(Bucket="beyourstories")["Contents"] == []
    )
    assert s3_config(client_config).list_buckets()["Buckets"] == []
    assert (
        s3_config(client_config).list_objects(Bucket="beyourstories")["Contents"] == []
    )
    assert s3_config(client_config).list_buckets()["Buckets"] == []
