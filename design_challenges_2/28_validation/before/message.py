from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Callable


class MessageType(StrEnum):
    TICKET_BOOKED = auto()
    EVENT_CREATED = auto()


@dataclass
class Message:
    type: MessageType
    message: str = ""
    data: object | None = None


MessageHandlerFn = Callable[[Message], None]


@dataclass
class MessageSystem:
    handlers: dict[MessageType, list[MessageHandlerFn]] = field(default_factory=dict)

    def attach(self, msg_type: MessageType, handler: MessageHandlerFn):
        if msg_type not in self.handlers:
            self.handlers[msg_type] = []
        self.handlers[msg_type].append(handler)

    def detach(self, msg_type: MessageType, handler: MessageHandlerFn):
        if msg_type not in self.handlers:
            return
        self.handlers[msg_type].remove(handler)

    def post(self, event: Message):
        if event.type not in self.handlers:
            return
        for handler in self.handlers[event.type]:
            handler(event)
