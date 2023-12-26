from typing import List
from .price import Price
from .receipt import Receipt


class Client:
    def __init__(self, name, user_id, receipts: List[Receipt] = None):
        if len(name) == 0:
            raise ValueError()
        if len(str(user_id)) == 0:
            raise ValueError()
        self._name = str(name)
        self._user_id = str(user_id)
        self._receipts = receipts

    @property
    def name(self):
        return str(self._name)

    @property
    def user_id(self):
        return str(self._user_id)

    @property
    def receipts(self):
        return self._receipts

    def add_receipt(self, receipt: Receipt):
        if self.receipts is None:
            self._receipts = []
        if isinstance(receipt, Receipt):
            self.receipts.append(receipt)
        else:
            raise TypeError('it\'s not a receipt')

    @property
    def total_spending(self):
        total_spend = 0
        for receipt in self.receipts:
            # price in gr
            total_spend += receipt.total_price.value_gr

        return Price(total_spend)

    def __str__(self):
        return f'Client {self.name} has id: {self.user_id}.'

    def __repr__(self):
        receipts = ')' if not self.receipts else f', {self.receipts})'
        return f'Client({self.name}, {self.user_id}{receipts}'


def random_client() -> Client:
    """Generates a random user"""


def generate_clients(
    num_clients: int, with_receipts=False, num_receipts=10
) -> List[Client]:
    """Generates a given number of fake clients with optional fake receipts"""
