# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:38:22 2020

@author: PRANIKP

DEQueue: Doubly Ended Queue.
       
Here we have implemented using List. 
"""



class DeQueue:

	def __init__(self):
		self.data = []

	
	def __len__(self):
		return(len(self.data))


	def isEmpty(self):
		return(len(self.data) == 0)




	def add_first(self,val):
	
		self.data.insert(0,val)


	def add_last(self,val):
		self.data.append(val)


	def remove_first(self):
		if self.isEmpty():
			print("DEQue is Empty!!!")
			return


		self.data.pop(0)

	
	def remove_last(self):
		if self.isEmpty():
			print("DEQue is Empty!!!")
			return


		self.data.pop(-1)


	def first(self):
		if self.isEmpty():
			print("DEQue is Empty!!!")
			return

		return self.data[0]


	def last(self):
		if self.isEmpty():
			print("DEQue is Empty!!!")
			return


		return self.data[-1]




d = DeQueue()


d.add_last(20)
d.add_last(33)
d.add_first(98)
d.add_first(79)
d.add_last(92)
d.add_first(21)


print(d.data)


print(d.first())
print(d.last())


print()
print()

d.remove_first()
print(d.data)

d.remove_last()
print(d.data)

print()
print()



print(d.first())
print(d.last())


print()
print()



d.remove_last()
print(d.data)



d.remove_first()
print(d.data)


print()
print()



print(d.first())
print(d.last())