import copy


def minmax(game, move, depth):
    stop_depth = 6
    board = copy.deepcopy(game)
    board.change_board(move)

    if board.finished:
        # tu powinno być -1 0 i 1 jako możliwe wartości
        # czy winner to int?
        # żeby wybrać ekstremum musi być int
        if depth == stop_depth:
            pass
        return board.state

    maxim = board.who_moves

    if maxim:
        values = []
        for move in board.possible_moves():
            value = minmax(board, move, depth + 1)
            values.append(value)
        if depth == stop_depth:
            pass
        return max(values)

    else:
        values = []
        for move in board.possible_moves():
            value = minmax(board, move, depth + 1)
            values.append(value)
        if depth == stop_depth:
            pass
        return min(values)


class Player():
    def __init__(self) -> None:
        self.max = None

    def move(self, game: str) -> str:

        move_type = input(f'{game.sign} move > ')
        return move_type


class Oponent():
    def __init__(self) -> None:
        self.max = None

    def move(self, game):
        moves_values = {}
        for move in game.possible_moves():
            moves_values[move] = minmax(game, move, 1)

        # ostatni najlepszy ruch będzie wykonany
        if self.max:

            best_moves = []
            best_move_val = max(moves_values.values())
            for move in moves_values:
                if moves_values[move] == best_move_val:
                    best_moves.append(move)
            return best_moves[0]

        else:
            best_moves = []
            best_move_val = min(moves_values.values())
            for move in moves_values:
                if moves_values[move] == best_move_val:
                    best_moves.append(move)
            return best_moves[0]
        # dopisać co jeśli min


class TicTacToe():
    def __init__(self, dimension: int, players, who_starts):
        # who_starts = '0' - player starts
        # who_starts = '1' - oponent starts
        who_starts = 1
        player_min = players[not who_starts]
        player_max = players[who_starts]
        self.signs = ('x', 'o')
        self.dimension = dimension
        player_min.max = False
        player_max.max = True
        self.players = (player_min, player_max)
        self.who_moves = 1
        self.sign = self.signs[1]
        self.board = self.create_board(dimension)
        self.finished = False
        self.state = None
        self.history = []

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
        move_type = player.move(self)
        while move_type not in self.possible_moves():
            print('You cannot mark that field.')
            move_type = player.move(self)

        self.history.append(move_type)
        self.change_board(move_type)

    def change_board(self, move_type):
        # nie wiadomo czy działa
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.board[i][j] == move_type:
                    self.board[i][j] = self.sign

        if self.is_winner():
            self.finished = True
            self.state = self.eval_state()
            self.winner = self.sign
        elif self.is_draw():
            self.finished = True
            self.state = 0
        self.who_moves = not self.who_moves
        self.sign = self.signs[self.who_moves]

    def is_winner(self) -> bool:
        # nie wiadomo czy działa
        diag1_line = True
        diag2_line = True
        for i in range(self.dimension):
            col_line = True
            row_line = True

            if self.board[i][i] != self.sign:
                diag1_line = False
            if self.board[i][-i-1] != self.sign:
                diag2_line = False

            for j in range(self.dimension):
                if self.board[i][j] != self.sign:
                    row_line = False
                if self.board[j][i] != self.sign:
                    col_line = False
            if col_line:
                return True
            if row_line:
                return True
        if diag1_line or diag2_line:
            return True
        if not self.possible_moves():
            return False

    def is_draw(self) -> bool:
        if not self.possible_moves():
            return True

    def eval_state(self) -> int:
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

    def print_winner(self):
        if self.state == 0:
            print('It is a draw.')
        else:
            print(f'{self.winner} won!')


def main():
    players = [Player(), Oponent()]
    who_starts = 1

    game = TicTacToe(
        3,
        players,
        who_starts
        )
    game.board = [
        ['1', '2', '3'],
        ['x', 'o', '6'],
        ['7', '8', '9']
    ]
    game.print_board()

    while not game.finished:
        game.move()
        game.print_board()
    game.print_winner()


if __name__ == "__main__":
    main()
