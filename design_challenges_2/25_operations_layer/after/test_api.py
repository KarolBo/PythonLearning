from datetime import datetime

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
import pytest

from main import app, get_db
from models import Base, Event

client = TestClient(app)

engine = create_engine("sqlite:///:memory:",
                        connect_args={ "check_same_thread": False },
                        poolclass=StaticPool)

Base.metadata.create_all(bind=engine)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    database = TestingSessionLocal()
    yield database
    database.close()


app.dependency_overrides[get_db] = override_get_db


def test_create_event():
    event_data = {
        'title': 'gay party',
        'location': 'u twojej starej',
        "start_date": "2023-09-22T12:00:00",
        "end_date": "2023-09-22T14:00:00",
        'available_tickets': 100
    }
    response = client.post("/events", json=event_data)

    received_event = response.json()
    assert response.status_code == 200
    assert "id" in received_event
    assert received_event['title'] == event_data['title']
    assert received_event['location'] == event_data['location']
    assert received_event['start_date'] == event_data['start_date']
    assert received_event['end_date'] == event_data['end_date']
    assert received_event['available_tickets'] == event_data['available_tickets']


def test_getting_not_existing_event():
    fake_id = 101
    response = client.get(f'/events/{fake_id}')
    assert response.status_code == 404


def test_tickets_not_available():
    event_data = {
        'title': 'gay party',
        'location': 'u twojej starej',
        "start_date": datetime.strptime("2023-09-22 12:00:00", '%Y-%m-%d %H:%M:%S'),
        "end_date": datetime.strptime("2023-09-22 14:00:00", '%Y-%m-%d %H:%M:%S'),
        'available_tickets': 0
    }
    db = next(override_get_db())
    new_event = Event(**event_data)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    ticket_data = {
        "event_id": new_event.id,
        "customer_name": "Jon Doe",
        "customer_email": "test@example.com",
    }

    response = client.post('/tickets', json=ticket_data)
    assert response.status_code == 400