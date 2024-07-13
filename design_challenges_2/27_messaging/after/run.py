import requests


def create_new_event(title: str):
    # Create a new event
    event_data = {
        "title": title,
        "location": "Amsterdam",
        "start_date": "2023-03-15 09:00:00",
        "end_date": "2023-03-18 16:00:00",
        "available_tickets": 50,
    }

    response = requests.post("http://localhost:8000/events", json=event_data, timeout=5)

    print(response.json())

def book_ticket(event_id: int):
    # Book tickets
    ticket_data = {
        "event_id": event_id,
        "customer_name": "Jon Doe",
        "customer_email": "test@example.com",
    }

    response = requests.post(
        "http://localhost:8000/tickets", json=ticket_data, timeout=5
    )

    print(response.json())

if __name__ == '__main__':
    create_new_event('gay party')
    book_ticket(1)