PLAY_GAME = True

MEASURE_STARTING_MOVES = False

MEASURE_MIDDLE_GAME = False

MEASURE_PROGRESS = False


PLAY_GAME_PARAMETERS = [
    dimension := 3,
    player_max := False,
    player_min := False
]

MEASURE_STARTING_MOVES_PARAMETERS = [
    dimension := 3,
    measures_number := 10,
    save_data_path := './results/starting_moves.txt',
]

MEASURE_MIDDLE_GAME_PARAMETERS = [
    dimension := 3,
    measure_number := 10,
    save_data_path := './results/middle_game.txt',
    state1 := {
        'board': [
            ['o', '2', '3'],
            ['x', 'o', '6'],
            ['7', '8', '9']
        ],
        'who_moves': 0,
        'move': '9'
    },
    state2 := {
        'board': [
            ['o', '2', '3'],
            ['4', 'o', '6'],
            ['x', '8', 'x']
        ],
        'who_moves': 1,
        'move': '6'
    },
    state3 := {
        'board': [
            ['1', '2', '3'],
            ['4', 'x', '6'],
            ['o', 'o', '9']
        ],
        'who_moves': 0,
        'move': '9'
    }
]

MEASURE_PROGRESS_PARAMETERS = [
    dimension := 3,
    save_plot_path := './plots/progress_plot.png',
    measure_number := 10,
    save_times_path := './results/progress_times.txt'
]
