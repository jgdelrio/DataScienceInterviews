# Stock Prices
# (Python Data Science > Correlation > Numpy & Pandas)
#
# You are given a list of tickers and their daily closing prices for a given period.
#
# Implement the most_corr function that, when given each ticker's daily closing prices,
# returns the pair of tickers that are the most highly (linearly) correlated by daily percentage change.


import pandas as pd
import numpy as np


def most_corr(prices):
    """
    :param prices: (pandas.DataFrame) A dataframe containing each ticker's
                   daily closing prices.
    :returns: (container of strings) A container, containing the two tickers that
              are the most highly (linearly) correlated by daily percentage change.
    """
    # Correlation % change for each pair of stocks
    correlations = prices.pct_change().corr().unstack()
    # Eliminate auto-correlations and sort
    sorted_cor = correlations[correlations != 1].sort_values(ascending=False, kind='quicksort')
    return list(sorted_cor.index[0])


def test_most_corr():
    input_data = pd.DataFrame.from_dict({
        'GOOG' : [
            742.66, 738.40, 738.22, 741.16,
            739.98, 747.28, 746.22, 741.80,
            745.33, 741.29, 742.83, 750.50
        ],
        'FB' : [
            108.40, 107.92, 109.64, 112.22,
            109.57, 113.82, 114.03, 112.24,
            114.68, 112.92, 113.28, 115.40
        ],
        'MSFT' : [
            55.40, 54.63, 54.98, 55.88,
            54.12, 59.16, 58.14, 55.97,
            61.20, 57.14, 56.62, 59.25
        ],
        'AAPL' : [
            106.00, 104.66, 104.87, 105.69,
            104.22, 110.16, 109.84, 108.86,
            110.14, 107.66, 108.08, 109.90
        ]
    })
    expected_tickers = ['MSFT', 'FB']

    predicted_tickers = most_corr(input_data)
    print(predicted_tickers)

    assert predicted_tickers == expected_tickers


if __name__ == "__main__":
    test_most_corr()
