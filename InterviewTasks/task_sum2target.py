"""
Write a function that given a list of integers and a target, finds if it is possible to obtain
the target with the sum of the number in the list.
- It is possible to use as many numbers in the list as required (without selecting twice the same entry).
- Return True if it is possible to obtain the target and False otherwise

Examples:
    [1,2,4,9] target: 8 --> Returns False
    [1,2,4,4] target: 8 --> Returns True
    [-3, 1, 3, 13] target: 10 --> Returns True
"""

from time import time


def sum2target(entry_list: tuple, target: int) -> bool:
    memo = {}

    def helper(curr_sum, idx):
        if curr_sum == target:
            return True
        if idx == len(entry_list) or curr_sum > target:
            return False
        if (curr_sum, idx) in memo:
            return memo[(curr_sum, idx)]

        selected = helper(curr_sum + entry_list[idx], idx + 1)
        not_selected = helper(curr_sum, idx + 1)

        memo[(curr_sum, idx)] = selected or not_selected

        return memo[(curr_sum, idx)]

    return helper(0, 0)

# The time complexity of this function is O(2^n) because we are trying out all possible combinations
# of numbers to see if the target can be obtained. The function uses memoization to store the results
# of subproblems and prevent redundant calculations, but the worst-case time complexity remains exponential.



# Try other solutions: ##################


def sum2target_1st_last(entry_list: tuple, target: int) -> bool:
    idx = 0
    last = len(entry_list) - 1
    accum = []

    if target in entry_list:
        return True

    while idx < last:
        val = entry_list[idx] + entry_list[last]
        accum = accum + [i + next2sum for i in accum]
        if (val == target) or (target in accum):
            return True
        elif val > target:
            last -= 1
        else:
            idx += 1
            accum.append(val)
            next2sum = entry_list[idx]

    return False


# For the first function `sum2target`, which uses recursion with memoization,
# the time complexity is O(n * target), where n is the number of elements in the entry_list.
# The auxiliary space complexity is also O(n * target) due to the memoization map.

# For the second function `sum2target_1st_last`, the time complexity is O(n^2) in the worst case,
# where n is the number of elements in the entry_list. The reason is that the while loop iterates
# through the list while adjusting the pointers `idx` and `last`, potentially resulting in checking
# all pairs of elements. The space complexity is O(n) due to the `accum` list storing sums of pairs.

# In terms of performance, the first approach is more efficient and scalable,
# especially for larger input sizes. The second approach has a higher time complexity
# due to the nested iteration through the list.


# Test samples
TESTS = (
    [(1, 2, 4, 9), 8, False],
    [(1, 2, 4, 4), 8, True],
    [(-3, 1, 3, 13), 10, True],
    [(-3, 2, 2, 2, 3, 10, 100), 19, True],
)


def time_execution(num_loops: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(num_loops):
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()
                total_time += end_time - start_time
            avg_time = total_time / num_loops
            print(f"Avg execution time over {num_loops} loops: {avg_time} seconds")
            return result
        return wrapper
    return decorator


@time_execution(10)
def test_function(func):
    for idx, test in enumerate(TESTS):
        result = func(test[0], test[1])
        if result != test[2]:
            print(f"Test case {idx+1} failed: {test}")


if __name__ == "__main__":
    test_function(sum2target_1st_last)
