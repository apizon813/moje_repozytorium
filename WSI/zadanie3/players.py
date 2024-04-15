from minmax import minmax


class Player():
    def move(self, game: str) -> str:

        move_type = input(f'{game.sign} move > ')
        return move_type


class Oponent():
    def __init__(self, max) -> None:
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
            best_move = best_moves[0]
            print(f'{game.sign} move > {best_move}')
            return best_move

        else:
            best_moves = []
            best_move_val = min(moves_values.values())
            for move in moves_values:
                if moves_values[move] == best_move_val:
                    best_moves.append(move)
            best_move = best_moves[0]
            print(f'{game.sign} move > {best_move}')

            return best_move
        # dopisać co jeśli min
