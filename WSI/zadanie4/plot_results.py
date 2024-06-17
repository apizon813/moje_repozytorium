import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def save_plot(fig, path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    fig.savefig(path)


def load_results(param_name, path_template, param_values):
    results = []
    for value in param_values:
        path = path_template.format(int(value))
        result = pd.read_csv(path)
        result[param_name] = value
        results.append(result)
    return pd.concat(results)


# Wczytanie wyników
regularization_values = np.logspace(-3, 3, 50)
iteration_values = np.logspace(1, 5, 50, dtype=int)
tree_iteration_values = np.linspace(1, 50, 50, dtype=int)

svm_regularization_results = load_results(
    "regularization",
    "results/plots/svm_regularization_C_{:04}.csv",
    regularization_values,
)
svm_iterations_results = load_results(
    "iterations",
    "results/plots/svm_iterations_iterations_{:04}.csv",
    iteration_values,
)
tree_iterations_results = load_results(
    "iterations",
    "results/plots/tree_iterations_max_depth_{:04}.csv",
    tree_iteration_values,
)

# Rysowanie wykresu dla siły regularizacji
plt.figure(figsize=(10, 6))
plt.plot(
    svm_regularization_results["regularization"],
    svm_regularization_results["precision_cv_mean"],
    marker="o",
)
plt.title("Wpływ siły regularizacji na precyzję SVM")
plt.xlabel("Siła regularizacji (C)")
plt.ylabel("Średnia precyzja z walidacji krzyżowej")
plt.xscale("log")
plt.grid(True)
save_plot(plt, "results/plots/svm_regularization_plot.png")
plt.show()

# Rysowanie wykresu dla liczby iteracji SVM
plt.figure(figsize=(10, 6))
plt.plot(
    svm_iterations_results["iterations"],
    svm_iterations_results["precision_cv_mean"],
    marker="o",
)
plt.title("Wpływ liczby iteracji na precyzję SVM")
plt.xlabel("Liczba iteracji")
plt.ylabel("Średnia precyzja z walidacji krzyżowej")
plt.xscale("log")
plt.grid(True)
save_plot(plt, "results/plots/svm_iterations_plot.png")
plt.show()

# Rysowanie wykresu dla liczby iteracji drzewa decyzyjnego
plt.figure(figsize=(10, 6))
plt.plot(
    tree_iterations_results["iterations"],
    tree_iterations_results["precision_cv_mean"],
    marker="o",
)
plt.title(
    "Wpływ liczby iteracji (maks. głębokości) na precyzję Drzewa Decyzyjnego"
)
plt.xlabel("Liczba iteracji (maks. głębokość)")
plt.ylabel("Średnia precyzja z walidacji krzyżowej")
plt.grid(True)
save_plot(plt, "results/plots/tree_iterations_plot.png")
plt.show()
