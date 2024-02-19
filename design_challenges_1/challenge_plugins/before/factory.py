from typing import Callable
from decimal import Decimal

PaymentHandlerFn = Callable[[Decimal], None]

PAYMENT_HANDLERS: dict[str, PaymentHandlerFn] = {}

def register_payment_handler(handler_name: str, payment_handler: PaymentHandlerFn) -> None:
    print(f'Registering {handler_name}')
    PAYMENT_HANDLERS[handler_name] = payment_handler