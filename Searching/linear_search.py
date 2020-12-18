# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:38:22 2020

@author: PRANIKP

Linear search : In computer science, a linear search or sequential search is a 
                method for finding an element within a list.

Time Complexity: O(n) , where n is the number of elements in the list.
Space Complexity: O(1) [constant Space]
"""


def linear_search(inp_list,key):
	length = len(inp_list)
	
	for index in range(length):
		if key == inp_list[index]:
			print("Key found!!!")
			return
		
	print("Key not found")
	return -1


inp_list = [10,20,40,75,99,123,200]
linear_search(inp_list,200) 
	