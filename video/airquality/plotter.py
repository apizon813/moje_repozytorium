import airquality
import sys
from random import choice


def main(arguments):
    all_stations = airquality.get_stations()
    station = choice(all_stations)
    all_sensors = station.sensors()
    sensor = choice(all_sensors)
    readings = sensor.readings()
    if readings:
        print(readings[0])


if __name__ == '__name__':
    main(sys.argv)
