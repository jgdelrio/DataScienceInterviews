"""
Given a file that contains a list of numbers (one per line) write a program with a function
called get_top_n to print out the 5 most commonly occurring numbers, one per line,
without whitespaces and in descending order of frequency.
"""

import sys
from pandas import read_csv
from collections import Counter


def get_top_n(filename, n=5):
    data = read_csv(filename, header=None)
    # spaces are already removed...

    # Select top n and print it
    topn = data.iloc[:, 0].value_counts().index[:n]

    # Other possibility (Counter)
    topn = Counter

    print('\n'.join(map(str, topn)))


if __name__ == '__main__':
    total = len(sys.argv)
    arguments = sys.argv

    if total == 0:
        raise ValueError('The filename is required as argument')
    if total > 2:
        n = arguments[2]
    else:
        n = 5
    get_top_n(arguments[1], n)

    # To run the example: python most_occurring_numbers.py numbers.txt
    # Note that you can achieve the same result using a bash one-liner
    #    sed 's/ //g' numbers.txt | sort | uniq -c | sort -k1.1nr -k2 | sed 's/^ *[0-9]* //' | head -5
    #  sed to eliminate spaces, we sort together, with uniq we create the freq count,
    #  we sort by frequency in descending order, eliminate the frequencies, and keep the top 5
