def minmax(board, maxim: bool, alpha, beta):
    board = board.deepcopy()
    if board.finished:
        # tu powinno być -1 0 i 1 jako możliwe wartości
        # czy winner to int?
        # żeby wybrać ekstremum musi być int
        return board.winner

    if maxim:
        max_val = -1
        for pos_move in board.possible_moves():
            val = minmax(board, pos_move, not maxim)
            max_val = max(max_val, val)

    else:
        min_val = 2
        for pos_move in board.possible_moves():
            val = minmax(board, pos_move, not maxim)
            min_val = min(min_val, val)


class Player():
    def __init__(self) -> None:
        self.max = None

    def move(self, board: list) -> str:
        move_type = input('> ')
        return move_type


class Oponent():
    def __init__(self) -> None:
        self.max = None

    def move(self, game):
        moves_vals = {}
        for move in game.possible_moves():
            board = game.deepcopy()
            board.change_board(move)
            moves_vals[move] = minmax(board, -1, 2)

        # ostatni najlepszy ruch będzie wykonany
        if self.max:
            # best
            pass


class TicTacToe():
    def __init__(self, dimension: int, player1, player2):
        # who_starts = '0' - player starts
        # who_starts = '1' - oponent starts

        self.signs = ('o', 'x')
        self.dimension = dimension
        player1.max = True
        player2.max = False
        self.players = (player1, player2)
        self.who_moves = 0
        self.board = self.create_board(dimension)
        self.finished = False
        self.winner = None

    def create_board(self, dimension: int):
        # działa
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
        # działa
        for i in range(self.dimension):
            fields = []
            for j in range(self.dimension):
                fields.append(self.board[i][j])
            row = '|' + '|'.join(fields) + '|'
            print(row)

    def move(self):
        # raczej działa
        player = self.players[self.who_moves]
        move_type = player.move(self.board)

        self.change_board(move_type)
        self.who_moves = not self.who_moves

    def change_board(self, move_type):
        # nie wiadomo czy działa
        sign = self.signs[self.who_moves]

        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.board[i][j] == move_type:
                    self.board[i][j] = sign

        if self.is_winner(sign):
            self.finished = True
            self.winner = self.who_won()
        elif self.is_draw():
            self.finished = True
            self.winner = 0

    def is_winner(self, sign) -> bool:
        # nie wiadomo czy działa
        for i in range(self.dimension):
            col_line = True
            row_line = True
            diag1_line = True
            diag2_line = True
            if self.board[i][i] != sign:
                diag1_line = False
            if self.board[i][-i-1] != sign:
                diag2_line = False

            for j in range(self.dimension):
                if self.board[i][j] != sign:
                    row_line = False
                if self.board[j][i] != sign:
                    col_line = False
            if col_line:
                return True
            if row_line:
                return True
        if diag1_line or diag2_line:
            return True
        if not self.possible_moves():
            return True

    def is_draw(self) -> bool:
        if not self.possible_moves():
            return True

    def who_won(self) -> int:
        if self.who_moves:
            return 1
        else:
            return -1

    def possible_moves(self) -> int:
        # raczej działa
        moves = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.board[i][j] not in self.signs:
                    moves.append(self.board[i][j])
        return moves


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
