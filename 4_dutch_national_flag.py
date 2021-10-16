"""
Problem 4: Dutch National Flag

Given an input array consisting on only 0, 1 and 2, sort the array in a single traversal. You are not allowed to 
use any sorting function that Python provides

Note: `O(n)` does not necessarily ean single-traversal. For e.g. if you traverse the array twice, that would still
be `O(n)` solution but it will not count as single traversal.
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    num_0 = []
    num_1 = []
    num_2 = []
    for index,element in enumerate(input_list):
        if element == 0:
            num_0.append(element)
        elif element == 1:
            num_1.append(element)
        else:
            num_2.append(element)
    return num_0 + num_1 + num_2


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])