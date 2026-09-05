import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_status_code(client):
    """A rota / deve responder com sucesso (200)."""
    response = client.get("/")
    assert response.status_code == 200


def test_home_retorna_json(client):
    """A rota / deve retornar um JSON com as chaves esperadas."""
    response = client.get("/")
    data = response.get_json()
    assert "mensagem" in data
    assert "host" in data
    assert "versao" in data


def test_health_status_code(client):
    """A rota /health deve responder com sucesso (200)."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_retorna_status_ok(client):
    """A rota /health deve confirmar que o status é 'ok'."""
    response = client.get("/health")
    data = response.get_json()
    assert data["status"] == "ok"
