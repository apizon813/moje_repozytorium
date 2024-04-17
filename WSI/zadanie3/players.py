from minmax import MiniMax


class Player():
    def move(self, game: str) -> str:

        move_type = input(f'{game.signs[game.who_moves]} move > ')
        return move_type


class Oponent():
    def __init__(self, pruning=False, max=None) -> None:
        self.minmax = MiniMax(pruning)
        self.max = max

    def move(self, game):
        moves = {}
        for move in game.possible_moves():
            moves[move] = self.minmax.eval(game, move, -2, 2)

        moves_best = []
        move_best_value = self.best_value(moves.values())
        for move in moves:
            if moves[move] == move_best_value:
                moves_best.append(move)
        best_move = moves_best[0]
        print(f'{game.signs[game.who_moves]} move > {best_move}')
        return best_move

    def best_value(self, values):
        if self.max:
            return max(values)
        else:
            return min(values)
