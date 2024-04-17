from parameters import (
    PLAY_GAME,
    MEASURE_STARTING_MOVES,
    MEASURE_DEPTH
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

    if MEASURE_DEPTH:
        from parameters import MEASURE_DEPTH_PARAMETERS
        from experiments import measure_depth
        measure_depth(MEASURE_DEPTH_PARAMETERS)


if __name__ == "__main__":
    main()
