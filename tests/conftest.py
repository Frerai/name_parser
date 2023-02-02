import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.app import create_app


@pytest.fixture(scope="session")
def fastapi_test_app() -> FastAPI:
    """Fixture for creating a FastAPI app for testing purposes.

    This fixture is sessions scoped to ensure the setup and teardown is
    performed only once per session, regardless of the number of tests
    requesting it."""
    return create_app()


@pytest.fixture(scope="class")
def client(fastapi_test_app: FastAPI):
    """Fixture yielding a FastAPI test client.

    This fixture is class scoped to ensure safe teardowns between test classes.
    """
    with TestClient(fastapi_test_app) as client:
        yield client