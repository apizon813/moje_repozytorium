from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report


def experiment1(pars, bankdata):
    '''
    eksperyment dotyczący siły regularyzacji
    '''
    x = bankdata.drop('class', axis=1)
    y = bankdata['class']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(x_train, y_train)
    y_pred = svclassifier.predict(x_test)
    print(classification_report(y_test, y_pred))
