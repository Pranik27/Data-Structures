# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:38:22 2020

@author: PRANIKP

Queue: queue is a collection of entities that are maintained in a sequence and can 
       be modified by the addition of entities at one end of the sequence and the 
       removal of entities from the other end of the sequence.
       Works in FIFO (First In First Out).
       
Here we have implemented using Linked List. 
"""


class Node:

	def __init__(self,data):
		self.data = data
		self.next = None



class QueueLinkedList:

	def __init__(self):
		self.front = None
		self.rear = None
		self.size = 0


	def __len__(self):
		return(self.size)


	def isEmpty(self):
		return(self.size == 0)


	def enqueue(self,val):

		new_node = Node(val)

		if self.isEmpty():
			self.front = new_node
		else:
			self.rear.next = new_node
		
		self.rear = new_node
		self.size += 1


	def display(self):
		if self.isEmpty():
			print("Queue is empty!!")
			return

		current_node = self.front

		while current_node:
			print(current_node.data, end = "-->")
			current_node = current_node.next


		print("None")


	def dequeue(self):

		if self.isEmpty():
			print("Queue is Empty!!")
			return

		val = self.front.data
		self.front = self.front.next
		self.size -+ 1

		if self.isEmpty():
			self.rear = None


		return(val)


	def first(self):

		if self.isEmpty():
			print("Queue is empty!!")
			return


		return(self.front.data)


q = QueueLinkedList()

q.enqueue(20)
q.enqueue(30)
q.enqueue(78)
q.enqueue(98)
q.enqueue(23)
q.enqueue(57)

q.display()

print(q.first())

print()
print()


val = q.dequeue()
print(val)

print()
print()
q.display()
print(q.first())

print()
print()


val = q.dequeue()
print(val)

print()
print()

q.display()
print(q.first())


		 