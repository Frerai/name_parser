import pytest
from fastapi import status
from fastapi.testclient import TestClient


def test_status_responses(client: TestClient):
    """Testing for correct status code at healthcheck."""
    response = client.get("/health/live")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.text == ""
    assert response.content == b""


@pytest.mark.parametrize("full_name, expected_status", [
    ("Elle Belle", status.HTTP_200_OK),
    ("Fortælle, Mig", status.HTTP_200_OK),
    ("Pif-Paf Puf.VÆK", status.HTTP_200_OK),
    ("", status.HTTP_400_BAD_REQUEST)
])
def test_parser_response(client: TestClient, full_name, expected_status):
    """Testing response with various status codes."""
    response = client.get(f"/api/v1/parse?full_name={full_name}")
    assert response.status_code == expected_status


@pytest.mark.parametrize("input_string, expected_raise_body", [
    ("", {
        "error": True,
        "description": "full_name cannot be empty!",
        "status": status.HTTP_400_BAD_REQUEST,
    }),
    ("😨", {
        "error": True,
        "description": "no use of emojis allowed!",
        "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
    }),
    ("😌😨, 😌 😌", {
        "error": True,
        "description": "no use of emojis allowed!",
        "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
    }),
    ("😹 😹😹😹 😹😹 😹 😹😹 😹 ARE emojis allowed? 😹 😹😹", {
        "error": True,
        "description": "no use of emojis allowed!",
        "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
    })
])
def test_name_parser_exception_details(client: TestClient, input_string, expected_raise_body):
    """Testing details on the expected raises."""
    response = client.get(f"/api/v1/parse?full_name={input_string}")
    assert response.json() == expected_raise_body

