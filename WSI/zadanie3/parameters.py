PLAY_GAME = False

MEASURE_STARTING_MOVES = True

MEASURE_PROGRESS = False


PLAY_GAME_PARAMETERS = [
    dimension := 3,
    player_max := True,
    player_min := False
]

MEASURE_STARTING_MOVES_PARAMETERS = [
    dimension := 3,
    measures_number := 2,
    save_data_path := './measured_time.txt',
]

MEASURE_PROGRESS_PARAMETERS = [
    dimension := 3,
    save_plot_path := './time_plot.png',
    measure_number := 2
]
