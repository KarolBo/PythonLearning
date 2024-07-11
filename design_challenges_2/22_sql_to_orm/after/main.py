from datetime import datetime

import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from models import Base, Event, Ticket

DB_URL = "sqlite:///./events.db"
engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(engine)
Base.metadata.create_all(engine)

app = FastAPI()


# Information needed to create an event
class EventCreate(BaseModel):
    title: str
    location: str
    start_date: datetime
    end_date: datetime
    available_tickets: int


# Information needed to create a ticket
class TicketCreate(BaseModel):
    event_id: int
    customer_name: str
    customer_email: str


# Initialize database connection
def get_db():
    db = SessionLocal()
    yield db
    db.close()


# Create event
@app.post("/events", response_model=None)
async def create_event(event: EventCreate, db: Session=Depends(get_db)) -> Event:
    new_event = Event(**event.model_dump())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


@app.delete("/events/{event_id}", response_model=None)
def delete_event(event_id: int, db: Session=Depends(get_db)) -> Event:
    event_do_delete = db.query(Event).filter(Event.id == event_id).first()
    if not event_do_delete:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event_do_delete)
    db.commit()
    return event_do_delete


# Get event by id
@app.get("/events/{event_id}", response_model=None)
async def get_event(event_id: int, db: Session=Depends(get_db)) -> Event:
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

# Get all events
@app.get("/events", response_model=None)
async def get_all_events(db: Session=Depends(get_db)) -> list[Event]:
    event_list = db.query(Event).all()
    return event_list

# Book ticket
@app.post("/tickets", response_model=None)
async def book_ticket(ticket: TicketCreate, db: Session=Depends(get_db)) -> Ticket:
    # Get the event
    event = db.query(Event).filter(Event.id == ticket.event_id).first()
    if event is None:
        raise HTTPException(
            status_code=404, detail=f"Event with id {ticket.event_id} not found"
        )

    # Check ticket availability
    if event.available_tickets < 1:
        raise HTTPException(status_code=400, detail="No available tickets.")

    # Create the ticket
    new_ticket = Ticket(**ticket.model_dump())
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    # Update the event ticket availability
    event.available_tickets -= 1
    db.commit()

    return new_ticket


# Get ticket by id
@app.get("/tickets/{ticket_id}", response_model=None)
async def get_ticket(ticket_id: int, db: Session=Depends(get_db)) -> Ticket:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

def main():
    uvicorn.run(app, host="0.0.0.0", port=8001)


if __name__ == "__main__":
    main()
