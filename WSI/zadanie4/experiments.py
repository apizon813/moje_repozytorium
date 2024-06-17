from sklearn.model_selection import train_test_split, cross_validate
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from tools import Metrics, save_results


def experiment_svm_regularization(args, bankdata):
    X = bankdata.drop("class", axis=1)
    y = bankdata["class"]

    scoring = ["precision_macro", "accuracy", "recall_macro", "f1_macro"]
    metrics = Metrics()

    for C_value in args["regularization"]:
        for seed in range(5):
            x_train, x_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=seed
            )
            clf = SVC(C=C_value, kernel="linear", random_state=seed)
            scores = cross_validate(clf, X, y, scoring=scoring, cv=5)
            metrics.update_cv(scores)

            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            metrics.update_pred(y_test, y_pred)

        results = metrics.to_dataframe()
        save_results(
            results, args["svm_results_path"], "regularization", C_value
        )


def experiment_svm_kernel(args, bankdata):
    X = bankdata.drop("class", axis=1)
    y = bankdata["class"]

    scoring = ["precision_macro", "accuracy", "recall_macro", "f1_macro"]
    metrics = Metrics()

    for kernel_function in args["kernel"]:
        for seed in range(5):
            x_train, x_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=seed
            )
            clf = SVC(kernel=kernel_function, random_state=seed)
            scores = cross_validate(clf, X, y, scoring=scoring, cv=5)
            metrics.update_cv(scores)

            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            metrics.update_pred(y_test, y_pred)

        results = metrics.to_dataframe()
        save_results(
            results, args["svm_results_path"], "kernel", kernel_function
        )


def experiment_svm_iterations(args, bankdata):
    X = bankdata.drop("class", axis=1)
    y = bankdata["class"]

    scoring = ["precision_macro", "accuracy", "recall_macro", "f1_macro"]
    metrics = Metrics()

    for max_iterations in args["iterations"]:
        for seed in range(5):
            x_train, x_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=seed
            )
            clf = SVC(
                tol=1e-16,
                max_iter=max_iterations,
                kernel="linear",
                random_state=seed,
            )
            scores = cross_validate(clf, X, y, scoring=scoring, cv=5)
            metrics.update_cv(scores)

            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            metrics.update_pred(y_test, y_pred)

        results = metrics.to_dataframe()
        save_results(
            results, args["svm_results_path"], "iterations", max_iterations
        )


def experiment_tree_criterion(args, bankdata):
    X = bankdata.drop("class", axis=1)
    y = bankdata["class"]

    scoring = ["precision_macro", "accuracy", "recall_macro", "f1_macro"]
    metrics = Metrics()

    for criterion in args["criterion"]:
        for seed in range(5):
            x_train, x_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=seed
            )
            clf = DecisionTreeClassifier(
                criterion=criterion, random_state=seed
            )
            scores = cross_validate(clf, X, y, scoring=scoring, cv=5)
            metrics.update_cv(scores)

            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            metrics.update_pred(y_test, y_pred)

        results = metrics.to_dataframe()
        save_results(
            results, args["tree_results_path"], "criterion", criterion
        )


def experiment_tree_splitter(args, bankdata):
    X = bankdata.drop("class", axis=1)
    y = bankdata["class"]

    scoring = ["precision_macro", "accuracy", "recall_macro", "f1_macro"]
    metrics = Metrics()

    for splitter in args["splitter"]:
        for seed in range(5):
            x_train, x_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=seed
            )
            clf = DecisionTreeClassifier(splitter=splitter, random_state=seed)
            scores = cross_validate(clf, X, y, scoring=scoring, cv=5)
            metrics.update_cv(scores)

            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            metrics.update_pred(y_test, y_pred)

        results = metrics.to_dataframe()
        save_results(results, args["tree_results_path"], "splitter", splitter)


def experiment_tree_depth(args, bankdata):
    X = bankdata.drop("class", axis=1)
    y = bankdata["class"]

    scoring = ["precision_macro", "accuracy", "recall_macro", "f1_macro"]
    metrics = Metrics()

    for depth in args["max_depth"]:
        max_depth = None if depth == "None" else depth
        for seed in range(5):
            x_train, x_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=seed
            )
            clf = DecisionTreeClassifier(
                max_depth=max_depth, random_state=seed
            )
            scores = cross_validate(clf, X, y, scoring=scoring, cv=5)
            metrics.update_cv(scores)

            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            metrics.update_pred(y_test, y_pred)

        results = metrics.to_dataframe()
        save_results(results, args["tree_results_path"], "max_depth", depth)
