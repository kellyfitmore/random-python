#Tree Sort
#FROM: https://www.tutorialspoint.com/python/python_binary_tree.htm

import time
import random

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

##################################    
test_list =[]   #create empty list
length = open('tree_sort_time.txt','w')


for x in range(10001): #add first 10k items to list
    test_list.append(random.randint(1,1000)) #random ints


total_time = 0 
while total_time < 10:
    start = time.time()
    root = Node(test_list.pop())
    for i in test_list:
        root.insert(i)
    total_time = float(format((time.time() - start),".3f"))
    if total_time < 10:
        sent = str((len(test_list),total_time))
        length.write(sent+"\n")
        #print("Tree Sort'ed a list of length ",len(test_list),"in", total_time, "seconds")
        for x in range(10001): #add first 10k items to list
            test_list.append(random.randint(1,1000)) #random ints

length.close()
            
        
    





