# Zaprojektuj i wykonaj klasy reprezentujące przedmiot o masie podanej w
# kilogramach oraz pojemnik (który sam jest przedmiotem) o podanym udźwigu.
# Przedmioty można wkładać i wyjmować z pojemników, o ile są one w ramach
# dopuszczalnego udźwigu (w przeciwnym razie nie udaje się włożyć przedmiotu do
# pojemnika). Program ma umożliwić wypisanie zawartości każdego pojemnika w
# postaci zestawu mas przedmiotów, które się w nim znajdują.

class Item:
    def __init__(self, name, mass):
        self._name = name
        self._mass = mass

    @property
    def name(self):
        return self._name

    @property
    def mass(self):
        return self._mass

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, mass={self.mass})'

    def __eq__(self, other):
        return self.name == other.name and self.mass == other.mass


class Box(Item):
    def __init__(self, name, mass, lift):
        super().__init__(name, mass)
        self._max_lift = lift
        self._current_lift = lift
        self._contains = []

    @property
    def lift(self):
        return self._max_lift

    @property
    def current_lift(self):
        return self._current_lift

    @property
    def contains(self):
        return self._contains

    def insert(self, item):
        self._contains.append(item)
        self._current_lift -= item.mass

    def remove(self, item):
        if item not in self.contains:
            print('yea')
        self._contains.remove(item)
        self._current_lift += item.mass
