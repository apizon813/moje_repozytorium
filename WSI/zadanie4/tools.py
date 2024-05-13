import pandas as pd
import numpy as np
from dataclasses import dataclass, field
from sklearn import metrics


def load_databank(path):
    bankdata = pd.read_csv(
        "iris/iris.data",
        names=[
            'sepal_length',
            'sepal_width',
            'petal_length',
            'petal_width',
            'class'
            ]
        )
    return bankdata


@dataclass
class Metrics():
    precision_cv: list = field(default_factory=list)
    precision_pred: list = field(default_factory=list)
    accuracy_cv: list = field(default_factory=list)
    accuracy_pred: list = field(default_factory=list)
    recall_cv: list = field(default_factory=list)
    recall_pred: list = field(default_factory=list)
    f1_cv: list = field(default_factory=list)
    f1_pred: list = field(default_factory=list)

    def update_cv(self, scores):
        self.precision_cv.append(scores['test_precision_macro'])
        self.accuracy_cv.append(scores['test_accuracy'])
        self.recall_cv.append(scores['test_recall_macro'])
        self.f1_cv.append(scores['test_f1_macro'])

    def update_pred(self, y_test, y_pred):
        self.precision_pred.append(metrics.precision_score(
            y_test,
            y_pred,
            average='macro'
            ))
        self.accuracy_pred.append(metrics.accuracy_score(
            y_test,
            y_pred,
            ))
        self.recall_pred.append(metrics.recall_score(
            y_test,
            y_pred,
            average='macro'
            ))
        self.f1_pred.append(metrics.f1_score(
            y_test,
            y_pred,
            average='macro'
            ))

    def to_dataframe(self):
        results = pd.DataFrame({
            'precision_cv': {
                'mean': np.mean(self.precision_cv),
                'dev': np.std(self.precision_cv)
                },
            'precision_pred': {
                'mean': np.mean(self.precision_pred),
                'dev': np.std(self.precision_pred)
                },
            'accuracy_cv': {
                'mean': np.mean(self.accuracy_cv),
                'dev': np.std(self.accuracy_cv)
                },
            'accuracy_pred': {
                'mean': np.mean(self.accuracy_pred),
                'dev': np.std(self.accuracy_pred)
                },
            'recall_cv': {
                'mean': np.mean(self.recall_cv),
                'dev': np.std(self.recall_cv)
                },
            'recall_pred': {
                'mean': np.mean(self.recall_pred),
                'dev': np.std(self.recall_pred)
                },
            'f1_cv': {
                'mean': np.mean(self.f1_cv),
                'dev': np.std(self.f1_cv)
                },
            'f1_pred': {
                'mean': np.mean(self.f1_pred),
                'dev': np.std(self.f1_pred)
            },
        }).transpose()

        return results
