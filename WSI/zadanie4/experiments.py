from sklearn.model_selection import train_test_split, cross_validate
from sklearn.svm import SVC
from sklearn import metrics
import numpy as np
import pandas as pd


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

    # wyniki z walidacji krzyżowej
    scores_precision = []
    scores_accuracy = []
    scores_recall = []
    scores_f1 = []

    # wyniki z predykcji
    pred_precision = []
    pred_accuracy = []
    pred_recall = []
    pred_f1 = []

    for linearization_value in args['linearization']:

        # wykonanie eksperymentu dla 3 różnych seedów
        for seed in range(3):

            # dzielenie danych na trening i test
            x_train, x_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=seed
                )

            # utworzenie modelu i walidacja
            clf = SVC(
                C=linearization_value,
                kernel='linear',
                random_state=seed
                )
            scores = cross_validate(clf, X, y, scoring=scoring)

            # dodanie do list wyników z walidacji
            scores_precision.append(scores['test_precision_macro'])
            scores_accuracy.append(scores['test_accuracy'])
            scores_recall.append(scores['test_recall_macro'])
            scores_f1.append(scores['test_f1_macro'])

            # trenowanie modelu i predykcja na danych testowych
            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)

            # zapisanie danych z predykcji do list
            pred_precision.append(metrics.precision_score(
                y_test,
                y_pred,
                average='macro'
                ))
            pred_accuracy.append(metrics.accuracy_score(
                y_test,
                y_pred,
                ))
            pred_recall.append(metrics.recall_score(
                y_test,
                y_pred,
                average='macro'
                ))
            pred_f1.append(metrics.f1_score(
                y_test,
                y_pred,
                average='macro'
                ))

        # zapisanie średnich i odchyleń do rezultatów
        results = pd.DataFrame({
            'precision_cv': {
                'mean': np.mean(scores_precision),
                'dev': np.std(scores_precision)
            },
            'precision_pred': {
                'mean': np.mean(pred_precision),
                'dev': np.std(pred_precision)
            },
            'accuracy_cv': {
                'mean': np.mean(scores_accuracy),
                'dev': np.std(scores_accuracy)
            },
            'accuracy_pred': {
                'mean': np.mean(pred_accuracy),
                'dev': np.std(pred_accuracy)
            },
            'recall_cv': {
                'mean': np.mean(scores_recall),
                'dev': np.std(scores_recall)
            },
            'recall_pred': {
                'mean': np.mean(pred_recall),
                'dev': np.std(pred_recall)
            },
            'f1_cv': {
                'mean': np.mean(scores_f1),
                'dev': np.std(scores_f1)
            },
            'f1_pred': {
                'mean': np.mean(pred_f1),
                'dev': np.std(pred_f1)
            },
        }).transpose()

        # zapisanie wyników w pliku
        save_results(
            data=results,
            path=args['svm_results_path'],
            param_name='linearization',
            param_value=linearization_value
            )
