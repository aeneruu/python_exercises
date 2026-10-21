##f to c convetrpt
# f=int(input("Enter temp in F:"))
# c = (f -32)*(5/9)
# print(c)

##m to km
# m=float(input("Enter distance in m:"))
# km=m*1.6
# print(km)

## c convert to f
# c=int(input("Enter temp in C:"))
# f = c*(9/5)+32
# print(f)

##counting apples
# budget=int(input("Please enter your budget: "))
# cost=3
# apples=budget//cost
# print(f"You may afford {apples} apples.")
# next_apple=3-budget%cost
#remainder=budget%cost
#print(f"You have {remainder} money left.")
# print(f"You need {next_apple} euros to afford another apple.")

##radius of a circle
# import math
# r=float(input("Input the radius of the circle:"))
# a=math.pi*r**2
# print(a)

##volume of a cylinder
# import math
# r=float(input("Input the radius of the circle:"))
# h=float(input("Input the height of the cylinder:"))
# v=math.pi*r**2*h
# print(v)

##electricity bill
# units=float(input("Please enter your units: "))
# price=0.0
# total_price=0.0
# surcharge=0.0
# if units<=50:
#     price=units*0.50
#     total_price=price
#     surcharge=0.0
# elif 50<units<=150:
#     price=0.50*50+(units-50)*0.75
#     total_price=price
#     surcharge=0.0
# elif 150<units<=250:
#     price=0.50*50+100*0.75+(units-150)*1.20
#     total_price=price
#     surcharge=0.0
# elif 250<units:
#     price=0.50*50+100*0.75+100*1.20+(units-250)*1.50
#     surcharge = 0.1 * price
#     total_price=price+surcharge
# print(f"Price is {price}, surcharge is {surcharge}, total price is {total_price}.")

##min of three
# num1=input("Please enter your first number: ")
# num2=input("Please enter your second number: ")
# num3=input("Please enter your third number: ")
# if num1<num2 and num2<num3:
#     print("The first integer is the minimum.")
# elif num2<num1 and num2<num3:
#     print("The second integer is the minimum.")
# elif num3<num2 and num3<num1:
#     print("The third integer is the minimum.")

year=int(input("Enter year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")