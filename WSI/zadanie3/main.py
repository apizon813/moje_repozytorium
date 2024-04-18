from parameters import (
    PLAY_GAME,
    MEASURE_STARTING_MOVES,
    MEASURE_PROGRESS,
    MEASURE_MIDDLE_GAME
)


def main():
    if PLAY_GAME:
        from parameters import PLAY_GAME_PARAMETERS
        from experiments import play_game
        play_game(PLAY_GAME_PARAMETERS)

    if MEASURE_STARTING_MOVES:
        from parameters import MEASURE_STARTING_MOVES_PARAMETERS
        from experiments import measure_starting_moves
        measure_starting_moves(MEASURE_STARTING_MOVES_PARAMETERS)

    if MEASURE_MIDDLE_GAME:
        from parameters import MEASURE_MIDDLE_GAME_PARAMETERS
        from experiments import measure_middle_game
        measure_middle_game(MEASURE_MIDDLE_GAME_PARAMETERS)

    if MEASURE_PROGRESS:
        from parameters import MEASURE_PROGRESS_PARAMETERS
        from experiments import measure_progress
        measure_progress(MEASURE_PROGRESS_PARAMETERS)


if __name__ == "__main__":
    main()
