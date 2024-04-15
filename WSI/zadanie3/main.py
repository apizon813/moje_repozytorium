from parameters import PLAY_GAME


def main():
    if PLAY_GAME:
        from parameters import PLAY_GAME_PARAMETERS
        from experiments import play_game
        play_game(PLAY_GAME_PARAMETERS)


if __name__ == "__main__":
    main()

# dodać agregat głębokości
