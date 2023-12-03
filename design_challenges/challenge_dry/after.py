from decimal import Decimal
from dataclasses import dataclass
from enum import Enum
from typing import Iterable


EMAIL_SENDER = "sales@webshop.com"


class OrderType(Enum):
    ONLINE = "online"
    IN_STORE = "in store"


@dataclass
class Item:
    name: str
    price: Decimal


@dataclass
class Order:
    id: int
    type: OrderType
    customer_email: str


@dataclass
class Email:
    body: str
    subject: str
    recipient: str
    sender: str


def calculate_total_price(items: Iterable[Item], discount: Decimal | None = None) -> Decimal:
    total_price = Decimal(sum(item.price for item in items))
    if discount is not None:
        discount = total_price - (total_price * discount)
    return total_price


def generate_order_confirmation_email(order: Order) -> Email:
    return Email(
        body=f"Thank you for your order! Your order #{order.id} has been confirmed.",
        subject="Order Confirmation",
        recipient=order.customer_email,
        sender=EMAIL_SENDER
    )


def generate_order_shipping_notification(order: Order) -> Email:
    return Email(
        body=f"Good news! Your order #{order.id} has been shipped and is on its way.",
        subject="Order Shipped",
        recipient=order.customer_email,
        sender=EMAIL_SENDER
    )

def process_order(order: Order) -> None:
    print(f"Processing {order.type.value} order...")
    print(generate_order_confirmation_email(order))
    
    if order.type == OrderType.ONLINE:
        print("Shipping the order...")
        print(generate_order_shipping_notification(order))
    else:
        print("Order ready for pickup.")

    print("Order processed successfully.")


def main() -> None:
    items = [
        Item(name="T-Shirt", price=Decimal("19.99")),
        Item(name="Jeans", price=Decimal("49.99")),
        Item(name="Shoes", price=Decimal("79.99")),
    ]

    online_order = Order(
        id=123, type=OrderType.ONLINE, customer_email="sarah@gmail.com"
    )

    total_price = calculate_total_price(items)
    print("Total price:", total_price)

    discounted_price = calculate_total_price(items, Decimal("0.1"))
    print("Discounted price:", discounted_price)

    process_order(online_order)

    in_store_order = Order(
        id=456, type=OrderType.IN_STORE, customer_email="john@gmail.com"
    )

    process_order(in_store_order)


if __name__ == "__main__":
    main()
