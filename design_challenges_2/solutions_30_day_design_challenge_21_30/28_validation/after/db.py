from datetime import datetime
from pydantic import BaseModel, validator
import re


class EventCreate(BaseModel):
    title: str
    location: str
    start_date: datetime
    end_date: datetime
    available_tickets: int

    @validator("available_tickets")
    def validate_available_tickets(cls, value: int):
        if value < 0:
            raise ValueError("available_tickets must be a positive integer")
        return value

    @validator("end_date")
    def validate_end_date(cls, value: datetime, values: dict[str, datetime]):
        if "start_date" in values and value <= values["start_date"]:
            raise ValueError("end_date must be after start_date")
        return value


class TicketCreate(BaseModel):
    event_id: int
    customer_name: str
    customer_email: str

    @validator("customer_email")
    def validate_customer_email(cls, value: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("invalid email address")
        return value


class TicketUpdate(BaseModel):
    customer_name: str | None = None
