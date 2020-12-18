# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:43:48 2020

@author: PRANIKP

STACK : A stack is an abstract data type that serves as a collection of elements, 
        with two main principal operations: Push, which adds an element to the collection,
        and Pop, which removes the most recently added element that was not yet removed.
        Works on LIFO [Last in First Out].

Here , we have implemented stack using Linked List.
        
"""

class Node:
    
    __slots__ = 'data','next'
    
    def __init__(self,data):
        
        self.data = data
        self.next = None
        
        

class StackLinkedList:
    
    def __init__(self):
        
        self.head = None
        self.size = 0
        
        
        
    def __len__(self):
        
        return(self.size)
    
    def isempty(self):
        
        return (self.size == 0)
    
    
    def push(self,val):
        
        new_node = Node(val)
        
        if self.isempty():
            pass
        else:
            new_node.next = self.head
            
        self.head = new_node
        self.size += 1
        
        
    def display(self):
        
        if self.isempty():
            print("Stack is empty!!!")
            return
        
        current_node = self.head
        
        while current_node:
            
            print(current_node.data , end = "-->")
            current_node = current_node.next
            
        print("None")
        
        
    def pop(self):
        
        if self.isempty():
            print("stack is empty!!!")
            return
        
        val = self.head.data
        self.head = self.head.next
        
        return (val)
    
    
    def top(self):
        
        if self.isempty():
            print("Stack is empty!!!!")
            return
        
        return(self.head.data)





s = StackLinkedList()


s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
            
            
s.display()

x = s.top()
y = s.pop()
print("At top: {}".format(x))
print("Element popped: {}".format(y))
x = s.top()
print("At top: {}".format(x))


s.display()
        
            
        
        
    