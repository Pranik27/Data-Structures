# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 02:12:35 2020

@author: PRANIKP

Circular Linked List: Circular Linked List is a variation of Linked list in which
                     the first element points to the last element and the 
                     last element points to the first element. 
                     Both Singly Linked List and Doubly Linked List can be made 
                     into a circular linked list.
"""

class Node:
    
    __slots__ = 'data','next'
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
    
class CircularLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
        
    def __len__(self):
        return (self.size)
    
    
    def isempty(self):
        return (self.size == 0)
    
    #Method ot create the list. [TIme Complx : O(1)]
    def insert(self,val):
        
        new_node = Node(val)
        
        if self.isempty():
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            
            
        self.tail = new_node
        self.size += 1
        
        
    #Method to display/traverse the list. [TIme Complx : O(n)]    
    def display(self):
        
        if self.isempty():
            print("List is empty!!!")
            return
        
        current_node = self.head
        index = 0
        
        while index < len(self):
            print(current_node.data, end = "-->")
            current_node = current_node.next
            index += 1
            
        print("None")
        
    #Method to add node at the fisrst pos. [TIme Complx : O(1)]   
    def add_first(self,val):
        
        if self.isempty():
            print("List is empty. calling insert method!!!")
            return
        
        new_node = Node(val)
        
        new_node.next = self.head
        self.head = new_node
        self.tail.next = new_node
        self.size += 1
        
        
    #Method to add at any pos in the list. [TIme Complx : O(n)]  
    def add_any(self,val,pos):
        
        if (pos == 1):
            print("Node needs to be added at head. Calling add_first method!!!")
            self.add_first(val)
            return
        
        new_node = Node(val)
        current_node = self.head
        index = 1
        
        while index < pos -1:
            current_node = current_node.next
            index += 1
            
        
        new_node.next = current_node.next
        current_node.next = new_node
        self.size += 1
        
            
        
    #Method to delete the first node. [Time Complx: O(1)]    
    def del_first(self):
        
        if self.isempty():
            print("List is empty!!!")
            return
        
        current_node = self.head
        val = current_node.data
        self.tail.next = current_node.next
        self.head = current_node.next
        self.size -= 1
        
        if self.isempty():
            self.tail = None
            
        return(val)
    
    #Method to delete at the end of the list. [Time Complx: O(n)]
    def del_last(self):
        
        if self.isempty():
            print("List is empty!!!")
            return
        
        current_node = self.head
        index = 0
        
        while index < len(self) - 1:
            current_node = current_node.next
            index += 1
            
            
        current_node.next = self.tail.next
        val = self.tail.data
        self.tail = current_node
        self.size -= 1
        
        return(val)
    
    #Method to delete from any pos from the list. [Time Complx : O(n)]
    def del_any(self,pos):
        
        if pos == 1:
            print("calling del_first method!!")
            val = self.del_first()
            return (val)
        elif pos == len(self):
            print("caliing del_last method")
            val = self.del_last()
            return (val)
        elif pos > len(self):
            print("Pos value greater than list lenght!!!")
            return
        
        current_list = self.head
        index = 1
        
        while index < pos - 1:
            current_list = current_list.next
            index += 1
            
        val = current_list.next.data
        current_list.next = current_list.next.next
        self.size -= 1
        
        return(val)
        
    


ll = CircularLinkedList()

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


print(ll.head)
print(ll.tail.next)