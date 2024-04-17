from minmax import MiniMax


class Player():
    def move(self, game: str) -> str:

        move_type = input(f'{game.signs[game.who_moves]} move > ')
        return move_type


class Oponent():
    def __init__(self, pruning=False, max=None) -> None:
        self.pruning = pruning
        self.max = max

    def move(self, game):
        moves_values = {}
        minmax = MiniMax(self.pruning)
        for move in game.possible_moves():
            moves_values[move] = minmax.eval(game, move, -2, 2)

        if self.max:

            best_moves = []
            best_move_val = max(moves_values.values())
            for move in moves_values:
                if moves_values[move] == best_move_val:
                    best_moves.append(move)
            best_move = best_moves[0]
            print(f'{game.signs[game.who_moves]} move > {best_move}')
            return best_move

        else:
            best_moves = []
            best_move_val = min(moves_values.values())
            for move in moves_values:
                if moves_values[move] == best_move_val:
                    best_moves.append(move)
            best_move = best_moves[0]
            print(f'{game.signs[game.who_moves]} move > {best_move}')

            return best_move
