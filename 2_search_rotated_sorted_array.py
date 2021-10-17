"""
Problem 2: Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.

Example: [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2]

You are given a target value to search. If found in the array return its index, otherwise return -1

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(logn).

Example:
Input: `nums = [4, 5, 6, 7, 0, 1 ,2], target = 0, Output: 4
"""

# assume that the input list contains 2 or more values
def search_recursive(input_list, number, start, end):

    if start > end:
        return -1
    
    if number == input_list[start]:
        return start
    if number == input_list[end]:
        return end
    mid = (start+end)//2

    if input_list[mid] ==  number:
        return mid

    
    if number > input_list[mid]:
        if number > input_list[start]:
            return search_recursive(input_list, number, start, mid-1)
        else:
            return search_recursive(input_list, number, mid+1, end)

    else: # number less than mid item
        if number > input_list[start]:
            return search_recursive(input_list, number, start, mid-1)
        else:
            return search_recursive(input_list, number, mid+1, end)

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
        input_list(array), number(int): Input array to search and the target
    Returns:
        int: Index or -1
    """
    # base case
    if len(input_list) == 0:
        return -1

    if len(input_list) == 1:
        if input_list[0] == number:
            return 0
        return -1
    return search_recursive(input_list, number, 0, len(input_list)-1)




### TEST CASES ###
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Case 1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) # prints "Pass"
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) # prints "Pass"
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) # prints "Pass"
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) # prints "Pass"
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) # prints "Pass"

# Case 2
test_function([[1], 1]) # prints "Pass"

# Case 3
test_function([[], 1]) # prints "Pass"