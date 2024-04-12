import numpy as np


class Player():
    pass

class Oponent():
    def move():
        pass


class TicTacToe():
    def __init__(self, dimension: int, players, who_starts: str):
        # who_starts = '0' - player starts
        # who_starts = '1' - oponent starts

        self.dimension = dimension
        self.players = players
        self.who_moves = who_starts
        self.board = self.create_board(dimension)

    def create_board(self, dimension: int):
        num = 1
        table = []
        for i in range(dimension):
            row = []
            for j in range(dimension):
                row.append(num)
                num += 1
            table.append(row)
        matrix = np.array(table)
        return matrix

    def print_board():
        pass

    def move(self):
        # do testu
        self.players[self.who_moves].move(self.board)
        self.who_moves = not self.who_moves

    def finished():
        pass


def main():
    players = (Player(), Oponent())
    starting_player = int(input('Who starts? [0/1]\n'))
    game = TicTacToe(
        dimension=3,
        players=players,
        who_starts=starting_player,
        )

    while not game.finished():
        game.move()
    pass


if __name__ == "__main__":
    main()
