import json
import hashlib

# from app.api.routes import api_bp
from prod_ready_api.api.routes import generate_random_array, api_bp
from .conftest import client
from tests.resources.mocked_output import mock_output


def test_generate_array(client):
    # Prepare a mock sentence for testing
    test_sentence = "Hello everyone"
    expected_response = {
        "sentence": test_sentence,
        "random_array": mock_output,
    }

    # Prepare the JSON payload
    data = {"sentence": test_sentence}

    # Send a POST request to the endpoint
    response = client.post("/api/generate_random_array", json=data)

    # Assert the response status code
    assert response.status_code == 200

    # Assert the response JSON content
    assert response.json == expected_response


def test_generate_random_array_missing_sentence(client):
    """
    Test generating random array with missing sentence
    """
    response = client.post("/api/generate_random_array", json={})

    assert response.status_code == 400
    assert "error" in response.json  # Ensure "error" key is present in JSON response
    assert response.json["error"] == "Please provide a valid input"
