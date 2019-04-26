# Python program for implementation of Selection Sort
# FROM: http://interactivepython.org/lpomz/courselib/static/pythonds/SortSearch/TheSelectionSort.html
import time
import random


def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp


test_list =[]   #create empty list


length = open('selection_sort_time.txt','w')



for x in range(10000): #add first 10k items to list
    test_list.append(random.randint(1,1000)) #random ints

total_time = 0 
while total_time < 60:
    start = time.time()
    selectionSort(test_list)
    total_time = float(format((time.time() - start),".3f"))
    sent = str((len(test_list),total_time))
    length.write(sent+"\n")
    if total_time < 60:
        for x in range(10000): #add first 10k items to list
            test_list.append(random.randint(1,1000)) #random ints
length.close()
