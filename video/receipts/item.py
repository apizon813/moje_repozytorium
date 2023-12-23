from typing import List
from .price import Price
import random

BARCODE_LENGTH = 13


class Item:
    def __init__(self, name, price: Price, barcode: str = "1234567890123"):
        # HINT barcode must be valid and have 13 digits
        if not name:
            raise ValueError('Name cannot be empty')
        self._name = name
        
    
        self._price = price
        
        
        if len(barcode) != 13 or not barcode.isnumeric():
            raise ValueError('Invalid barcode')
        self._barcode = barcode

        

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def barcode(self):
        return self._barcode
        

    def __str__(self) -> str:
        return f'{self._name} price is {self._price}, barcode is {self._barcode}'
        

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name}, price={self._price}, barcode={self._barcode})"


# def random_item() -> Item:
#     """Generate a random item"""
#     names = {
#         1: 'Milk'


#     }
#     prices = {
#         1: 100
#     }
    



# def generate_items(num_items: int) -> List[Item]:
#     """Generates a given number of random items"""




