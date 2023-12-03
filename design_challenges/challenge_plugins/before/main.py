from dataclasses import dataclass, field
from decimal import Decimal
import json

from payment_mathods import process_payment_cc, process_payment_paypal, process_payment_apple_pay
from factory import PAYMENT_HANDLERS
from loader import load_plugin
from factory import register_payment_handler

register_payment_handler('cc', process_payment_cc)
register_payment_handler('paypal', process_payment_paypal)
register_payment_handler('apple', process_payment_apple_pay)

with open('./plugins_to_load.json') as file:
    plugins_json = json.load(file)
    plugins_list = plugins_json['plugins']

for plugin_name in plugins_list:
    plugin_module = load_plugin(plugin_name)
    plugin_method = getattr(plugin_module, plugin_name)
    register_payment_handler(plugin_name, plugin_method)

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
    amount: Decimal
    percentage: Decimal


DISCOUNTS = {
    "SAVE10": Discount(amount=Decimal("0"), percentage=Decimal("0.1")),
    "5BUCKSOFF": Discount(amount=Decimal("5.00"), percentage=Decimal("0")),
    "FREESHIPPING": Discount(amount=Decimal("2.00"), percentage=Decimal("0")),
    "BLKFRIDAY": Discount(amount=Decimal("0"), percentage=Decimal("0.2")),
}


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discounts: list[str] = field(default_factory=list)

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        found_item = self.find_item(item_name)
        if not found_item:
            print(f"Item '{item_name}' not in shopping cart, can't remove it!")
        else:
            self.items.remove(found_item)

    def find_item(self, item_name: str) -> Item | None:
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    @property
    def subtotal(self) -> Decimal:
        return Decimal(sum(item.subtotal for item in self.items))

    @property
    def total(self) -> Decimal:
        return self.subtotal - self.discount

    def apply_discount(self, code: str) -> None:
        if not code in DISCOUNTS:
            print(f"Discount code '{code}' is not valid!")
            return
        self.discounts.append(code)

    def remove_discount(self, code: str) -> None:
        self.discounts.remove(code)

    @property
    def discount(self) -> Decimal:
        total_discount = Decimal("0")
        for code in self.discounts:
            if code in DISCOUNTS:
                total_discount += DISCOUNTS[code].amount + (
                    DISCOUNTS[code].percentage * self.subtotal
                )
        return total_discount

    def print_cart(self) -> None:
        print("Shopping Cart:")
        print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
        for item in self.items:
            print(
                f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}"
            )
        print("=" * 40)
        print(f"Subtotal: ${self.subtotal:>7.2f}")
        print(f"Discount: ${self.discount:>7.2f}")
        print(f"Total:    ${self.total:>7.2f}")


def handle_payment(total: Decimal) -> None:
    payment_type = input(
        f"What payment method would you like to use? {'/'.join(PAYMENT_HANDLERS.keys())} "
    )

    if payment_type in PAYMENT_HANDLERS:
        # Process the payment
        PAYMENT_HANDLERS[payment_type](total)
    else:
        print(f"Payment type '{payment_type}' is not valid!")


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.50"), 10),
            Item("Banana", Decimal("2.00"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
    )
    cart.apply_discount("SAVE10")

    # Print the total
    cart.print_cart()

    handle_payment(cart.total)


if __name__ == "__main__":
    main()
