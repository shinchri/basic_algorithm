"""
Problem 6: Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers.

The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = None
    max = None

    for int in ints:
        if min is None or min > int:
            min = int
        if max is None or max < int:
            max = int

    return (min, max)

### TEST CASES ###
## Example Test Case of Ten Integers
import random

# Case 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Case 2
l = [-1, 3, 5, 2, -6, 3]
random.shuffle(l)

print ("Pass" if ((-6, 5) == get_min_max(l)) else "Fail")


# Case 3
l = [1]
random.shuffle(l)

print("Pass" if ((1,1) == get_min_max(l)) else "Fail")

# Case 4
l = []

print("Pass" if (None, None) == get_min_max(l)  else "Fail")