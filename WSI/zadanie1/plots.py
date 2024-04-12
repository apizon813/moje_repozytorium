import matplotlib.pyplot as plt
import numpy as np


def extract_data(data_path):
    with open(data_path, 'r') as data_file:
        data = {}
        for line in data_file:
            line = line[:-1].split(',')
            beta = line[-3]
            if beta in data:
                data[beta].append(line[:4])
            else:
                data[beta] = [line[:4]]

    return data


def plot_lined_points(data, beta):
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    for two_points in data[beta]:
        coords = []
        for coord in two_points:
            coords.append(float(coord))
        x = [coords[0], coords[2]]
        y = [coords[1], coords[3]]
        plt.plot(x, y, color='black')
        x1.append(coords[0])
        x2.append(coords[2])
        y1.append(coords[1])
        y2.append(coords[3])
    plt.scatter(x1, y1, color='blue', label='start')
    plt.scatter(x2, y2, color='red', label='end')


def rastrigin_im():

    x = np.linspace(-5.12, 5.12, 1024)
    y = np.linspace(-5.12, 5.12, 1024)
    X, Y = np.meshgrid(x, y)

    Z = (X**2 - 10 * np.cos(2 * np.pi * X)) + \
        (Y**2 - 10 * np.cos(2 * np.pi * Y)) + 20

    fig, ax = plt.subplots()
    im = ax.imshow(
        Z,
        cmap='plasma',
        extent=[np.min(x), np.max(x), np.min(y), np.max(y)]
    )
    fig.colorbar(
        im,
        ax=ax,
        label='function value'
    )


def griewank_im():
    x = np.linspace(-5, 5, 1024)
    y = np.linspace(-5, 5, 1024)
    X, Y = np.meshgrid(x, y)

    Z = 1 + X ** 2 / 4000 + Y ** 2 / 4000 - np.cos(X) * np.cos(Y/np.sqrt(2))

    fig, ax = plt.subplots()
    im = ax.imshow(
        Z,
        cmap='plasma',
        extent=[np.min(x), np.max(x), np.min(y), np.max(y)]
    )
    fig.colorbar(
        im,
        ax=ax,
        label='Griewank function value'
    )


def quadratic_plot(plot_path, solution):
    x = np.linspace(-10, 10, 1000)
    y = x**2

    data = []
    for i in range(len(solution.data)):
        data.append(solution.data[i])

    x1 = np.array(data)
    y1 = x1 ** 2

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(x1, y1, marker='o', color='red')
    plt.title(f'Quadratic function\nbeta = {solution.beta}')

    plt.savefig(plot_path)


def rastrigin_plot(data_path, plot_path):

    data = extract_data(data_path)

    for beta in data:

        rastrigin_im()
        plot_lined_points(data, beta)

        beta_str = beta.replace('.', '')
        path = plot_path[:-4] + '_beta' + beta_str + plot_path[-4:]
        plt.legend()
        plt.title(f'Rastring function\nbeta = {beta}')
        plt.savefig(path)


def griewank_plot(data_path, plot_path):

    data = extract_data(data_path)

    for beta in data:

        griewank_im()
        plot_lined_points(data, beta)

        beta_str = beta.replace('.', '')
        path = plot_path[:-4] + '_beta' + beta_str + plot_path[-4:]
        plt.legend()
        plt.title(f'Griewank function\nbeta = {beta}')
        plt.savefig(path)
