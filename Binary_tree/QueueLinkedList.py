# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 19:07:02 2020

@author: PRANIKP
"""

class Node:
    
    __slots__ = 'data','next'
    
    def __init__(self,data):
        
        self.data = data
        self.next = None
        
        


class QueueLinkedList:
    
    def __init__(self):
        
        self.head = None
        self.size = 0
        self.tail = None
        
        
    def __len__(self):
        
        return(self.size)
    
    def isemprty(self):
        return(self.size == 0)
    
    
    def enqueue(self,val):
        
        new_node = Node(val)
        
        if self.isemprty():
            self.head = new_node
        else:
            self.tail.next = new_node
            
        self.tail = new_node
        self.size += 1
        
        
        
    def diaplay(self):
        
        if self.isemprty():
            print("Queue is empty!!!")
            return
        
        current_node = self.head
        
        while current_node:
            print(current_node.data, end = "-->")
            current_node = current_node.next
            
        
        print("None")
        
        
    def dequeue(self):
        
        if self.isemprty():
            print("Queue is empty!!!")
            return
        
        
        val = self.head.data
        self.head = self.head.next
        self.size -= 1
        
        
        if self.isemprty():
            self.tail = None
            
            
        return(val)
    
    
    def first(self):
        
        if self.isemprty():
            print("Queue is empty!!!")
            return
        
        
        return(self.head.data)
        
        
        
        
        
s = QueueLinkedList()


s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
s.enqueue(40)
s.enqueue(50)

s.diaplay()
x = s.first()
y = s.dequeue()
print("At top: {}".format(x))
print("Element popped: {}".format(y))
x = s.first()
print("At top: {}".format(x))

s.diaplay()
            