# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:38:22 2020

@author: PRANIKP

Queue: queue is a collection of entities that are maintained in a sequence and can 
       be modified by the addition of entities at one end of the sequence and the 
       removal of entities from the other end of the sequence.
       Works in FIFO (First In First Out).
       
Here we have implemented using List. 
"""



class Queue:

	def __init__(self):
		self.data = []


	def __len__(self):
		return(len(self.data))


	def isEmpty(self):
		return(len(self.data) == 0)

	

	def enqueue(self,val):
		self.data.append(val)


	def dequeue(self):
		return(self.data.pop(0))


	def first(self):
		return(self.data[0])



q = Queue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(78)
q.enqueue(98)
q.enqueue(23)
q.enqueue(57)


print(q.data)

print(q.first())

print()
print()

val = q.dequeue()
print(val)

print()

print(q.data)
print(q.first())

print()
print()

val = q.dequeue()
print(val)

print()

print(q.data)
print(q.first())


