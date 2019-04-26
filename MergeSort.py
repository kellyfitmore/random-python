# Python program for implementation of MergeSort
# FROM https://www.geeksforgeeks.org/merge-sort/

import time
import random

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  


#Time loop!
test_list =[]   #create empty list


length = open('Merge_sort_time.txt','w')


for x in range(10000): #add first 10k items to list
    test_list.append(random.randint(1,1000)) #random ints

total_time = 0 
while total_time < 10:
    start = time.time()
    mergeSort(test_list)
    total_time = float(format((time.time() - start),".3f"))
    sent = str((len(test_list),total_time))
    length.write(sent+"\n")
    if total_time < 10:
        for x in range(10000): #add first 10k items to list
            test_list.append(random.randint(1,1000)) #random ints
length.close()
