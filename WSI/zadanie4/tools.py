import pandas as pd


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
