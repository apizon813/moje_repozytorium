from typing import Tuple, List


class Price:
    def __init__(self, value_gr=0):
        if int(value_gr) < 0:
            raise ValueError
        self._value_gr = int(value_gr)
        
    @property
    def value_gr(self):
        return self._value_gr

    def __add__(self, other: "Price") -> "Price":
        return Price(self.value_gr + other.value_gr)

    def __sub__(self, other: "Price") -> "Price":
        return Price(self.value_gr - other.value_gr)

    def __mul__(self, multiplier: float) -> "Price":
        return Price(self.value_gr * multiplier)

    def __rmul__(self, multiplier: float) -> "Price":
        return Price(self.value_gr * multiplier)

    def __lt__(self, other: "Price"):
        # HINT this should allow sorting Prices by value_gr
        return self.value_gr < other.value_gr

    @classmethod
    def from_float(cls, value=0) -> "Price":
        # HINT this will be called `p = Price.from_float(1.25)`
        # HINT we expect it to work like `p = Price(125)`
        # HINT notice cls instead of self!
        # HINT `cls(125)` will be `Price(125)` in this case!
        # HINT try using the round() built-in function
        return cls(round(float(value) * 100, ndigits=2))

    def _split_price(self) -> Tuple[int, int]:
        price_zl = self.value_gr // 100
        price_gr = self.value_gr % 100
        return price_zl, price_gr

    def __str__(self) -> str:
        return str(self.value_gr)

    def __repr__(self) -> str:
        # repr is a raw description of the instance
        # usually you implement it like this:
        return f"{self.__class__.__name__}(value_gr={self.value_gr})"

    def _format_price(self) -> str:
        # HINT zl, gr = self._split_price()
        price_zl, price_gr = self._split_price()
        return f'{price_zl}.{price_gr:02}'

    def __eq__(self, other) -> bool:
        return self.value_gr == other.value_gr


def random_price() -> Price:
    """Generates a random Price object"""


def generate_prices(num_prices: int) -> List[Price]:
    """Generates a given number of random items"""
