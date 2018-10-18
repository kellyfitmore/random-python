#Stephen Duncanson
#This program finds the greatest common factor of two integers

#[0] is larger number, [1] is smaller number
#0 % 1 = remainder
#When remainder = 0, [1] = gcf
numbers = [0,0]

numbers[0] = int(input("Enter the larger number: "))
numbers[1] = int(input("Enter the smaller number: "))

remainder = numbers[0] % numbers[1]


while remainder != 0:
    numbers[0] = numbers[1]
    numbers[1] = remainder
    remainder = numbers[0] % numbers[1]


print("The gcf is", numbers[1])


#ANOTHER SOLUTION Break up facotes into list and use a for loop, for facrots in list if
#in other factors list then gcf?



