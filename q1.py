"""1. Day of the Week
Write a program that asks the user for a number in the range of 1 through 7. The program should display 
the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = 
Friday, 6 = Saturday, and 7 = Sunday. The program should display an error message if the user enters a 
number that is outside the range of 1 through 7."""

n=int(input("please enter integer number in the range of 1 through 7:"))
if(n==1):
    print("monday")
elif(n==2):
    print("tuesday")
elif(n==3):
    print("wednesday")
elif(n==4):
    print("thursday")
elif(n==5):
    print("friday")
elif(n==6):
    print("saturday")
elif(n==7):
    print("sunday")
else:
    print("you entered wrong information,try again")
