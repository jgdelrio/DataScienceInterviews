# Marketing Costs
# (Python Data Science > Linear Regression > Machine Learning > Numpy > Scikit-Learn)
#
# 1) Use the data from previous marketing campaigns to evaluate how the number of units sold grows
# linearly as the amount of money invested increases and build a model that captures that knowledge.
#
# 2) Implement a function 'desired_marketing_expenditure', which returns the required amount of money
# that needs to be invested in a new marketing campaign to sell the desired number of units.
# We recommend reusing the previous model. For the desired number of 60,000 units sold
# the expenditure in marketing should be 250,000.


import numpy as np
from sklearn import linear_model


def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):
    """
    :param marketing_expenditure: (list) A list of integers with the expenditure for each previous campaign.
    :param units_sold: (list) A list of integers with the number of units sold for each previous campaign.
    :param desired_units_sold: (integer) Target number of units to sell in the new campaign.
    :returns: (float) Required amount of money to be invested.
    """
    x = np.array(marketing_expenditure).reshape((-1, 1))
    y = np.array(units_sold)

    lr = linear_model.LinearRegression()
    lr.fit(x, y)
    prediction = np.float((desired_units_sold - lr.intercept_intercept_) / lr.coef_)
    return prediction


def test_desired_marketing_expenditure():
    data_marketing_expenditure = [300000, 200000, 400000, 300000, 100000]
    data_units_sold = [60000, 50000, 90000, 80000, 30000]
    desired_units_sold = 60000
    expected_expenditure = 250000

    predicted_expenditure = round(desired_marketing_expenditure(
        data_marketing_expenditure,
        data_units_sold,
        desired_units_sold))
    print(predicted_expenditure)

    assert predicted_expenditure == expected_expenditure


if __name__ == "__main__":
    test_desired_marketing_expenditure()
