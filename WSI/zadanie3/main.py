import numpy as np


class Oponent():
    pass


class TicTacToe():
    def __init__(self, dimension: int, who_starts: str):
        # who_starts = 'p' - player starts
        # who_starts = 'o' - oponent starts
        self.dimension = dimension
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

    def move():
        pass

    def finished():
        pass


def main():
    who_starts = input('Who starts? [p/o]\n')
    game = TicTacToe(3, who_starts)
    while not game.finished():
        game.move()
    pass


if __name__ == "__main__":
    main()
