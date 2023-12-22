"""11. Software Sales
A software company sells a package that retails for $99. Quantity discounts are given according to the 
following table:
Quantity    Discount
10–19       20%
20–49       30%
50–99       40%
100 or more 50%
Write a program that asks the user to enter the number of packages purchased. The program should then 
display the amount of the discount (if any) and the total amount of the purchase after the discount."""
q=int(input("please enter the number of packages purchased:"))
pb=q*99
if(q>=10 and q<=19):
    d=q*pb*20/100
    pd=pb-d
    print(f"""
Quantity  puchase before  discount  purchase after  
             discount                   discount
 {q}          {pb}          {d}          {pd}

""")
elif(q>=20 and q<=49):
    d=q*pb*30/100
    pd=pb-d
    print(f"""
Quantity  puchase before  discount  purchase after  
             discount                   discount
 {q}          {pb}          {d}          {pd}

""")
elif(q>=50 and q<=99):
    d=q*pb*40/100
    pd=pb-d
    print(f"""
Quantity  puchase before  discount  purchase after  
             discount                   discount
 {q}          {pb}          {d}          {pd}

""")
elif(q>=100):
    d=q*pb*50/100
    pd=pb-d
    print(f"""
Quantity  puchase before  discount  purchase after  
             discount                   discount
 {q}          {pb}          {d}          {pd}

""")
else:
    print("You enter wrong input,please try again")
