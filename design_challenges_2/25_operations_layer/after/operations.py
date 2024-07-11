from sqlalchemy.orm import Session
from fastapi import HTTPException

from models import Event, Ticket




def event_create(event: Event, db: Session):
    db_event = Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def event_delete(event: Event, db: Session):
    db.delete(event)
    db.commit()

def event_get(event_id: int, db: Session):
    event = db.query(Event).filter(Event.id == event_id).first()
    return event

def event_get_all(db: Session):
    events = db.query(Event).all()
    return events

def ticket_create(event: Event, ticket: Ticket, db: Session):
    db_ticket = Ticket(**ticket.model_dump())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)

    event.available_tickets -= 1
    db.commit()

    return db_ticket



def ticket_get(ticket_id: int, db: Session):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    return ticket