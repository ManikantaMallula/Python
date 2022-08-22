#7 write a program if the given input is leap year or not
year=eval(input("enter a year to find: "))
if (year%4==0 and year%100!=0 or year%400==0):
    print(year," is a leap year")
else:
    print(year,"  is a not leap year")