"""
Create a function 'cosine' to calculate the cosine similarity between two vectors

What tests cases can we consider to evaluate the function?
Implement some of the tests cases.
"""
from typing import Union
import math
import numpy as np
import unittest


def magnitude(vector: np.ndarray) -> float:
    return math.sqrt(np.dot(vector, vector))


def cosine(v1: Union[list, np.ndarray], v2: Union[list, np.ndarray]) -> float:
    if isinstance(v1, list):
        v1 = np.array(v1)
    if isinstance(v2, list):
        v2 = np.array(v2)
    if any([not isinstance(k, np.ndarray) for k in (v1, v2)]):
        raise TypeError('v1 and v2 must be lists or numpy arrays')

    den = np.linalg.norm(v1) * np.linalg.norm(v2)
    # dev = magnitude(v1) * magnitude(v2)             # If asked to implement the norm
    if den == 0:
        # Return None or raise error
        return None
    value = np.dot(v1, v2) / den
    return value


class TestExercise(unittest.TestCase):
    def test_same_vector(self):
        v1 = [1, 2, 3, 4]
        self.assertEqual(cosine(v1, v1), 1)

    def test_zero_case(self):
        v1 = [1, 1]
        v2 = [0, 0]
        self.assertEqual(cosine(v1, v2), None)

    def test_90_degrees(self):
        v1 = [0, 1]
        v2 = [1, 0]
        self.assertEqual(cosine(v1, v2), 0)

    def test_180_degrees(self):
        v1 = [0, 1]
        v2 = [0, -1]
        self.assertEqual(cosine(v1, v2), -1)

    def test_270_degrees(self):
        v1 = [0, 1]
        v2 = [-1, 0]
        self.assertEqual(cosine(v1, v2), 0)


if __name__ == '__main__':
    unittest.main()
