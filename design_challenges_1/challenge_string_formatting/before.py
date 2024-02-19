from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int


def main():
    # Create a shopping cart
    items = [
        Item("Apple", Decimal("1.50"), 10),
        Item("Banana", Decimal("2.00"), 2),
        Item("Pizza", Decimal("11.90"), 5),
    ]

    total = sum(item.price * item.quantity for item in items)

    # Print the cart
    print("Shopping Cart:")
    headers: list[str] = ["Item", "Price", "Qty", "Total"]
    for header in headers:
        print(f'{header:<10}', end='')
    print()
    for item in items:
        total_price = item.price * item.quantity
        print(f'{item.name:<7} $ {item.price:>5.2f} {item.quantity:>7}     $ {total_price:>6.2f}')
    print("=" * 40)
    print(f"Total:  $ {total:>5.2f}")


if __name__ == "__main__":
    main()
