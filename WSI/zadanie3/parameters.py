PLAY_GAME = False

MEASURE_STARTING_MOVES = True

MEASURE_DEPTH = False


PLAY_GAME_PARAMETERS = [
    dimension := 3,
    player_max := False,
    player_min := False
]

MEASURE_STARTING_MOVES_PARAMETERS = [
    dimension := 3,
    measures_number := 2,
    save_data_path := './measured_time.txt',
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

STATE1 = [
    dimension := 3,
    board := [
        ['o', 'x', 'o'],
        ['o', 'x', '6'],
        ['x', '8', '9']
    ],
    move := '8',
    who_starts := 1,
]

STATE2 = [
    dimension := 3,
    board := [
        ['1', '2', 'o'],
        ['x', 'o', '6'],
        ['7', '8', '9']
    ],
    move := '1',
    who_starts := 0,
]

STATE3 = [
    dimension := 3,
    board := [
        ['1', '2', '3'],
        ['o', 'x', '6'],
        ['7', '8', '9']
    ],
    move := '1',
    who_starts := 1,
]

STATES = [STATE1, STATE2, STATE3]
