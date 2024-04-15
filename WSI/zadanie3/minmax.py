class DepthAggregate():
    def __init__(self) -> None:
        self.aggregate = []

    def add_depth(self, depth):
        self.aggregate.append(depth)

    def mean_depth(self):
        return sum(self.aggregate) / len(self.aggregate)


def minmax(game, move, depth=1, aggregate=False):

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

    values = []
    possible_moves = game.possible_moves()
    for move in possible_moves:

        if aggregate:
            value, aggregate = minmax(game, move, depth + 1, aggregate)
        else:
            value = minmax(game, move, depth + 1)
        values.append(value)
        # if depth == 14:
        #     print(f'thinking...{move}')

    if max_moves:
        game.undo()
        result = max(values)
    else:
        game.undo()
        result = min(values)

    if aggregate:
        return result, aggregate
    else:
        return result
