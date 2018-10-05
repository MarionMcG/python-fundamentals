#Demos and notes from Week 1 of Python Fundamentals 
#Reviewing the basics

#Is it Tuesday?? (Review of IF Statements)
import datetime
print()
print("Is it Tuesday???")
today = datetime.datetime.today()
dayofweek = today.weekday()
print ('Today = ',today)
print ('Day of Week =', dayofweek)
#If the day of the week equals 1, then its Tuesday as datetime  
#sets days as number 0 - 6 , with Monday been the first day = 0
if dayofweek == 1:
    print("It's Tuesday!")
elif dayofweek == 0:
    print("It's not Tuesday....")
    print("Luckily it will be Tuesday Tomorrow!")
else:
    print("Sorry, it's not Tueday")

print()

#Highest common factor (Review of WHILE Loops)
print('Highest Common Factor')
a = 50 
b = 20 

while b > 0:
    #Set a = temp value that can be overwritten using this format.
    #IN PYTHON: a, b are the old values on the LHS and they are overwritten by new values.
    #On the RHS new values, are b and a modulo b
    a, b = b, a%b
print(a, 'is the HCF of 20 and 50')

print()


#Listing the first 10 square numbers (Review of FOR Loops)
#Used to iterate through a list, so you always need to begin with a list!
print("The first 11 Square numbers")
for i in range(11):
    #range (10) is same as list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"{i:2} {i*i:4}")
    print()

#Highest Common Factor ..again(Review of FUNCTIONS)
def hcf (a, b):
    """ Returns the Highest Common Factor of a, b
    """
    if a<b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

print ("The HCF of 20 and 50 is", hcf (20, 50))

print("The HCF of 143 and 22 is", hcf (143, 22))
print()