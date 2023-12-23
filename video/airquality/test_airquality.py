import airquality


def test_1():
    all_stations = airquality.get_stations()
    station = all_stations[0]
    assert str(station) == 'Wrocław, ul. Bartnicza'
