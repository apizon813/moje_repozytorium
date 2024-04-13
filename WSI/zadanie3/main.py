import numpy as np


class Player():
    def move(self, board):
        move_type = int(input('> '))
        return move_type


class Oponent():
    def move():
        pass


class TicTacToe():
    def __init__(self, dimension: int, players, who_starts: str):
        # who_starts = '0' - player starts
        # who_starts = '1' - oponent starts

        self.signs = ('o', 'x')
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

    def print_board(self):
        for i in range(self.dimension):
            fields = []
            for j in range(self.dimension):
                fields.append(str(self.board[i][j]))
            row = '|' + '|'.join(fields) + '|'
            print(row)

    def move(self):
        player = self.players[self.who_moves]
        sign = self.signs[self.who_moves]
        move_type = player.move(self.board)
        self.board[self.board == move_type] = sign
        self.who_moves = not self.who_moves

    def finished(self):
        pass


def main():
    players = (Player(), Oponent())
    starting_player = int(input('Who starts? [0/1]\n'))
    game = TicTacToe(
        dimension=3,
        players=players,
        who_starts=starting_player,
        )
    game.print_board()

    while not game.finished():
        game.move()
        game.print_board()
    pass


if __name__ == "__main__":
    main()
