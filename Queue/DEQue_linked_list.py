# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:38:22 2020

@author: PRANIKP

DEQueue: Doubly Ended Queue.
       
Here we have implemented using Linked List. 
"""



class Node:

	def __init__(self,data):
		self.data = data
		self.next = None




class DEQueLinkedList:

	def __init__(self):
		self.front = None
		self.rear = None
		self.size = 0



	def __len__(self):
		return (self.size)

	def isEmpty(self):
		return (self.size == 0)



	def add_first(self,val):
		new_node = Node(val)


		if self.isEmpty():
			self.front = new_node
			self.rear = new_node
		else:
			new_node.next = self.front
			self.front = new_node

		self.size += 1



	def add_last(self,val):

		new_node = Node(val)

		if self.isEmpty():
			self.front = new_node
		else:
			self.rear.next = new_node
			
		self.rear = new_node
		self.size += 1




	def remove_first(self):
		
		if self.isEmpty():
			print("DEQue is empty!!!")
			return


		self.front = self.front.next
		self.size -= 1


		if self.isEmpty():
			self.rear = None




	def remove_last(self):
	
		if self.isEmpty():
			print("DEQue is empty!!!")
			return


		current_node = self.front
		next_node = self.front.next

		while next_node.next:

			next_node = next_node.next
			current_node = current_node.next



		print("Current Node Data: {}".format(current_node.data))
		self.rear = current_node
		current_node.next = None
		self.size -= 1



	def display(self):

		if self.isEmpty():
			print("DEQue is empty!!")
			return


		current_node = self.front
		while current_node:
			print(current_node.data,end = "-->")
			current_node = current_node.next


		print("None")



	def first(self):
		if self.isEmpty():
			print("DEQue is empty!!!")
			return


		return(self.front.data)


	def last(self):
		if self.isEmpty():
			print("DEQue is Empty!!!")
			return


		return(self.rear.data)






d = DEQueLinkedList()

d.add_last(20)
d.add_last(33)
d.add_first(98)
d.add_first(79)
d.add_last(92)
d.add_first(21)


d.display()


d.remove_last()
d.display()


d.remove_last()
d.display()

print()
print()

print(d.first())
print(d.last())



d.remove_first()
d.display()

d.remove_first()
d.display()


print()
print()

print(d.first())
print(d.last())
