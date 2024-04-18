from timeit import default_timer as timer


def save_starting_moves(data, path):
    with open(path, 'w') as file:
        file.write('move,time,nodes,mean_depth\n')
        for move in data:
            time = data[move]['time']
            nodes = data[move]['nodes']
            mean_depth = data[move]['mean_depth']
            row = f'{move},{time},{nodes},{mean_depth}\n'
            file.write(row)


def time_measure(game, minmax, move, n, alpha=None, beta=None):
    data = []
    for i in range(n):
        start = timer()
        minmax.eval(game, move, alpha, beta)
        end = timer()
        minmax.reset()
        data.append(end - start)
        print(f'{i}: {end - start}')
    mean_time = sum(data) / len(data)
    return mean_time


def measure_depth(game, minmax, move, alpha=None, beta=None):
    data = {}
    minmax.eval(game, move, alpha, beta)
    data['mean_depth'] = minmax.mean_depth()
    data['nodes'] = minmax.nodes
    minmax.reset()
    return data


def mean_values(data: list[list]) -> list:
    length = len(data[0])
    mean = []

    for i in range(length):
        sum = 0
        for points in data:
            sum += points[i]
        mean.append(sum / len(data))
    return mean


def measure_times_no_pruning(game):
    data = []
    while not game.finished:
        start = timer()
        game.ask_for_move()
        end = timer()
        data.append(end - start)
    return data


def save_progress_times(data, path):
    with open(path, 'w') as file:
        for times in data:
            row = []
            for time in times:
                row.append(str(time))
            row = ','.join(row)
            file.write(row + '\n')
