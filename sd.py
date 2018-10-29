#Stephen Duncanson
#Standard deviation
import math

total = 0
dataList = []
total_num = 0

def get_input():
    how_many = 0
    how_many = int(input("How many pieces of data: "))
    for i in range(how_many):
        data = float(input("Enter data point:"))
        dataList.append(data)

def sd():
    total = 0
    total_num = 0
    for i in dataList:
        total += i
        mean = total / len(dataList)
        
    for x in dataList:
        total_num += (x - mean)**2
        s = math.sqrt(total_num /(len(dataList) -1))
    print(format(s, '.2f'))
    
def main():
    get_input()
    sd()

main()
