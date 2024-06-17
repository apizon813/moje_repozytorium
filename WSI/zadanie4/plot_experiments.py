import os
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from tools import Metrics


def save_results(data, path, param_name, param_value):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    formatted_value = f"{param_value:.2e}"
    path = f"{path}{param_name}_{formatted_value}.csv"
    data.to_csv(path, index=True)


def experiment_svm_regularization(bankdata):
    X = bankdata.drop("class", axis=1)
    y = bankdata["class"]
    scoring = ["precision_macro"]
    metrics = Metrics()

    regularization_values = np.logspace(
        -3, 3, 50
    )

    for C_value in regularization_values:
        for seed in range(5):
            clf = SVC(C=C_value, kernel="linear", random_state=seed)
            scores = cross_validate(
                clf,
                X,
                y,
                scoring=scoring,
                cv=5,
                return_train_score=False,
                n_jobs=-1,
            )
            metrics.update_cv(scores)

        results = metrics.to_dataframe()
        save_results(
            results, "results/plots/svm_regularization_", "C", C_value
        )


def experiment_svm_iterations(bankdata):
    X = bankdata.drop("class", axis=1)
    y = bankdata["class"]
    scoring = ["precision_macro"]
    metrics = Metrics()

    iteration_values = np.logspace(
        1, 5, 50, dtype=int
    )

    for max_iterations in iteration_values:
        for seed in range(5):
            clf = SVC(
                tol=1e-16,
                max_iter=max_iterations,
                kernel="linear",
                random_state=seed,
            )
            scores = cross_validate(
                clf,
                X,
                y,
                scoring=scoring,
                cv=5,
                return_train_score=False,
                n_jobs=-1,
            )
            metrics.update_cv(scores)

        results = metrics.to_dataframe()
        save_results(
            results,
            "results/plots/svm_iterations_",
            "iterations",
            max_iterations,
        )


def experiment_tree_depth(bankdata):
    X = bankdata.drop("class", axis=1)
    y = bankdata["class"]
    scoring = ["precision_macro"]
    metrics = Metrics()

    depth_values = np.linspace(
        1, 50, 50, dtype=int
    )

    for max_depth in depth_values:
        for seed in range(5):
            clf = DecisionTreeClassifier(
                max_depth=max_depth, random_state=seed
            )
            scores = cross_validate(
                clf,
                X,
                y,
                scoring=scoring,
                cv=5,
                return_train_score=False,
                n_jobs=-1,
            )
            metrics.update_cv(scores)

        results = metrics.to_dataframe()
        save_results(
            results, "results/plots/tree_depth_", "max_depth", max_depth
        )


def main():
    bankdata = pd.read_csv(
        "iris/iris.data",
        names=[
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
            "class",
        ],
    )
    experiment_svm_regularization(bankdata)
    experiment_svm_iterations(bankdata)
    experiment_tree_depth(bankdata)


if __name__ == "__main__":
    main()
