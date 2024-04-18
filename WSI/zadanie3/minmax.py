class MinMax():
    def __init__(self, pruning=False):

        self.depth = 1
        self.aggregate = []
        self.nodes = 0
        self.pruning = pruning

    def eval(self, game, move, alpha=None, beta=None):
        game.change_board(move)

        if game.finished:
            state = game.state
            game.undo()
            self.aggregate.append(self.depth)
            self.depth -= 1
            return state

        max_val = float('-inf')
        min_val = float('inf')

        for move in game.possible_moves():
            self.depth += 1
            self.nodes += 1
            value = self.eval(game, move, alpha, beta)

            if game.who_moves:
                max_val = max(max_val, value)
                if self.pruning:
                    alpha = max(alpha, value)
                    if beta <= alpha:
                        break
            else:
                min_val = min(min_val, value)
                if self.pruning:
                    beta = min(beta, value)
                    if beta <= alpha:
                        break

        if game.who_moves:
            game.undo()
            self.depth -= 1
            return max_val
        else:
            game.undo()
            self.depth -= 1
            return min_val

    def mean_depth(self):
        return sum(self.aggregate) / len(self.aggregate)

    def reset(self):
        self.depth = 1
        self.aggregate = []
        self.nodes = 0
