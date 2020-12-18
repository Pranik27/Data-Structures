# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:19:14 2020

@author: PRANIKP

STACK : A stack is an abstract data type that serves as a collection of elements, 
        with two main principal operations: Push, which adds an element to the collection,
        and Pop, which removes the most recently added element that was not yet removed.
        Works on LIFO [Last in First Out].

Here , we have implemented stack using List.
        
"""

class stackList:
    
    def __init__(self):
        self.data = []
        
        
    def __len__(self):
        return (len(self.data))
    
    
    def isempty(self):
        return(len(self.data) == 0)
    
    
    def push(self,val):
        
        self.data.append(val)
        
        
    def pop(self):
        
        if self.isempty():
            print("Stack is empty!!!")
            return
        
        
        return(self.data.pop(-1))
    
    def top(self):
        
        if self.isempty():
            print("Stack is empty!!!!")
            return
        
        return(self.data[-1])
    
            
            
    

s = stackList()


s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print(s.data)
x = s.top()
y = s.pop()
print("At top: {}".format(x))
print("Element popped: {}".format(y))
x = s.top()
print("At top: {}".format(x))