import matplotlib.pyplot as plt
import numpy as np


def plotter(solution, args):

    function = args.function
    path = args.plot_path
    generations = args.plot_generations
    data = solution.data
    image_fun = globals()[function + '_im']

    fig, axes = plt.subplots(2, 3)
    for i, ax in enumerate(axes.flat):
        image_fun(ax)
        generation = generations[i]
        plot_population(ax, data, generation)
        ax.set_title(f'gen={generation}')

    fig.suptitle(f'{function} function')
    fig.savefig(path)


def plot_population(ax, data, generation):
    points = data[generation][0]
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])

    ax.scatter(
        x,
        y,
        marker='v',
        color='r',
    )


def plot_end_populations(solutions, params_set):

    fig, axes = plt.subplots(2, 3)
    for i, ax in enumerate(axes.flat):
        args = params_set[i]
        function = args.function
        image_fun = globals()[function + '_im']

        solution = solutions[i]
        data = solution.data
        generation = args.max_generations
        image_fun(ax)
        plot_population(ax, data, generation)

        var_val = getattr(solution, args.variable)

        ax.set_title(f'{args.variable}={var_val}')

    fig.suptitle(f'{function} function')
    fig.savefig(args.plot_end_path)


def fitness_plot(solutions, args):

    fig, ax = plt.subplots()

    for solution in solutions:
        x = []
        y = []
        for generation in solution.data:
            x.append(generation)
            y.append(solution.data[generation][1])
        var_val = getattr(solution, args.variable)
        label = f'{args.variable}={var_val}'
        ax.plot(x, y, label=label)
    plt.xlabel('generation')
    plt.ylabel('mean distance')
    ax.legend()
    fig.savefig(args.fit_path)


def rastrigin_im(ax):

    x = np.linspace(-5.12, 5.12, 1024)
    y = np.linspace(-5.12, 5.12, 1024)
    X, Y = np.meshgrid(x, y)

    Z = (X**2 - 10 * np.cos(2 * np.pi * X)) + \
        (Y**2 - 10 * np.cos(2 * np.pi * Y)) + 20

    ax.imshow(
        Z,
        cmap='plasma',
        extent=[np.min(x), np.max(x), np.min(y), np.max(y)]
    )


def griewank_im(ax):
    x = np.linspace(-50, 50, 1024)
    y = np.linspace(-50, 50, 1024)
    X, Y = np.meshgrid(x, y)

    Z = 1 + X ** 2 / 4000 + Y ** 2 / 4000 - np.cos(X) * np.cos(Y/np.sqrt(2))

    ax.imshow(
        Z,
        cmap='plasma',
        extent=[np.min(x), np.max(x), np.min(y), np.max(y)]
    )
