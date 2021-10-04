"""
Dog Classification
(General Data Science > Classification > Decision Boundary)

The first column contains information if the dog is in the image or not.
The second column contains the classifier prediction, which is in the interval 0-100,
with higher values meaning that the classifier is more confident that image contains a dog.

What is the value of the decision boundary that will maximize the accuracy of the model?
Values greater than or equal to the decision boundary will be treated as positive.
"""


import numpy as np
import pandas as pd
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt


def get_threshold_for_max_accuracy(tpr, fpr, thresholds, num_positives, num_negatives):
    """Calculate the best accuracy and threshold"""
    tp = tpr * num_positives
    tn = (1 - fpr) * num_negatives
    acc = (tp + tn) / (num_positives + num_negatives)

    best_threshold = thresholds[np.argmax(acc)]
    return np.amax(acc), best_threshold


def run_analysis():
    # Read data
    data_file = './files/dog_classification.csv'
    df = pd.read_csv(data_file)

    # We could calculate by hand the roc curve but it's easier to use the build-in utilities in sklearn
    fpr, tpr, thresholds = roc_curve(df['Dog is on image'], df['Classifier prediction'])

    plt.figure(1)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.plot(fpr, tpr, label='Ratio')
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve')
    plt.legend(loc='best')
    plt.savefig('./images/dog_classification_roc.png')
    plt.show()

    # Get total counts for positives and negatives
    positives_count = df['Dog is on image'].sum()
    negatives_count = df.shape[0] - positives_count
    # Calculate best threshold
    max_acc, best_threshold = get_threshold_for_max_accuracy(tpr, fpr, thresholds, positives_count, negatives_count)
    print(f"Max acc is {max_acc:.2f} with threshold {best_threshold}")


if __name__ == '__main__':
    run_analysis()
