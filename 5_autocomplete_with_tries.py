"""
Problem 5: Finding Suffixes

From the functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.
To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that
exist below it in the trie.

For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would
expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`
"""

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
            
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        
        return current_node


    def suffixes(self, suffix = ''):
        arr = []
        self._suffixes_recursion(suffix, arr)
        return arr

    def _suffixes_recursion(self, suffix, arr, chars=''):
        node = self.find(suffix)

        if node is None:
            return []
        
        for char in node.children:
            if self.find(suffix+char).is_word:
                arr.append(chars+char)
            self._suffixes_recursion(suffix+char, arr, chars=chars+char)


### TEST CASES ###

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Case 1
print(MyTrie.suffixes("")) 
# Output: ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

# Case 2
print(MyTrie.suffixes("asdfasdf")) 
# Output: []

# Case 3
print(MyTrie.suffixes("fu"))
# Output: ['n', 'nction']

# Case 4
print(MyTrie.suffixes("ant"))
# Output: ['hology', 'agonist', 'onym']