"""
Problem 5: Finding Suffixes

From the functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.
To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that
exist below it in the trie.

For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would
expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`
"""

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        pass
    
    def insert(self, char):
        ## Add a child node in this Trie
        pass
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        pass

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        pass

    def insert(self, word):
        ## Add a word to the Trie
        pass

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        pass


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='')