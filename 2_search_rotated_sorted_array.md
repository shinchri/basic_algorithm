# Explanation

## Reason for choice in data structure

Recursion is used because the sub-problems are similar to the initial problem.

## time complexity

The time complexity is `O(log(n))`. This is reached by finding
the mid value from the input.

## space complexity

The space complexity of `rotated_array_search` method is `O(1)`. This is because the memory used does not depend on the input size.

However, it uses a recursive function called `search_recursive` method, which takes an input array and the successive recursive call takes in half the number of the input array items. Thus, the space complexity of it is `O(log(n))`.