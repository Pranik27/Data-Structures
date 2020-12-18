# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:34:34 2020

@author: PRANIKP
"""
class Nodes:
    
    def __init__(self,val,children = []):
        self.val = val
        self.children = children or []
        
    
    
class NArrayTree:

    def __init__(self):
        self.root = None
        self.size = 0
        
    
    def find_node(self,node,key):
        
        
        
        if node.val == key:
            return node
        
        for child in node.children:
            
            return_node = self.find_node(child,key)
            
            if return_node:
                return return_node
            
        return None
    
    

    def add_child(self,val,parent_key = None):
        
        new_node = Nodes(val)
        
        if parent_key == None:
            self.root = new_node
            self.size += 1
        else:
            parent_node = self.find_node(self.root,parent_key)
            
            if not(parent_node):
                return 
            
            parent_node.children.append(new_node)
            self.size += 1
            
    def max_depth(self,root):
        
        if root == None:
            return 0
        
        if root.children == None:
            return 1
        max_depth = 0
        
        for child in root.children:
            max_depth = max(max_depth,self.max_depth(child))
            
        return max_depth + 1

    def depth(self):
        
        return self.max_depth(self.root)
        
        
        
        




tree = NArrayTree()

tree.add_child(10)
tree.add_child(20,10)
tree.add_child(30,20)
tree.add_child(40,20)
tree.add_child(50,20)
tree.add_child(60,30)
print(tree.depth())


        
        



  


