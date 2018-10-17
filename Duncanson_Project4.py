#Stephen Duncanson
#Project 4

total_rainfall = 0       #total rainfall over the whole period (accumulator)
average_rainfall = 0     #average rainfall per month
YEAR = 12                #Year constant, used in nested loop to interate 12 times

#This list holds the months of the year
#jan in [0] to dec in [11]
#This is used to print the month
#the index of the correct month = for month in range(YEAR):
#jan at index [0] = 0, the first vaule of iteration for YEAR
monthsList = [
    " Jan"," feb"," mar",
    " apr"," may"," jun",
    " jul"," aug"," sep",
    " oct"," nov"," dec"
]

#Collect an int number of years from the user, keyboard input
#this is used as the range for the outer loop
years = int(input("How many years: "))

#Calculate total months, 12 months * amount of years = total months
total_months = years * 12

#outer loop, iterate once for every year in the range of years entered
for number_of_years in range(years):
    #inner loop, iterate 12 times, 0-11 from the YEAR constant
    for month in range(YEAR):
        #print the year, since this starts at 0, I add 1
        #print the month, this is cool, see comments above
        print("Year ",number_of_years +1,',', monthsList[month], sep='')
        #use an augmented opperator for the accumulator 
        total_rainfall += float(input("How many inches of rain fell: "))
    print()


#Calculate the average_rainfall by dividing the total rainfall over the total months
average_rainfall = total_rainfall / total_months

#print out the total months
print("Over a period of",total_months, "months:")

#print the total_rainfall (accumulator)
print(total_rainfall, "inches of rain fell in total.")

#print the average rainfall, using the format function so it's pretty
print("On average",format(average_rainfall, '.2f'), "inches of rain fell each month.")
