from fastapi.testclient import TestClient
from src.modules.api import app

client = TestClient(app)


def test_create_pdf_from_json():
    response = client.get("/create_pdf_from_json")

    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }


def test_create_pdf_from_html():
    source_html = "<p style='color: #ff33aa'><strong>A big man create a new world</strong></p>\n<p>But, at a moment, he <ins>dies</ins></p>"

    response = client.post(
        "/test_create_pdf_from_html", json={"source_html": source_html}
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Doc converted"}
