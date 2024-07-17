from datetime import datetime
import re

from pydantic import BaseModel, ValidationError, Field, field_validator, model_validator


class EventCreate(BaseModel):

    @model_validator(mode='after')
    def start_before_end(self):
        if self.end_date <= self.start_date:
            raise ValidationError("Start date must be before the end date.")
        return self

    title: str
    location: str
    start_date: datetime
    end_date: datetime
    available_tickets: int = Field(gt=0)


class TicketCreate(BaseModel):
    @field_validator('customer_email')
    @classmethod
    def validate_email(cls, customer_email: str):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if not re.match(regex, customer_email):
            raise ValidationError(f"Incorrect e-mail format: {customer_email}")
        return customer_email

    event_id: int
    customer_name: str
    customer_email: str


class TicketUpdate(BaseModel):
    customer_name: str | None = None
