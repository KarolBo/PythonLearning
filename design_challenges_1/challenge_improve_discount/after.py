from dataclasses import dataclass, field
from decimal import Decimal


class ItemNotFoundException(Exception):
    pass


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    @property
    def subtotal(self) -> Decimal:
        return self.price * self.quantity

@dataclass  
class Discount:
    amount: Decimal = field(default=Decimal('0'))
    percentage: Decimal = field(default=Decimal('0'))


DISCOUNTS = {
    "SAVE10": Discount(percentage=Decimal('0.1')),
    "5BUCKSOFF": Discount(amount=Decimal('5.00')),
    "FREESHIPPING": Discount(percentage=Decimal('2.00')),
    "BLKFRIDAY": Discount(percentage=Decimal('0.2'))
}


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discounts: list[Discount] = field(default_factory=list)

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        found_item = self.find_item(item_name)
        self.items.remove(found_item)

    def find_item(self, item_name: str) -> Item:
        for item in self.items:
            if item.name == item_name:
                return item
        raise ItemNotFoundException(f"Item '{item_name}' not found.")
    
    def add_discount(self, code: str) -> None:
        if code in DISCOUNTS:
            self.discounts.append(DISCOUNTS[code])

    @property
    def subtotal(self) -> Decimal:
        return Decimal(sum(item.subtotal for item in self.items))
    
    @property
    def discount(self) -> Decimal:
        subtotal = self.subtotal
        return Decimal(
            sum([dsc.amount + dsc.percentage * subtotal 
                    for dsc in self.discounts]
            ))
    
    @property
    def total(self) -> Decimal:
        return self.subtotal - self.discount
    
    def __str__(self) -> str:
        s = "Shopping Cart:\n"
        s += f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}"
        for item in self.items:
            s += f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}\n"
        s += "=" * 40 + '\n'
        s += f"Subtotal: ${self.subtotal:>7.2f}\n"
        s += f"Discount: ${self.discount:>7.2f}\n"
        s += f"Total:    ${self.total:>7.2f}\n"

        return s


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.50"), 10),
            Item("Banana", Decimal("2.00"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ]
    )
    cart.add_discount("SAVE10")
    print(cart)


if __name__ == "__main__":
    main()
