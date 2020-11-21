# Iris ClassifierPYTHON
# (Python Data Science > Classification > Machine Learning > Numpy > Scikit-learn)
#
# As a part of an application for iris enthusiasts, implement the train_and_predict function
# which should be able to classify three types of irises based on four features.
#
# The train_and_predict function accepts three parameters:
#   - train_input_features - a two-dimensional NumPy array where each element is an array
#                            that contains: sepal length, sepal width, petal length, and petal width.
#   - train_outputs - a one-dimensional NumPy array where each element is a number representing the
#                     species of iris which is described in the same row of train_input_features.
#                          0 represents Iris setosa
#                          1 represents Iris versicolor
#                          2 represents Iris virginica
#   - prediction_features - two-dimensional NumPy array where each element is an array that contains:
#                           sepal length, sepal width, petal length, and petal width.
#
# The function should train a classifier using train_input_features as input data and train_outputs
# as the expected result. After that, the function should use the trained classifier to predict labels
# for prediction_features and return them as an iterable (like list or numpy.ndarray).
# The nth position in the result should be the classification of the nth row of the prediction_features parameter.


import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
# Extra libraries
from numpy import ndarray
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier


def train_and_predict(train_input_features, train_outputs, prediction_features, model='tree'):
    """
    :param train_input_features: (numpy.array) A two-dimensional NumPy array where each element
                        is an array that contains: sepal length, sepal width, petal length, and petal width
    :param train_outputs: (numpy.array) A one-dimensional NumPy array where each element
                        is a number representing the species of iris which is described in
                        the same row of train_input_features. 0 represents Iris setosa,
                        1 represents Iris versicolor, and 2 represents Iris virginica.
    :param prediction_features: (numpy.array) A two-dimensional NumPy array where each element
                        is an array that contains: sepal length, sepal width, petal length, and petal width
    :returns: (list) The function should return an iterable (like list or numpy.ndarray) of the predicted
                        iris species, one for each item in prediction_features
    """
    # Scale the data
    sc = StandardScaler()
    sc.fit(train_input_features)
    X_tr_std = sc.transform(train_input_features)
    X_pred_std = sc.transform(prediction_features)

    if model == 'svc':
        # SVC model
        svm = SVC(kernel='rbf', random_state=517, gamma=.1, C=1.)
        svm.fit(X_tr_std, train_outputs)
        return svm.predict(X_pred_std)

    elif model == 'tree':
        # Create and train decision tree model
        decision_tree = tree.DecisionTreeClassifier(criterion='gini')
        decision_tree.fit(X_tr_std, train_outputs)
        return decision_tree.predict(X_pred_std)

    else: # Random Forest
        rf_classifier = RandomForestClassifier()
        rf_classifier.fit(X_tr_std, train_outputs)
        return rf_classifier.predict(X_pred_std)


def test_iris_classifier_svc():
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                        test_size=0.3, random_state=0)

    y_pred = train_and_predict(X_train, y_train, X_test, model='svc')
    assert isinstance(y_pred, (list, ndarray))
    assert len(y_pred) == len(y_test)

    if y_pred is not None:
        print(metrics.accuracy_score(y_test, y_pred))


def test_iris_classifier_tree():
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                        test_size=0.3, random_state=0)

    y_pred = train_and_predict(X_train, y_train, X_test, model='tree')
    assert isinstance(y_pred, (list, ndarray))
    assert len(y_pred) == len(y_test)

    if y_pred is not None:
        print(metrics.accuracy_score(y_test, y_pred))


def test_iris_classifier_random_forest():
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                        test_size=0.3, random_state=0)

    y_pred = train_and_predict(X_train, y_train, X_test)
    assert isinstance(y_pred, (list, ndarray))
    assert len(y_pred) == len(y_test)

    if y_pred is not None:
        print(metrics.accuracy_score(y_test, y_pred))


if __name__ == "__main__":
    test_iris_classifier_random_forest()
