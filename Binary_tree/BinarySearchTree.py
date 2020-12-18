# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:57:51 2020

@author: PRANIKP
"""

class Node:
    
    __slots__ = 'data','left','right'
    
    
    def __init__(self,data,left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
        
class BinarySearchTree:
    
    def __init__(self):
        
        self.root = None
        
        
    
    def insert(self,root,key):
        
        temp = None
        
        while root:
            temp = root
            if key == root.data:
                print("Key is already present!!!")
                return
            elif key < root.data:
                root = root.left
            elif key > root.data:
                root = root.right
        
        new_node = Node(key,None,None)
        
        if self.root:
            if key < temp.data:
                temp.left = new_node
            else:
                temp.right = new_node
        else:
            self.root = new_node
            
            
    def rinsert(self,root,key):
        
        if root:
            
            if key == root.data:
                print("Key already present!!!")
                return root
            elif key < root.data:
                root.left =  self.rinsert(root.left,key)
            elif key > root.data:
                root.right =  self.rinsert(root.right,key)
        else:
            new_node = Node(key,None,None)
            root = new_node
            
        return root
            
        
            
            
    
    def serach(self,root,key):
        
        while root:
            
            if key == root.data:
                print("Key found!!!")
                return
            elif key < root.data:
                root = root.left
            elif key > root.data:
                root = root.right
                
        print("Key does not exist in Binary Tree!!!")
        return
    
    
    def rsearch(self,root,key):

        
        if root:
            
            if key == root.data:
                print("Key is found!!!")
                return True
            elif key < root.data:
                return self.rsearch(root.left,key)
            elif key > root.data:
                return self.rsearch(root.right,key)
        else:
            return False
                

            
    
    def inorder(self,root):
        
        if root:
            
            self.inorder(root.left)
            print(root.data, end = " ")
            self.inorder(root.right)
            
            
        
    def deleteBinaryTree(self,root,key):
        
        if not root:
            return None
        elif key == root.data:
            if not root.left and not root.right:
                root = None
            elif not root.right:
                root = root.left
            elif not root.left:
                root = root.right
            else:
                temp = root.right
                while  temp.left:
                    temp = temp.left
                root.data = temp.data
                root.right = self.deleteBinaryTree(root.right, temp.data)
        elif key < root.data:
            root.left = self.deleteBinaryTree(root.left, key)
        elif key > root.data:
            root.right = self.deleteBinaryTree(root.right, key)
            
        return root
            
            
        
        
z = BinarySearchTree()

z.insert(z.root, 10)
z.insert(z.root, 20)
z.insert(z.root, 30)
z.insert(z.root, 15)
z.rinsert(z.root, 97)
z.rinsert(z.root, 1234)
z.rinsert(z.root, 1)
z.rinsert(z.root, 73)



z.inorder(z.root)

print()
print()

del_root = z.deleteBinaryTree(z.root, 97)

print()
print()

z.inorder(z.root)

