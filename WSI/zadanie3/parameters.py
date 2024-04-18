PLAY_GAME = False

MEASURE_STARTING_MOVES = False

MEASURE_PROGRESS = True


PLAY_GAME_PARAMETERS = [
    dimension := 3,
    player_max := True,
    player_min := False
]

MEASURE_STARTING_MOVES_PARAMETERS = [
    dimension := 3,
    measures_number := 2,
    save_data_path := './results/measured_time.txt',
]

MEASURE_PROGRESS_PARAMETERS = [
    dimension := 3,
    save_plot_path := './plots/time_plot.png',
    measure_number := 10,
    save_times_path := './results/progress_times.txt'
]
