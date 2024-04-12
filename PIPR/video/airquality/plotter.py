import airquality
import sys
from random import choice
from matplotlib import pyplot as plt
import argparse


def find_station(id):
    for station in airquality.get_stations():
        if station.id() == id:
            return station


def list_stations(args):
    pattern = args.list_stations
    all_stations = airquality.get_stations()
    for station in all_stations:
        if pattern == ' ' or pattern in station.name():
            print(f'{station.id()}\t{station}')


def list_sensors(args):
    station_id = float(args.list_sensors)
    station = find_station(station_id)
    if station:
        for sensor in station.sensors():
            print(f'{sensor.id()}\t{sensor.name()}')


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('--list-stations', nargs='?', const=' ')
    parser.add_argument('--list-sensors')

    args = parser.parse_args(arguments[1:])

    if args.list_stations:
        list_stations(args)
        return

    if args.list_sensors is not None:
        list_sensors(args)
        return

    all_stations = [
        station
        for station in airquality.get_stations()
        if station.city_name() == 'Warszawa'
    ]
    station = choice(all_stations)
    all_sensors = station.sensors()
    for sensor in all_sensors:
        if sensor.code() == 'CO':
            continue
        readings = sensor.readings()
        keys = [
            reading.date
            for reading in readings
        ]
        values = [reading.value for reading in readings]
        plt.plot(keys, values, label=sensor.code())
    plt.legend()
    plt.title(label=station.name())
    plt.xticks(rotation=30, fontsize='xx-small', horizontalalignment='right')
    plt.savefig(f'{station}.png')
    plt.show()


if __name__ == '__main__':
    main(sys.argv)
