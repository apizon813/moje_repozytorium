import numpy as np


class Oponent():
    pass


class TicTacToe():
    def __init__(self, dimension: int):
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


def main():
    game = TicTacToe(3)
    game
    pass
