from .item import Item
from .price import Price
from typing import List


class ReceiptPosition:
    def __init__(self, amount: float, item: Item):
        if amount <= 0:
            raise ValueError
        self._amount = amount

        self._item = item

    @property
    def item(self) -> Item:
        return self._item

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def total_price(self) -> Price:
        price = self.amount * self.item.price
        return price

    def __lt__(self, other: "ReceiptPosition"):
        return self.total_price < other.total_price

    def __str__(self) -> str:
        return self._format_position()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(amount={self._amount},"\
            " item={repr(self._item)})"

    def _format_position(self):
        # FIXME this is hacky but simple and not super important
        result = (
            f"{self.item.name:<20}"
            f"{self.amount:<5} * {str(self.item.price):<9} | "
            f"{str(self.total_price):>10}"
        )
        result += "\n"
        return result


def random_position() -> ReceiptPosition:
    """Generates a random receipt position"""


def generate_positions(num_positions: int) -> List[ReceiptPosition]:
    """Generates a given number of random fake receipt positions"""
