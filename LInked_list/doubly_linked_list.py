# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 23:27:08 2020

@author: PRANIKP

Doubly LIked List : A doubly linked list is a linked data structure that consists
                    of a set of sequentially linked records called nodes. 
                    Each node contains three fields: two link fields and one data field.
"""

class Node:
    
    __slots__ = 'data','next','prev'
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
        

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
        
    def __len__(self):
        return(self.size)
    
    def isempty(self):
        return (self.size == 0)
    
    
    def insert(self,val):
        
        new_node = Node(val)
        
        if self.isempty():
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            
        self.tail = new_node
        self.size += 1
        
    
    def display(self):
        
        if self.isempty():
            print("List is empty!!!")
            
        current_node = self.head
        
        while current_node:
            print(current_node.data , end = "-->")
            current_node = current_node.next
            
        print(None)
        
        
    def add_first(self,val):
        
        new_node = Node(val)
        
        
        if self.isempty():
            print("list is empty. calling the insert method!!!")
            self.insert(val)
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1
            
            
    def add_any(self,val,pos):
        
        new_node = Node(val)
        current_node = self.head
        index = 1
        
        while index < pos - 1:
            current_node = current_node.next
            index += 1
            
        new_node.next = current_node.next
        current_node.next.prev = new_node
        new_node.prev = current_node
        current_node.next = new_node
        self.size += 1
        
        
    def del_first(self):
        
        if self.isempty():
            print("List is empty!!!")
            return
        
        val = self.head.data
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        
        if self.isempty():
            self.tail = None
            
        return (val)
            
    
    def del_last(self):
        
        if self.isempty():
            print("list is empty!!")
            return
        
        val = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        
        return (val)
    
    
    def del_any(self,pos):
        
        if self.isempty():
            print("list is empty!!!")
            return
        elif pos == len(self):
            print("Calling del_last method!!!")
            val = self.del_last()
            return (val)
        
        current_node = self.head
        index = 1
        
        while index < pos - 1:
            current_node =  current_node.next
            index += 1
            
        val = current_node.next.data
        current_node.next = current_node.next.next
        current_node.next.prev = current_node
        self.size -= 1
        
        return(val)
        
            
        
        
        
        
ll = DoublyLinkedList()

ll.insert(5)
ll.insert(7)
ll.insert(11)
ll.insert(23)
ll.insert(27)


ll.display() 
print(len(ll)) 


ll.add_first(15)
ll.display()
print(len(ll)) 


ll.add_any(198, 5)
ll.display()
print(len(ll)) 

ll.add_any(128, 7)
ll.display()
print(len(ll)) 



f = ll.del_first()
ll.display()
print(f)
print(len(ll)) 

d = ll .del_last()
ll.display()
print(d)
print(len(ll)) 


a = ll.del_any(3)
ll.display()
print("delete : {}".format(a))
print(len(ll)) 


a = ll.del_any(5)
ll.display()
print("delete : {}".format(a))
print(len(ll)) 

print(ll.head.prev)
print(ll.tail.next)