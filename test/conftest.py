import pytest
import json

from app import app


@pytest.fixture
def client():
    client = app.test_client()

    yield client


def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))
