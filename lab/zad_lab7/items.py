# NIE WOLNO TYPE NIEWOLNOOO!!!!!!!!!! ZERO ZE WSZYSTKIEGO
# klasa Item
# atrybuty: masa, nazwa
# klasa Container
# atrybuty: masa, nazwa, udźwig, przechowywane przedmioty w formie słownika
# metody: wsadzić przedmiot, wyciągnąć przedmiot,
# wypisanie listy przedmiotów lista mas
class AboveLiftError(Exception):
    def __init__(self, item):
        super().__init__('Mass above max lift!')
        self.item = item


class Item:
    def __init__(self, name: str, mass: float):
        if mass <= 0:
            raise ValueError('Mass must be positive.')
        if not name:
            name = 'Mass'
        self._name = name
        self._mass = mass

    @property
    def name(self) -> str:
        return self._name

    @property
    def mass(self) -> float:
        return self._mass

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, mass={self.mass})"

    def __eq__(self, other: object) -> bool:
        return self.name == other.name and self.mass and other.mass


class Container(Item):
    def __init__(self, name: str, mass: float, lift: float):
        if lift <= 0:
            raise ValueError('Lift must be positive.')
        if not name:
            name = 'Box'
        super().__init__(name, mass)
        self._max_lift = lift
        self._lift_left = lift
        self._contains = []

    @property
    def max_lift(self) -> float:
        return self._max_lift

    @property
    def current_lift(self) -> float:
        return self._lift_left

    @property
    def contains(self) -> list:
        return self._contains

    def insert(self, item):
        if item.mass > self._lift_left:
            raise AboveLiftError(item)
        self._lift_left -= item.mass
        self._contains.append(item)

    def remove(self, item):
        if item not in self._contains:
            raise ValueError
        self._lift_left += item.mass
        self._contains.remove(item)

    @property
    def info(self):
        return [item.mass for item in self._contains]
