from app import app


def test_hello_world_should_return_Hello():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.is_json

    body = response.get_json()

    assert 'message' in body
    assert body['message'] == 'Hello'
