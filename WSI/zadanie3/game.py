class TicTacToe():
    def __init__(self, dimension: int, player_max=None, player_min=None):

        self.players = (player_min, player_max)
        self.signs = ('x', 'o')

        self.who_moves = 1

        self.dimension = dimension
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
        return table

    def print_board(self):
        # działa
        for i in range(self.dimension):
            fields = []
            for j in range(self.dimension):
                fields.append(self.board[i][j])
            row = '|' + '|'.join(fields) + '|'
            print(row)

    def ask_for_move(self):
        # raczej działa
        player = self.players[self.who_moves]
        move_type = player.move(self)
        while move_type not in self.possible_moves():
            print('You cannot mark that field.')
            move_type = player.move(self)

        self.change_board(move_type)

    def undo(self):
        number = 1
        last_move = self.history[-1]
        for i in range(self.dimension):
            for j in range(self.dimension):
                if str(number) == last_move:
                    self.board[i][j] = str(number)
                number += 1
        self.history.pop()
        self.finished = False
        self.winner = None
        self.state = None
        self.who_moves = not self.who_moves

    def change_board(self, move_type):
        self.history.append(move_type)
        sign = self.signs[self.who_moves]
        # nie wiadomo czy działa
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.board[i][j] == move_type:
                    self.board[i][j] = sign

        if self.is_winner():
            self.finished = True
            self.state = self.eval_state()
            self.winner = sign
        elif self.is_draw():
            self.finished = True
            self.state = 0
        self.who_moves = not self.who_moves

    def is_winner(self) -> bool:

        sign = self.signs[self.who_moves]
        diag1_line = True
        diag2_line = True
        for i in range(self.dimension):
            col_line = True
            row_line = True

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
        # if not self.possible_moves():
        #     return False

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
