# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 01:12:19 2020

@author: PRANIKP

Linked List: A  linked list is a linear collection of data elements whose order 
            is not given by their physical placement in memory. 
            Instead, each element points to the next. It is a data structure consisting 
            of a collection of nodes which together represent a sequence.
            
"""

class Node:
    
    __slot__ = 'data','next'
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
        

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
        
    def __len__(self):
        return (self.size)
    
    def isempty(self):
        return (self.size == 0)
    
    #Method to create the list. [Time Complx : O(1)]
    def insert(self,val):
        
        new_node = Node(val)
        
        if self.isempty():
            self.head = new_node
        else:
            self.tail.next = new_node
            
        self.tail = new_node
        self.size += 1
        
    #Mehod to display/traverse a list. [Time Complx: O(n)]    
    def display(self):
        
        if self.isempty():
            print("List is empty!!!")
            return
        
        current_list = self.head
        
        while current_list:
            print(current_list.data, end = "-->")
            current_list = current_list.next
            
        print("None")
        
    #Method to add node as the first node. [Time Complx : O(1)]  
    def add_first(self,val):
        
        if self.isempty():
            print("List is empty. calling the insert method!!!")
            self.insert(val)
            return
        
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
        
    #Method to add node at any pos in the list . [TIme Complx : O(n)]    
    def add_any(self,val,pos):
        
        if pos == 1:
            print("The node is to be inserted at the beginning. Calling the add_first methd!!")
            self.add_first(val)
            return
        elif pos > self.size:
            print("The input pos is greater than the list size.!!")
            return
        
        new_node = Node(val)
        current_node = self.head
        index = 1
        
        while index < pos - 1:
            current_node = current_node.next
            index += 1
            
        new_node.next = current_node.next 
        current_node.next = new_node
        self.size += 1
        
        
    #Method to delete the first node. [Time Complx : O(1)]  
    def del_first(self):
        
        if self.isempty():
            print("list is empty!!!")
            return
        
        current_node  = self.head
        val = current_node.data
        self.head = current_node.next
        self.size -= 1
        
        if self.isempty():
            self.tail = None
            
        return(val)
    
    #Method to delete at the last of the list. [Time Complx : O(n)]
    def del_last(self):
        
        if self.isempty():
            print("list is empty!!!")
            return
        
        current_node = self.head
        index = 1
        
        while index < len(self) - 1:
            current_node = current_node.next
            index += 1
        
        val = self.tail.data
        self.tail = current_node
        current_node.next = None
        self.size -= 1
        
        return(val)
    
    
    #Method to del from any pos in the list. [Time Complx : O(n)]
    def del_any(self,pos):
        
        if self.isempty():
            print("List is empty!!")
            return
        
        current_node = self.head
        index = 1
        
        while index < pos - 1:
            current_node = current_node.next
            index += 1
            
        val = current_node.next.data
        current_node.next = current_node.next.next
        self.size -= 1
        
        return(val)
        
        
            
        
        

ll = LinkedList()

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