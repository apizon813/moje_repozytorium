class Planet():
    def __init__(self, x, y, z, name=''):
        self._coords = (x, y, z)
        self._moons = 0
        self._name = name

    def __str__(self):
        return f'This planet is called {self._name}.'

    def coords(self):
        return self._coords

    def set_coords(self, new_coords):
        self._coords = new_coords

    def moons(self):
        return self._moons

    def set_moons(self, moons):
        self._moons = moons

    def name(self):
        return self._name

    def new_name(self, new_name):
        self._name = new_name
