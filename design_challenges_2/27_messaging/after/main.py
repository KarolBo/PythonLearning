from fastapi import Depends, FastAPI, HTTPException
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from db import EventCreate, TicketCreate, TicketUpdate
import operations
import uvicorn

from events import call_event
from listeners import subscribe_to_event_created, subscribe_to_ticket_booked

SQLALCHEMY_DATABASE_URL = "sqlite:///./events.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Initialize database session
def get_db():
    database = SessionLocal()
    yield database
    database.close()


subscribe_to_event_created()
subscribe_to_ticket_booked()


# Create event
@app.post("/events")
async def create_event(event: EventCreate, database: Session = Depends(get_db)):
    event = operations.create_event(event, database)
    call_event('event_created', event.title)
    return event


# Delete event
@app.delete("/events/{event_id}")
async def delete_event(event_id: int, database: Session = Depends(get_db)):
    try:
        event = operations.get_event(event_id, database)
    except operations.NotFoundError as exc:
        raise HTTPException(status_code=404) from exc
    operations.delete_event(event, database)
    return event


# Get event by id
@app.get("/events/{event_id}")
async def get_event(event_id: int, database: Session = Depends(get_db)):
    try:
        event = operations.get_event(event_id, database)
    except operations.NotFoundError as exc:
        raise HTTPException(status_code=404) from exc
    return event


# Get all events
@app.get("/events")
async def get_all_events(database: Session = Depends(get_db)):
    return operations.get_all_events(database)


# Book ticket
@app.post("/tickets")
async def book_ticket(ticket: TicketCreate, database: Session = Depends(get_db)):
    try:
        ticket = operations.book_ticket(ticket, database)
        call_event("ticket_booked", ticket.customer_name, ticket.event_id)
        return ticket
    except operations.NoAvailableTickets as exc:
        raise HTTPException(status_code=400) from exc


@app.get("/tickets/{ticket_id}")
async def get_ticket(ticket_id: int, database: Session = Depends(get_db)):
    try:
        ticket = operations.get_ticket(ticket_id, database)
    except operations.NotFoundError as exc:
        raise HTTPException(status_code=404) from exc
    return ticket


# Update ticket
@app.put("/tickets/{ticket_id}")
async def update_ticket(
    ticket_id: int, ticket_update: TicketUpdate, db: Session = Depends(get_db)
):
    try:
        return operations.update_ticket(ticket_id, ticket_update, db)
    except operations.NotFoundError as exc:
        raise HTTPException(status_code=404) from exc
    except operations.EventAlreadyStarted as exc:
        raise HTTPException(status_code=400) from exc


# Cancel ticket
@app.delete("/tickets/{ticket_id}")
async def cancel_ticket(ticket_id: int, db: Session = Depends(get_db)):
    try:
        return operations.delete_ticket(ticket_id, db)
    except operations.NotFoundError as exc:
        raise HTTPException(status_code=404) from exc
    except operations.EventAlreadyStarted as exc:
        raise HTTPException(status_code=400) from exc


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
