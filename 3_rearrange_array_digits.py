"""
Problem 3: Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is maximum.
Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number
of digits in both the numbers cannot differ by more than 1. You are not allowed to use any built-in python sorting function.

Expected time complexity is O(nlog(n))
"""

def heapsort(arr):
    n = len(arr)

    # build maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # one by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

    return arr
    
def heapify(arr, n, i):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """
    # Using i as the index of the current node, find the 2 child nodes (if the array were a binary tree)
    # and find the largest value.   If one of the children is larger swap the values and recurse into that subree
    
    # consider current index as largest
    largest_index = i 
    left_node = 2 * i + 1     
    right_node = 2 * i + 2     
  
    # compare with left child
    if left_node < n and arr[i] < arr[left_node]: 
        largest_index = left_node
  
    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]: 
        largest_index = right_node
  
    # if either of left / right child is the largest node
    if largest_index != i: 
        arr[i], arr[largest_index] = arr[largest_index], arr[i] 
    
        heapify(arr, n, largest_index)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if len(input_list) == 0:
        return []

    if len(input_list) == 1:
        return [input_list[0]]

    sorted_list = heapsort(input_list)

    list_len = len(sorted_list)
    mid = list_len//2
    num_1 = num_2 = ""
    for index, element in enumerate(sorted_list):
        if index%2 == 0:
            # even
            num_1 = str(element) + num_1
        else:
            num_2 = str(element) + num_2
    
    return [int(num_1), int(num_2)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
        
test_function([[1, 2, 3, 4, 5], [542, 31]])

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case = [[], []]
test_function(test_case)

test_case = [[1], [1]]
test_function(test_case)