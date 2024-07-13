from events import subscribe
from messaging import send_sms, send_email


def send_event_created_email(event_title: str):
    send_email(f'Check out the new awesome Event: {event_title}')

def send_ticket_booked_email(customer_name: str, event_id: str):
    send_email(f'{customer_name}! You have booked a fucking ticket: {event_id}')

def send_ticket_booked_sms(customer_name: str, event_id: str):
    send_sms(f'{customer_name}! You have booked a fucking ticket: {event_id}')


def subscribe_to_event_created():
    subscribe('event_created', send_event_created_email)

def subscribe_to_ticket_booked():
    print("Subscribing to 'ticket_booked'")
    subscribe('ticket_booked', send_ticket_booked_sms)
    subscribe('ticket_booked', send_ticket_booked_email)