# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:38:22 2020

@author: PRANIKP

Binary Search : It is a search algorithm that finds the position of a target value 
                within a sorted array.

Time Complexity: O(logn)
Space Complexity: O(1) [Constant space] , if we don't consider the internal stack .

"""

def rbinary_search(inp_list,key,left,right):
	if left > right:
		print("key not found")
	else:
		mid = (left + right)//2
		if key == inp_list[mid]:
			print("Key found")
			return True
		elif key > inp_list[mid]:
			left = mid + 1
			rbinary_search(inp_list,key,left,right)
		elif key < inp_list[mid]:
			right = mid - 1
			rbinary_search(inp_list,key,left,right)



inp_list = [10,20,40,75,99,123,200]
left = 0
right = len(inp_list) - 1
rbinary_search(inp_list,10,left,right)
	