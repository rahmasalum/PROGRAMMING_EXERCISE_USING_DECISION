"""14. Time Calculator
Write a program that asks the user to enter a number of seconds, and works as follows:
• There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal 
to 60, the program should display the number of minutes in that many seconds.
• There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or 
equal to 3,600, the program should display the number of hours in that many seconds.
• There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal 
to 86,400, the program should display the number of days in that many seconds."""
try:
    sec=float(input("please enter a number of seconds:"))
    m=sec/60
    hrs=sec/3600
    d=sec/86400
    if(sec>=86400):
        print(f"There are {d} days in seconds {sec}")
    elif(sec>=3600):
        print(f"There are {hrs} hours in seconds {sec}")
    elif(sec>=60):
        print(f"There are {m} minutes in seconds {sec}")
    elif(sec>=0):
        print(f"There are {sec} seconds")
    else:
        print("You entered wrong input,please try again")
except ValueError:
    print("You entered wrong input,please try again")
          
