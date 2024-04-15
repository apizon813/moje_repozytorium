from game import TicTacToe
from players import (
    Player,
    Oponent
    )


def main():

    game = TicTacToe(
        dimension=3,
        player_max=Oponent(),
        player_min=Player()
        )

    # game.board = [
    #     ['1', '2', '3'],
    #     ['4', 'o', '6'],
    #     ['x', '8', '9']
    # ]
    game.print_board()

    while not game.finished:
        game.ask_for_move()
        game.print_board()
    game.print_winner()


if __name__ == "__main__":
    main()

# dodać metodę cofającą ruch zamiast kopiowania całego obiektu
