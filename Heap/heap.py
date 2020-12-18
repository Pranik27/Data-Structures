# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:55:12 2020

@author: PRANIKP

Heap: Heap is a specialized tree-based data structure which is essentially an almost 
      complete tree that satisfies the heap property.
      
Please Note: Here we have implemented Max heap from the scratch.
             Where as for Min heap we have used exisintg Python package/library "heapq"
"""
import heapq as heap

class Heap:
    
    def __init__(self):
        
        self.maxsize = 10
        self.data = [-1] * self.maxsize
        self.csize = 0
        
        
    
    def isempty(self):
        return(self.csize == 0)
    
    
    def insert(self,val):
        
        if self.csize == self.maxsize:
            print("Heap is full!!!")
            return
        
        self.csize += 1
        heap_index = self.csize
        
        while heap_index >1 and val > self.data[heap_index//2]:
            
            self.data[heap_index] = self.data[heap_index//2]
            heap_index = heap_index//2
        
        
        self.data[heap_index] = val
        
        
        def max(self):
            if self.isempty():
                print("HEap is empty!!")
                return
            return(self.data[1])
        
        
        
    def delete_max(self):
            
        val = self.data[1]
        self.data[1] = self.data[self.csize]
        self.data[self.csize] = -1
        self.csize -= 1
            
        i = 1 
        j = i*2
        while j < self.csize:
            
            
            if self.data[j] < self.data[j+1]:
                j = j +1
            if self.data[i] < self.data[j]:
                temp = self.data[i]
                self.data[i] = self.data[j]
                self.data[j] = temp
                    
            i = j
            j = i*2
                
                
        return val
    
    
    def heapsort(self,data):
        
        heap.heapify(data)
        
        n = len(data)
        sorted_heap =[-1]* n
        
        for index in range(n):
            sorted_heap[index] = heap.heappop(data)
        return(sorted_heap)
    
    
    def heapsort_max(self,data):
        
        n = len(data)
        print("Value of n:{}".format(n))
        
        for index in range(n):
            self.insert(data[index])
            
        k = n -1
        for index in range(self.csize):
            data[k] = H.delete_max()
            k = k -1
        
        
        return(data)
            
            


H = Heap()

A = [63,250,835,947,651,28]
out_list = H.heapsort_max(A)
print (out_list)


H.insert(25)
H.insert(14)
H.insert(2)
H.insert(20)
H.insert(10)


print(H.data)

H.insert(40)
print(H.data)

val = H.delete_max()
print(val)
print(H.data)

val = H.delete_max()
print(val)
print(H.data)



print()
print()


'''
From here Onwards we have min heap usage!!!!
'''


print("Min Heap implementation!!!")

data = []
heap.heappush(data,25)
heap.heappush(data,14)
heap.heappush(data,2)
heap.heappush(data,20)
heap.heappush(data,10)

print(data)

out = heap.heappop(data)
print(out)
print(data)

out = heap.heappushpop(data,1)
print(out)
print(data)

out = heap.heapreplace(data, 8)
print(out)

print(data)

print(heap.nsmallest(2, data))
print(heap.nlargest(2, data))


A = [63,250,835,947,651,28]
out_list = H.heapsort(A)
print (out_list)
