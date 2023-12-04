from planet import Planet
from math import sqrt
COORDINATES = [(3, 0, 0), (0, 4, 0)]

def distance(planet1, planet2):
    x1, y1, z1 = planet1.coords()
    x2, y2, z2 = planet2.coords()
    x = x2 - x1
    y = y2 - y1
    z = z2 - z1
    distance = sqrt(x ** 2 + y ** 2 + z ** 2)
    return distance

if __name__ == "__main__":
    x, y, z = COORDINATES[0]
    planet1 = Planet(x, y, z, "Mars")
    x, y, z = COORDINATES[1]
    planet2 = Planet(x, y, z, "Earth")
    print(distance(planet1, planet2))
