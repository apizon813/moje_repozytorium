import pandas as pd
import numpy as np
from dataclasses import dataclass, field


@dataclass
class Metrics:
    precision_cv: list = field(default_factory=list)
    accuracy_cv: list = field(default_factory=list)
    recall_cv: list = field(default_factory=list)
    f1_cv: list = field(default_factory=list)

    def update_cv(self, scores):
        self.precision_cv.append(scores["test_precision_macro"])
        if "test_accuracy" in scores:
            self.accuracy_cv.append(scores["test_accuracy"])
        if "test_recall_macro" in scores:
            self.recall_cv.append(scores["test_recall_macro"])
        if "test_f1_macro" in scores:
            self.f1_cv.append(scores["test_f1_macro"])

    def to_dataframe(self):
        results = {
            "precision_cv_mean": np.mean(self.precision_cv),
            "precision_cv_std": np.std(self.precision_cv),
        }
        if self.accuracy_cv:
            results.update(
                {
                    "accuracy_cv_mean": np.mean(self.accuracy_cv),
                    "accuracy_cv_std": np.std(self.accuracy_cv),
                }
            )
        if self.recall_cv:
            results.update(
                {
                    "recall_cv_mean": np.mean(self.recall_cv),
                    "recall_cv_std": np.std(self.recall_cv),
                }
            )
        if self.f1_cv:
            results.update(
                {
                    "f1_cv_mean": np.mean(self.f1_cv),
                    "f1_cv_std": np.std(self.f1_cv),
                }
            )

        return pd.DataFrame([results])
