from datetime import date
from typing import List, Optional
from random import randint

from .item import Item
from .receipt_position import ReceiptPosition
from .price import Price


class Receipt:
    def __init__(self, positions: Optional[List[ReceiptPosition]] = None):
        # set date attribute and set it to today
        # https://docs.python.org/3/library/datetime.html
        self._positions = positions or []
        self._date = date.today()

    @property
    def date(self):
        return self._date

    @property
    def positions(self):
        return self._positions

    @property
    def total_price(self) -> Price:
        # HINT try to use sum() built-in function here
        # HINT you can also use a list comprehension
        prices: [Price] = []
        for position in self.positions:
            prices.append(position.total_price.value_gr)
        # prices = [position.total_price for position in self.positions]
        return Price(sum(prices))

    def __iter__(self):
        # HINT this will allow you to write `for position in receipt:`
        # HINT you simply want to return the iterator over `positions`
        return iter(self._positions)

    def __len__(self):
        # HINT this will allow you to write `len(receipt)`
        # HINT the length of the receipt is the number of positions
        return len(self._positions)

    def top_expensive_positions(self, num_positions=1) -> list:
        '''
        zwraca :num_positions: najdroższych pozycji na paragonie
        '''
        if num_positions < 1:
            raise ValueError()
        # HINT try sorting positions by their total price
        # HINT https://docs.python.org/3/howto/sorting.html
        top_pricey = sorted(
            self._positions, key=lambda position: position.total_price, reverse=True
        )
        return top_pricey[:num_positions]

    def add_position(self, amount: float, item: Item):
        position = ReceiptPosition(amount, item)
        self._positions.append(position)

    def __repr__(self):
        # positions = self._positions or None
        return f"{self.__class__.__name__}(positions={self._positions})"

    def __str__(self) -> str:
        # FIXME this is hacky but simple and not super important
        result = f"{self.date.strftime('%a, %d.%m.%Y, %H:%M:%S')}\n"
        separator = "-" * 50 + "\n"
        result += separator
        for position in self.positions:
            result += str(position)
        result += separator
        total_price = f"TOTAL: {str(self.total_price)}"
        result += f"{total_price:>{len(separator) - 1}}\n"
        return result


def random_receipt() -> Receipt:
    """Generates a random receipt"""
    max_amount = 20
    max_price = 1000
    max_positions = 10

    receipt = Receipt()
    num_positions = randint(1, max_positions)
    for i in range(num_positions):
        amount = randint(1, max_amount)
        price = randint(1, max_price)
        name = f"item #{i}"
        item = Item(name, price)
        receipt.add_position(amount, item)

    return receipt


def generate_receipts(num_receipts: int) -> List[Receipt]:
    """Generates a given number of fake receipts"""
    receipts = []
    for i in range(num_receipts):
        receipts.append(random_receipt())
