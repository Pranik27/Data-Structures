# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:58:32 2020

@author: PRANIKP
"""
from QueueLinkedList import QueueLinkedList

class Node:
    
    __slots__ = 'element','left','right'
    
    def __init__(self,element,left = None,right = None):
        self.element = element
        self.left = left
        self.right = right
        
        

class BinaryTree:
    
    def __init__(self):
        
        self.troot = None
        
        
    
    def maketree(self,element,left,right):
        self.troot = Node(element,left,right)
        
        
    def preorder(self,troot):
        
        if troot:
            print(troot.element , end = " ")
            self.preorder(troot.left)
            self.preorder(troot.right)
            
            
    def inorder(self,troot):
        
        if troot:
            self.inorder(troot.left)
            print(troot.element, end = " ")
            self.inorder(troot.right)
            
            
    
    def postorder(self,troot):
        
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.element, end = " ")
            
            
            
    
    def count(self,troot):
        
        if troot:
            
            x = self.count(troot.left)
            y = self.count(troot.right)
            return (x + y +1)
        
        return 0
    
    
    def height(self,troot):
        
        if troot:
            
            x = self.height(troot.left)
            y = self.height(troot.right)
            if x > y:
                return x + 1
            else:
                return y + 1
            
            
        return 0
    
    
    def levelorder(self,root):
        
        temp_queue = QueueLinkedList()
        troot = root
        
        print(troot.element, end = " ")
        temp_queue.enqueue(troot)
        
        while not temp_queue.isemprty():
            temp_root = temp_queue.dequeue()
            
            if temp_root.left:
                print(temp_root.left.element, end = " ")
                temp_queue.enqueue(temp_root.left)
                
            if temp_root.right:
                print(temp_root.right.element, end = " ")
                temp_queue.enqueue(temp_root.right)
                
                
            
            
            
            
            
    

            
    

x = BinaryTree()
y = BinaryTree()
z = BinaryTree()  #Root node
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()



r.maketree(40,None,None)
s.maketree(50,None,None)
t.maketree(70, None, None)
x.maketree(20, r.troot,s.troot)
y.maketree(30, None,t.troot)
z.maketree(10, x.troot,y.troot)


print("Inorder Traversal!!")
z.inorder(z.troot)
print()

print("Preorder Traversal!!!")
z.preorder(z.troot)
print()

print("Postorder traversal!!!")
z.postorder(z.troot)
print()

        
print("No of nodes : {}".format(z.count(z.troot)))   
print("height of the Tree: {}".format(z.height(z.troot) -  1))
z.levelorder(z.troot)