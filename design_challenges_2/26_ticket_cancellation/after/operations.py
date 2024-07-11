from datetime import datetime
from typing import Any, Protocol

from models import Event, Ticket


class NoAvailableTickets(Exception):
    pass


class NotFoundError(Exception):
    pass

class TooLateMan(Exception):
    pass


class EventCreate(Protocol):
    title: str
    location: str
    start_date: datetime
    end_date: datetime
    available_tickets: int

    def dict(self) -> dict[str, Any]:
        ...


class TicketCreate(Protocol):
    event_id: int
    customer_name: str
    customer_email: str

    def dict(self) -> dict[str, Any]:
        ...


class Database(Protocol):
    def add(self, instance: object, _warn: bool = True) -> None:
        ...

    def commit(self) -> None:
        ...

    def delete(self, instance: object) -> None:
        ...

    def query(self, instance: object) -> Any:
        ...

    def refresh(self, instance: object) -> None:
        ...


def create_event(event: EventCreate, database: Database) -> Event:
    db_event = Event(**event.dict())
    database.add(db_event)
    database.commit()
    database.refresh(db_event)
    return db_event


def delete_event(event_id: int, database: Database) -> Event:
    event = get_event(event_id, database)
    database.delete(event)
    database.commit()
    return event


def get_event(event_id: int, database: Database) -> Event:
    event = database.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise NotFoundError(f"Event with id {event_id} not found.")
    return event


def get_all_events(database: Database) -> list[Event]:
    events = database.query(Event).all()
    return events


def book_ticket(ticket: TicketCreate, database: Database) -> Ticket:
    event = get_event(ticket.event_id, database)
    if event.available_tickets < 1:
        raise NoAvailableTickets()

    db_ticket = Ticket(**ticket.dict())
    database.add(db_ticket)
    database.commit()
    database.refresh(db_ticket)

    event.available_tickets -= 1
    database.commit()

    return db_ticket


def get_ticket(ticket_id: int, database: Database) -> Ticket:
    ticket = database.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise NotFoundError(f"Ticket with id {ticket_id} not found.")
    return ticket


def delete_ticket(ticket_id: int, database: Database) -> Ticket:
    ticket = database.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise NotFoundError(f"Ticket with id {ticket_id} not found.")
    event = get_event(ticket.event_id, database)
    if event.start_date <= datetime.now():
        raise TooLateMan("Too late motherfucker!")
    event.available_tickets += 1
    database.delete(ticket)
    database.commit()
    return ticket


def update_ticket_name(ticket_id: int, customer_name: str, database: Database):
    ticket = get_ticket(ticket_id)
    ticket.customer_name = customer_name
    database.commit()
    return ticket


def delete_event(event_id: int, database: Database):
    event = get_event(event_id)
    ticket_list = database.query(Ticket).filter(Ticket.event_id == event_id).all()
    for ticket in ticket_list:
        database.delete(ticket)
    database.delete(event)
    database.commit()
    return event()