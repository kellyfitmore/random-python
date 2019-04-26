import time
import random

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


test_list =[]   #create empty list

length = open('bubble_sort_time.txt','w')

for x in range(10000): #add first 10k items to list
    test_list.append(random.randint(1,1000)) #random ints

total_time = 0 
while total_time < 60:
    start = time.time()
    bubbleSort(test_list)
    total_time = float(format((time.time() - start),".3f"))
    sent = str((len(test_list),total_time))
    length.write(sent+"\n")
    if total_time < 60:
        for x in range(10000): #add first 10k items to list
            test_list.append(random.randint(1,1000)) #random ints
length.close()
