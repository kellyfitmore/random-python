import matplotlib.pyplot as plt


#FIRST VALUES
#THEORETICAL
#Moles of Mg
x2 = [.003,.004,.005,.005,.006,.007]
# corresponding y axis values
y2 = [67.2,89.6,112,112,112,112]

# x axis values
#Moles of HCl
x = [.003,.004,.0045,.0053,.006,.007]
# corresponding y axis values
y = [60,85,90,95,100,120]

# plotting the points
plt.plot(x, y, color='blue', linestyle='solid', linewidth = 2,
         marker='o', markerfacecolor='blue', markersize=5)


#plt.plot(x2,y2, color='grey', linestyle='dashed', linewidth = 1,
#         marker ='o', markerfacecolor='grey', markersize=5)


plt.legend(['Experimental value', 'Theoretical value'])



# setting x and y axis range
plt.xlim(.000,.010)
plt.ylim(0,130)

# naming the x axis
plt.xlabel('Moles of Mg')
# naming the y axis
plt.ylabel('Volume of Hydrogen gas (mL)')

# giving a title to my graph
plt.title('Group B - Fixed Volume of HCl \n First Recorded Values')

# function to show the plot
plt.show()
