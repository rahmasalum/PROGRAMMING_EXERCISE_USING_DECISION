"""12. Shipping Charges
The Fast Freight Shipping Company charges the following rates:
Weight of Package Rate per Pound
2 pounds or less $1.10
Over 2 pounds but not more than 6 pounds $2.20
Over 6 pounds but not more than 10 pounds $3.70
Over 10 pounds $3.80
Write a program that asks the user to enter the weight of a package and then displays the shipping 
charges."""
w=float(input("please enter the weight of package rate per pound:"))
if(w>0 and w<=2):
    charge=w*1.10
    print("the shipping charge of the pound",w,"is $",charge)
elif(w>2 and w<=6):
s    charge=w*2.20
    print("the shipping charge of the pound",w,"is $",charge)
elif(w>6 and w<=10):
    charge=w*3.70
    print("the shipping charge of the pound",w,"is $",charge)
elif(w>10):
    charge=w*3.80
    print("the shipping charge of the pound",w,"is $",charge)
else:
    print("You entered wrong input,please try again")



