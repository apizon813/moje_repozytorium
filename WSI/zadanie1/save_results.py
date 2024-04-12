def exp1_save_results(path, solution):
    data = solution.data
    with open(path, 'w') as output:
        for i in range(len(data)):
            coords = ''
            for j in range(len(data[i])):
                coords += f'{data[i][j]},'
                coords = coords[:-1]
            line = f'{i},{coords}\n'
            output.write(line)


def save_results_2d_function(path, solutions):
    with open(path, 'w') as output:
        for solution in solutions:

            start_point = solution.data[0]
            point = solution.x
            line = [
                str(start_point[0]),
                str(start_point[1]),
                str(point[0]),
                str(point[1]),
                str(solution.beta),
                str(solution.current_step),
                str(solution.eval_distance())
            ]
            line = ','.join(line)
            output.write(line + '\n')
