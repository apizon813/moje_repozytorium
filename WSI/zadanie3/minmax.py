class DepthAggregate():
    def __init__(self) -> None:
        self.aggregate = []

    def add_depth(self, depth):
        self.aggregate.append(depth)

    def mean_depth(self):
        return sum(self.aggregate) / len(self.aggregate)


def minmax(
        game,
        move,
        depth=1,
        aggregate=False,
        pruning=False,
        alpha=None,
        beta=None
        ):

    game.change_board(move)

    if game.finished:
        state = game.state
        game.undo()
        if aggregate:
            aggregate.add_depth(depth)
            return state, aggregate
        else:
            return state

    max_moves: bool = game.who_moves

    possible_moves = game.possible_moves()

    max_val = -2
    min_val = 2

    for move in possible_moves:

        if aggregate:
            value, aggregate = minmax(
                game,
                move,
                depth + 1,
                aggregate,
                pruning,
                alpha,
                beta
                )
        else:
            value = minmax(
                game,
                move,
                depth + 1,
                aggregate,
                pruning,
                alpha,
                beta
                )

        if max_moves:
            max_val = max(max_val, value)
            if pruning:
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
        else:
            min_val = min(min_val, value)
            if pruning:
                beta = min(beta, value)
                if beta <= alpha:
                    break

    if max_moves:
        result = max_val
    else:
        result = min_val

    if aggregate:
        game.undo()
        return result, aggregate
    else:
        game.undo()
        return result
