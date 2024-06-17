import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def save_plot(fig, path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    fig.savefig(path)
    print(f"Zapisano wykres: {path}")


def load_results(param_name, path_template, param_values):
    results = []
    total = len(param_values)
    for i, value in enumerate(param_values):
        formatted_value = f"{value:.2e}"  # Formatowanie w notacji naukowej
        path = path_template.format(formatted_value)
        print(
            f"[{i+1}/{total}] Wcz {param_name}: {formatted_value}"
        )  # Postęp wczytywania
        try:
            result = pd.read_csv(path)
            result[param_name] = value
            results.append(result)
        except FileNotFoundError:
            print(
                f"Plik nie znaleziony: {path}"
            )  # Informowanie o brakujących plikach
            continue
    if results:
        return pd.concat(results)
    else:
        raise ValueError(
            "Brak danych do przetworzenia. Sprawdź, czy pliki CSV istnieją."
        )


print("Wczytywanie wyników eksperymentów...")

# Wczytanie wyników
regularization_values = np.logspace(-3, 3, 50)
iteration_values = np.logspace(1, 5, 50, dtype=int)
tree_depth_values = np.linspace(1, 50, 50, dtype=int)

svm_regularization_results = load_results(
    "regularization",
    "results/plots/svm_regularization_C_{}.csv",
    regularization_values,
)
svm_iterations_results = load_results(
    "iterations",
    "results/plots/svm_iterations_iterations_{}.csv",
    iteration_values,
)
tree_depth_results = load_results(
    "max_depth", "results/plots/tree_depth_max_depth_{}.csv", tree_depth_values
)

print("Wyniki wczytane, tworzenie wykresów...")

# Rysowanie wykresu dla siły regularizacji
print("Rysowanie wykresu dla siły regularizacji SVM...")
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
print("Rysowanie wykresu dla liczby iteracji SVM...")
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

# Rysowanie wykresu dla głębokości drzewa decyzyjnego
print("Rysowanie wykresu dla głębokości drzewa decyzyjnego...")
plt.figure(figsize=(10, 6))
plt.plot(
    tree_depth_results["max_depth"],
    tree_depth_results["precision_cv_mean"],
    marker="o",
)
plt.title("Wpływ maksymalnej głębokości drzewa na precyzję Drzewa Decyzyjnego")
plt.xlabel("Maksymalna głębokość drzewa")
plt.ylabel("Średnia precyzja z walidacji krzyżowej")
plt.grid(True)
save_plot(plt, "results/plots/tree_depth_plot.png")
plt.show()

print("Tworzenie wykresów zakończone.")
