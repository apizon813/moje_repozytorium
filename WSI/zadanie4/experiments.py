from sklearn.model_selection import train_test_split, cross_validate
from sklearn.svm import SVC
from tools import Metrics


def save_results(data, path, param_name, param_value):
    path = f'{path}{param_name}_{param_value}'
    data.to_csv(path, index=True)


def experiment1(args, bankdata):
    '''
    eksperyment dotyczący siły regularyzacji
    '''
    X = bankdata.drop('class', axis=1)
    y = bankdata['class']

    scoring = ['precision_macro', 'accuracy', 'recall_macro', 'f1_macro']

    metrics = Metrics()

    for linearization_value in args['linearization']:
        for seed in range(3):
            x_train, x_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=seed
                )
            clf = SVC(
                C=linearization_value,
                kernel='linear',
                random_state=seed
                )
            scores = cross_validate(clf, X, y, scoring=scoring)
            metrics.update_cv(scores)

            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            metrics.update_pred(y_test, y_pred)

        results = metrics.to_dataframe()
        save_results(
            data=results,
            path=args['svm_results_path'],
            param_name='linearization',
            param_value=linearization_value
            )


def experiment2(args, bankdata):
    '''
    eksperyment dotyczący funkcji jądra
    '''
    X = bankdata.drop('class', axis=1)
    y = bankdata['class']

    scoring = ['precision_macro', 'accuracy', 'recall_macro', 'f1_macro']

    metrics = Metrics()

    for kernel_function in args['kernel']:
        for seed in range(3):
            x_train, x_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=seed
                )
            clf = SVC(
                kernel=kernel_function,
                random_state=seed
                )
            scores = cross_validate(clf, X, y, scoring=scoring)
            metrics.update_cv(scores)

            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            metrics.update_pred(y_test, y_pred)

        results = metrics.to_dataframe()
        save_results(
            data=results,
            path=args['svm_results_path'],
            param_name='kernel',
            param_value=kernel_function
            )


def experiment3(args, bankdata):
    '''
    eksperyment dotyczący liczby iteracji
    '''
    X = bankdata.drop('class', axis=1)
    y = bankdata['class']

    scoring = ['precision_macro', 'accuracy', 'recall_macro', 'f1_macro']

    metrics = Metrics()

    for max_iterations in args['iterations']:
        for seed in range(3):
            x_train, x_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=seed
                )
            clf = SVC(
                tol=1e-16,
                max_iter=max_iterations,
                kernel='linear',
                random_state=seed
                )
            scores = cross_validate(clf, X, y, scoring=scoring)
            metrics.update_cv(scores)

            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            metrics.update_pred(y_test, y_pred)

        results = metrics.to_dataframe()
        save_results(
            data=results,
            path=args['svm_results_path'],
            param_name='iterations',
            param_value=max_iterations
            )
