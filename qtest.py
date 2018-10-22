#Stephen Duncanson
#The q-test


qtest_pass = []
qtest_fail = []
rejection_quotient = [.376, .392, .412, .437, .468, .507, .560, .642, .765, .941]
q = 0

#logical error, closest != index +1 when decending?
percentList = [163, 59.6, 55, 53.4, 52.9, 50, 49.9, 46.6, 41.2, 41.2, 41.1, 38.7]

for a in percentList:
    index = percentList.index(a)
    if index + 1 < len(percentList):
        nearest = index + 1
    elif index +1 >= len(percentList):
        nearest = index -1

    #actual q test calculation
    numerator = abs(a - percentList[nearest]) 
    denominator = abs(percentList[0] - percentList[-1])
    q = (numerator / denominator)

    print()
    print("\tQ-Test")
    print("(",a," - ", percentList[nearest],") / (",percentList[0], " - ", percentList[-1],")", sep='')
    print("Q = ",format(q, ".3f"))
    print("Since there are", len(percentList),"observations, the Rejection quotient is", rejection_quotient[0])

    
    if q > rejection_quotient[0]:
        print("Since", format(q, ".3f"), ">", rejection_quotient[0])
        print(a, "fails the Qtest!")
        qtest_fail.append(a)
        percentList.remove(a)
        del rejection_quotient[0]
        #remove a and add to qtestfail also remove rejection_q[0], this way they both move down stepwise together! 
    else:
        qtest_pass.append(a)
        print("Since", format(q, ".3f"), "<", rejection_quotient[0])
        print(a, "passes the Qtest!")

    print("Press enter to test the next number:",end='')
    input()
    
print("These values fail the qtest!")
print(qtest_fail)
print("These values pass the qtest!")
print(qtest_pass)
    
