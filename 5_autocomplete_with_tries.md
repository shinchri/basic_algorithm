# Explanation

## Reason for choice in data structure

Trie is used because it is a very efficient way of storing strings that have some common characters in them.

## time complexity

The insert function takes `O(n)` where n is the length of the word.

Find method of Trie takes `O(n)` where n is the length of the key.

Suffixes method takes `O(n)` where n is the number of children in the node.

## space complexity

The insert function takes `O(kn)` where `k` is the length of the key and `n` is the number of the key.

Find method of Trie takes `O(1)` since it does not need additional space.

The suffixes method takes `O(n)` where `n` is the number of suffixes.