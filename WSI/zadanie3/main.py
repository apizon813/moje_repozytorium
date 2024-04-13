class Player():
    def move(self, board: list) -> str:
        move_type = input('> ')
        return move_type


class Oponent():
    def move(self, board):
        pass


class TicTacToe():
    def __init__(self, dimension: int, player1, player2):
        # who_starts = '0' - player starts
        # who_starts = '1' - oponent starts

        self.signs = ('o', 'x')
        self.dimension = dimension
        self.players = (player1, player2)
        self.who_moves = 0
        self.board = self.create_board(dimension)
        self.finished = False

    def create_board(self, dimension: int):
        num = 1
        table = []
        for i in range(dimension):
            row = []
            for j in range(dimension):
                row.append(str(num))
                num += 1
            table.append(row)
        print(table)
        return table

    def print_board(self):
        for i in range(self.dimension):
            fields = []
            for j in range(self.dimension):
                fields.append(self.board[i][j])
            row = '|' + '|'.join(fields) + '|'
            print(row)

    def move(self):
        player = self.players[self.who_moves]
        sign = self.signs[self.who_moves]
        move_type = player.move(self.board)

        self.change_board(move_type, sign)
        self.finished = self.is_finished(sign)
        self.who_moves = not self.who_moves

    def change_board(self, move_type, sign):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.board[i][j] == move_type:
                    self.board[i][j] = sign

    def is_finished(self, sign) -> bool:
        def is_row_line():
            for i in range(self.dimension):
                is_line = True
                for j in range(self.dimension):
                    if self.board[i][j] != sign:
                        is_line = False
                if is_line:
                    return True

        def is_col_line():
            for i in range(self.dimension):
                is_line = True
                for j in range(self.dimension):
                    if self.board[j][i] != sign:
                        is_line = False
                if is_line:
                    return True

        def is_diag_line():
            is_line = True
            for i in range(self.dimension):
                if self.board[i][i] != sign:
                    is_line = False
            if is_line:
                return True

            is_line = True
            for i in range(self.dimension):

                if self.board[i][-i-1] != sign:
                    is_line = False
            if is_line:
                return True
        
        return is_row_line() or is_col_line() or is_diag_line()


def main():
    game = TicTacToe(
        dimension=3,
        player1=Player(),
        player2=Oponent()
        )
    game.print_board()

    while not game.finished:
        game.move()
        game.print_board()
    print('u won')


if __name__ == "__main__":
    main()
