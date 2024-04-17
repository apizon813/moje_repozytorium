PLAY_GAME = False

MEASURE_TIME = True

MEASURE_DEPTH = False


PLAY_GAME_PARAMETERS = [
    dimension := 3,
    player_max := False,
    player_min := False
]

MEASURE_TIME_PARAMETERS = [
    dimension := 3,
    board := [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ],
    move := '5',
    who_starts := 1,
    measures_number := 10,
    save_data_path := './measured_time.txt',
    pruning := True
]

MEASURE_DEPTH_PARAMETERS = [
    dimension := 3,
    board := [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ],
    move := '5',
    who_starts := 1,
    save_data_path := './measured_depth.txt',
    pruning := True
]
