#Plotting using Mathplotlib with pyplot

import matplotlib.pyplot as plt
#REMEMBER there is no H in matplotlib

#Linear Plot - Example from Matplotlib  Pyplot tutorial
#https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

plt.plot([1, 2, 3, 4])
#Above you are plotting the y values 1, 2, 3, 4
#I have not provided x values, so it's defaulted to the index of each number ie. position in list
#So x = [0, 1, 2, 3]
plt.ylabel('some numbers')
plt.show()


plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 19])
#Passing two lists through will set the first list as x values, and the second as y
plt.ylabel('Squares')
plt.show()
#The plot will join the coordinates with a straight line rather than a curve required for an exponential


plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 19], 'b.')
#Use shorthand 'b.' to specify that you want blue dots only, and no line between them
plt.ylabel('Squares')
plt.show()