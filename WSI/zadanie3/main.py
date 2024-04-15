from parameters import (
    PLAY_GAME,
    MEASURE_TIME
)


def main():
    if PLAY_GAME:
        from parameters import PLAY_GAME_PARAMETERS
        from experiments import play_game
        play_game(PLAY_GAME_PARAMETERS)

    if MEASURE_TIME:
        from parameters import MEASURE_TIME_PARAMETERS
        from experiments import measure_time
        measure_time(MEASURE_TIME_PARAMETERS)


if __name__ == "__main__":
    main()

# dodać agregat głębokości
