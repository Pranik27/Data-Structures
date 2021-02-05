# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:10:59 2021

@author: PRANIKP

TRIE CRUD Operation using fixed size list .

Time Complexity:
Space Complexity:
"""

class TrieNode:
    
    def __init__(self):
        self.isEndOfWord = False
        self.children = [None]*26

class Trie:
    
    def __init__(self):
        self.curr = TrieNode()
        
    
    def insert(self,word): #TC : O(N * M) , SC = O(26 * M * N) ,where N is the no of words to be inseted and M is the approx lenght of each word
        parent_node = self.curr
        
        for c in word:
            
            
            if (parent_node.children[ord(c) - ord('a')] == None):
                parent_node.children[ord(c) - ord('a')] = TrieNode()
                
            parent_node = parent_node.children[ord(c) - ord('a')]
            
        parent_node.isEndOfWord = True
        
    def select(self,word): #TC : O(M) , where M is the length of the word
        curr = self.curr
        
        for c in word:
           
            if (curr.children[ord(c) - ord('a')] == None):
                return False
            
            curr = curr.children[ord(c) - ord('a')]
        
        if not curr.isEndOfWord:
            return False
        
        return True
    
    
    def startsWith(self,word): #TC : O(M) , where M is the length of the word
        
        curr = self.curr
        
        for c in word:
           
            if (curr.children[ord(c) - ord('a')] == None):
                return False
            
            curr = curr.children[ord(c) - ord('a')]
        
        return True



t = Trie()

t.insert('apple')
t.insert('bat')
print(t.select('apple'))
print(t.select('bat'))
print(t.startsWith('app'))
print(t.startsWith('ba'))

        