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


def see_all_events():
    # Retrieve all events
    response = requests.get("http://localhost:8000/events", timeout=5)
    print(response.json())


def delete_event(event_id: int):
    # Delete an event from the database
    url = f"http://localhost:8000/events/{event_id}"
    response = requests.delete(url, timeout=5)
    if response.status_code == 200:
        print(f"Event with id {event_id} and all its tickets deleted successfully.")
    else:
        print(f"Error deleting event with id {event_id}: {response.content}")


def update_ticket_name():
    ticket_id = 1
    new_customer_name = "John Smith"

    url = f"http://localhost:8000/tickets/{ticket_id}"
    # headers = {"Content-Type": "application/json"}
    data = {"customer_name": new_customer_name}

    response = requests.put(url, json=data, timeout=5)

    if response.ok:
        print("Ticket customer name updated successfully")
    else:
        print(f"Error updating ticket customer name: {response.text}")


def delete_ticket(ticket_id: int):
    # Delete a ticket from the database
    url = f"http://localhost:8000/tickets/{ticket_id}"
    response = requests.delete(url, timeout=5)
    if response.status_code == 200:
        print(f"Ticket with id {ticket_id} deleted successfully.")
    else:
        print(f"Error deleting ticket with id {ticket_id}: {response.content}")


if __name__ == "__main__":
    create_new_event("Python_Conf")  # Define parameters in the function
    create_new_event("Ruby_Conf")  # Create dupilcate event for checking deletion
    see_all_events()  # You can also do that in the browser
    book_ticket(1)  # Define parameters in the function
    delete_ticket(ticket_id=1)
