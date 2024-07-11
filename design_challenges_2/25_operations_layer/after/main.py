from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

import uvicorn

from db import EventCreate, TicketCreate
from models import Base
from operations import *

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


# Create event
@app.post("/events")
async def create_event(event: EventCreate, database: Session = Depends(get_db)):
    return event_create(event, database)


# Delete event
@app.delete("/events/{event_id}")
async def delete_event(event_id: int, database: Session = Depends(get_db)):
    event = event_get(event_id, database)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    event_delete(event)
    return event


# Get event by id
@app.get("/events/{event_id}")
async def get_event(event_id: int, database: Session = Depends(get_db)):
    event = event_get(event_id, database)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return


# Get all events
@app.get("/events")
async def get_all_events(database: Session = Depends(get_db)):
    return event_get_all(database)


# Book ticket
@app.post("/tickets")
async def book_ticket(ticket: TicketCreate, database: Session = Depends(get_db)):
    event = event_get(ticket.event_id, database)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if event.available_tickets < 1:
        raise HTTPException(status_code=400, detail="No available tickets")

    return ticket_create(ticket, event, database)

@app.get("/tickets/{ticket_id}")
async def get_ticket(ticket_id: int, database: Session = Depends(get_db)):
    ticket = ticket_get(ticket_id, database)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
