PLAY_GAME = True

MEASURE_TIME = True


PLAY_GAME_PARAMETERS = [
    dimension := 3,
    player_max := True,
    player_min := False
]

MEASURE_TIME_PARAMETERS = [
    dimension := 3,
    board := [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ],
    who_starts := 1,
    measures_number := 10
]