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
    
    def name(self):
        return self._name
    
    def mass(self):
        return self._mass
