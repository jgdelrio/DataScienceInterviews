# Iris ClassifierPYTHON
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

# Please provide the accuracy score


import numpy as np
from sklearn import datasets
