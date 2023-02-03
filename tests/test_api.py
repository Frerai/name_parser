import pytest
from fastapi import status
from fastapi.testclient import TestClient


def test_status_responses(client: TestClient):
    """Testing for correct status code at healthcheck."""
    response = client.get("/health/live")
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.parametrize("full_name, expected_status", [
    ("Elle Belle", status.HTTP_200_OK),
    ("Fortælle, Mig", status.HTTP_200_OK),
    ("Pif-Paf Puf", status.HTTP_200_OK),
    ("", status.HTTP_400_BAD_REQUEST)
])
def test_parser_response(client: TestClient, full_name, expected_status):
    """Testing response with various status codes."""
    response = client.get(f"/api/v1/parse?full_name={full_name}")
    assert response.status_code == expected_status
