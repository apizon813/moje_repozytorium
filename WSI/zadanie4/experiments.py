from sklearn.model_selection import train_test_split, cross_validate
from sklearn.svm import SVC
from sklearn import metrics
import numpy as np


def save_results(results):
    pass


def experiment1(args, bankdata):
    '''
    eksperyment dotyczący siły regularyzacji
    '''
    x = bankdata.drop('class', axis=1)
    y = bankdata['class']

    scoring = ['precision_macro', 'accuracy', 'recall_macro', 'f1_macro']

    scores_precision = []
    scores_accuracy = []
    scores_recall = []
    scores_f1 = []

    pred_precision = []
    pred_accuracy = []
    pred_recall = []
    pred_f1 = []

    for seed in range(3):
        x_train, x_test, y_train, y_test = train_test_split(
            x,
            y,
            test_size=0.2,
            random_state=seed
            )
        clf = SVC(kernel='linear', random_state=seed)
        scores = cross_validate(clf, x, y, scoring=scoring)

        scores_precision.append(scores['test_precision_macro'])
        scores_accuracy.append(scores['test_accuracy'])
        scores_recall.append(scores['test_recall_macro'])
        scores_f1.append(scores['test_f1_macro'])

        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)

        pred_precision.append(metrics.precision_score(
            y_test,
            y_pred,
            average='macro'
            ))
        pred_accuracy.append(metrics.accuracy_score(
            y_test,
            y_pred,
            average='macro'
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

    results = {
        'precision_cross_validate': {
            'mean': np.mean(scores_precision),
            'dev': np.std(scores_precision)
        },
        'accuracy_cross_validate': {
            'mean': np.mean(scores_accuracy),
            'dev': np.std(scores_accuracy)
        },
        'recall_cross_validate': {
            'mean': np.mean(scores_recall),
            'dev': np.std(scores_recall)
        },
        'f1_cross_validate': {
            'mean': np.mean(scores_f1),
            'dev': np.std(scores_f1)
        },
    }

    save_results(results)
