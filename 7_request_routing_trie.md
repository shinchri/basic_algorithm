# Explanation

## Reason for choice in data structure

Trie is used because it is an efficient way to store a set of strings that have some common character(s).

## time complexity


### RouteTrieNode class
- insert method takes `O(1)` for simply inserting node.

### RouteTrie class
- insert method takes `O(n)` where n is the length of the path list.
- find method takes `O(n)` where n is the length of thepath list.

### Router Class:
- split_path method takes `O(1)`.
- lookup method take `O(n)` since it uses find method and split_path.

## space complexity

### RouteTrieNode class
- insert method takes `O(1)` for simply inserting node.

### RouteTrie class
- insert method takes `O(n)` where n is the length of the path list.
- find method takes `O(1)` since it does not take up any additional space. 

### Router Class:
- split_path method takes `O(n)` where n is the length of the path list.
- lookup method takes `O(1)` since it does not take additional space.
