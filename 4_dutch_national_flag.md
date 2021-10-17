# Explanation

## Reason for choice in data structure

Simple forloop is used to traverse the input array. The if-else is used to check the input value, and is appended to the respective lists. The lists are combined to form the output array.

## time complexity

Since it makes a single traversal, the run time is `O(n)`.

## space complexity

The input list takes `O(n)`. the three lists `num_0`, `num_1`, and `num_2` combined takes `O(n)`. Lastly, a output list is created when you combine three `num_x` lists, which takes another `O(n)`.

The total space complexity is `O(n) + O(n) + O(n)` or `O(n)`.