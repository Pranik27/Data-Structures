# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:38:22 2020

@author: PRANIKP

Binary Search : It is a search algorithm that finds the position of a target value 
                within a sorted array.

Time Complexity: O(logn)
Space Complexity: O(1) [Constant space]
"""


def binary_search(inp_list,key):
	
	length = len(inp_list)
	left_pos = 0
	right_pos = length - 1
	
	while left_pos <= right_pos:
		mid = (left_pos + right_pos)//2
		if key > inp_list[mid]:
			left_pos = mid + 1
		elif key < inp_list[mid]:
			right_pos = mid - 1
		elif key == inp_list[mid]:
			print("Key Found")
			return
	
	print("Key not found")
	return 
		


inp_list = [10,20,40,75,99,123,200]
binary_search(inp_list,99)