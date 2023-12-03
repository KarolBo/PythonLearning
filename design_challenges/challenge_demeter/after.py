from dataclasses import dataclass, field
from decimal import Decimal

class ItemNotFoundException(Exception):
    pass


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    def set_price(self, new_price: Decimal):
        self.price = new_price

    def set_quantity(self, new_quantity: int):
        self.quantity = new_quantity

    @property
    def total_price(self):
        return self.price * self.quantity


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discount_code: str | None = None

    def find_item(self, item_name: str) -> tuple[Item | None, int]:
        for i, item in enumerate(self.items):
            if item.name == item_name:
                return item, i
        return None, -1

    def set_item_quantity(self, item_name: str, quantity: int):
        assert quantity >= 0
        item, _ = self.find_item(item_name)
        if item is not None:
            item.set_quantity(quantity)
        else:
            raise ItemNotFoundException(item_name)
        
    def set_item_price(self, item_name: str, price: Decimal):
        assert price >= 0
        item, _ = self.find_item(item_name)
        if item is not None:
            item.set_price(price)
        else:
            raise ItemNotFoundException(item_name)
        
    def remove_item(self, item_name: str):
        _, item_idx = self.find_item(item_name)
        if item_idx != -1:
            del self.items[item_idx]
        else:
            raise ItemNotFoundException(item_name)
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.items)
    
    def __str__(self) -> str:
        s: str = "Shopping Cart:\n"
        s += f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}\n"
        for item in self.items:
            s += f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.total_price:>7.2f}\n"
        s += ("=" * 40) + '\n'
        s += f"Total: ${self.total_price:>7.2f}\n"
        return s


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.5"), 10),
            Item("Banana", Decimal("2"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
    )

    # Update some items' quantity and price
    cart.set_item_quantity('Apple', 10)
    cart.set_item_price('Pizza', Decimal("3.50"))

    # Remove an item
    cart.remove_item("Banana")

    # Print the cart
    print(cart)


if __name__ == "__main__":
    main()
