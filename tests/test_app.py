import pytest
from flask import url_for
from backend.app import app, contacts

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    """Testet die GET-Anfrage an '/'"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Titel" in response.data  # grobe Überprüfung, ob Seite gerendert wird

def test_add_title_success(client):
    """Testet das Hinzufügen eines neuen Titels über POST"""
    response = client.post("/", data={
        "action": "add-title",
        "new-title": "Ing.",
        "gender": "männlich"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"erfolgreich hinzugef" in response.data

def test_add_title_duplicate(client):
    """Doppelter Titel sollte Warnung auslösen"""
    # Erst hinzufügen
    client.post("/", data={
        "action": "add-title",
        "new-title": "TestTitel",
        "gender": "männlich"
    })
    # Dann erneut versuchen
    response = client.post("/", data={
        "action": "add-title",
        "new-title": "TestTitel",
        "gender": "männlich"
    }, follow_redirects=True)

    assert b"bereits vorhanden" in response.data

def test_split_valid_contact(client):
    response = client.post("/split", json={"new_contact": "Herr Dr. Max Mustermann"})
    assert response.status_code == 200
    assert "last_name" in response.get_json()

def test_split_empty_contact(client):
    response = client.post("/split", json={"new_contact": ""})
    assert response.status_code == 400
    assert response.get_json()["error"] == "Leerer Kontakt"

def test_save_contact(client):
    contacts.clear()
    payload = {
        "first_name": "Anna",
        "last_name": "Musterfrau",
        "gender": "weiblich",
        "language": "DE",
        "titles": "Dr."
    }
    response = client.post("/save_contact", json=payload)
    assert response.status_code == 200
    assert response.get_json()["status"] == "success"
    assert contacts[-1]["last_name"] == "Musterfrau"

def test_briefanrede_valid(client):
    contacts.clear()
    contacts.append({
        "first_name": "Anna",
        "last_name": "Musterfrau",
        "gender": "weiblich",
        "language": "DE",
        "titles": "Dr."
    })
    response = client.get("/briefanrede/0")
    assert response.status_code == 200
    assert "Frau" in response.get_data(as_text=True)

def test_briefanrede_invalid_index(client):
    contacts.clear()
    response = client.get("/briefanrede/999")
    assert response.status_code == 404
    assert "Kontakt nicht gefunden" in response.get_data(as_text=True)
