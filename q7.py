"""7. Magic Dates
The date June 10, 1960, is special because when it is written in the following format, the month times the 
day equals the year: 6/10/60
Design a program that asks the user to enter a month (in numeric form), a day, and a two digit year. The 
program should then determine whether the month times the day equals the year. If so, it should display 
a message saying the date is magic. Otherwise, it should display a message saying the date is not magic."""
month=int(input("please enter a month in numeric form:"))
day=int(input("please enter a day:"))
year=int(input("please enter a two digit year:"))
magic=month*day
if(magic==year):
    print("Date",month,"/",day,"/",year,"the date is magic")
else:
    print("Date",month,"/",day,"/",year,"the date is not magic")
