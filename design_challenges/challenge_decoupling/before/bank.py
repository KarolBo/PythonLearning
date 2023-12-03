from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol


class BankAccount(Protocol):
    account_number: str
    balance: Decimal

    def deposit(self, amount: Decimal) -> None:
        ...

    def withdraw(self, amount: Decimal) -> None:
        ...


class PaymentService(Protocol):
    def process_payment(self, amount: Decimal) -> None:
        ...

    def process_payout(self, amount: Decimal) -> None:
        ...


@dataclass
class SavingsAccount:
    account_number: str
    balance: Decimal

    def deposit(self, amount: Decimal) -> None:
        print(f"Depositing {amount} into Savings Account {self.account_number}.")

    def withdraw(self, amount: Decimal) -> None:
        print(f"Withdrawing {amount} from Savings Account {self.account_number}.")


@dataclass
class CheckingAccount:
    account_number: str
    balance: Decimal

    def deposit(self, amount: Decimal) -> None:
        print(f"Depositing {amount} into Checking Account {self.account_number}.")

    def withdraw(self, amount: Decimal) -> None:
        print(f"Withdrawing {amount} from Checking Account {self.account_number}.")


class BankService:
    def __init__(self, payment_service: PaymentService):
        self._payment_service = payment_service

    def deposit(self, amount: Decimal, account: BankAccount) -> None:
        account.deposit(amount)
        self._payment_service.process_payment(amount)
        account.balance += amount

    def withdraw(self, amount: Decimal, account: BankAccount) -> None:
        account.withdraw(amount)
        self._payment_service.process_payout(amount)
        account.balance -= amount
