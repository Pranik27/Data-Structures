"""
This program consists of different operations along with Time and space complexity analysis
for Trie data Structure.
"""

class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self,word): #O(m) Time and space complexity , where 'm' is the length of the word to be inserted.
        parent_node = self.root

        for ch in word:
            print(parent_node.children)
            current_node = parent_node.children.get(ch)

            if not current_node:
                current_node = TrieNode()
                parent_node.children.update({ch:current_node})

            parent_node = current_node

        parent_node.endOfString = True
        print("Successful Insertion")

    def searchString(self,word):#Constant O(1) Space complexity and O(m) Time cmplexity where 'm' is the length of word.
        current_node = self.root

        for ch in word:
            node = current_node.children.get(ch)
            if not node:
                return False
            current_node = node

        if current_node.endOfString:
            return True
        else:
            return False


new_trie = Trie()

new_trie.insert("APP")
new_trie.insert("AP")
new_trie.insert("BAT")

print(new_trie.searchString("APP"))
print(new_trie.searchString("ABCD"))
print(new_trie.searchString("BAT"))


