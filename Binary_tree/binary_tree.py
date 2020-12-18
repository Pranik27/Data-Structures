# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 23:19:25 2020

@author: PRANIKP
"""

class Node:
    
    __slots__ = 'data','left','right'
    
    def __init__(self,data,left= None,right = None):
        self.data = data
        self.left = left
        self.right = right
        
        
        
class binayTree:
    
    def __init__(self):
        self.root = None
        
        
    def maketree(self,data,left,right):
        self.root = Node(data,left,right)
        
    def inorder(self,troot):
        
        if troot:
            self.inorder(troot.left)
            print(troot.data, end = " ")
            self.inorder(troot.right)
            
            
    def preorder(self,troot):
        
        if troot:
            print(troot.data , end = " ")
            self.preorder(troot.left)
            self.preorder(troot.right)
            
        
    def postorder(self,troot):
        
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.data , end = " ")
            
            
    def count(self,troot):
        
        if troot:
            
            x = self.count(troot.left)
            y = self.count(troot.right)
            
            return (x+y+1)
        
        return 0
            
            
    def height(self,troot):
        
        if troot:
            
            x = self.height(troot.left)
            y = self.height(troot.right)
            
            if x > y :
                return x + 1
            else:
                return y + 1
            
        return 0
    
            
            

x = binayTree()
y = binayTree()
z = binayTree()  #Root node
r = binayTree()
s = binayTree()
t = binayTree()



r.maketree(40,None,None)
s.maketree(50,None,None)
t.maketree(70,None,None)
x.maketree(20,r.root,s.root)
y.maketree(30,None,t.root)
z.maketree(10, x.root , y.root)

print("Inorder Traversal!!")
z.inorder(z.root)
print()

print("Preorder Traversal!!!")
z.preorder(z.root)
print()

print("Postorder traversal!!!")
z.postorder(z.root)
print()

print("No of nodes : {}".format(z.count(z.root)))
print("height of the Tree: {}".format(z.height(z.root) -  1))