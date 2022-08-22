'''
1.Write a program to find sum of number.  '''

##n=int(input("enter num to find sum: "))
##sum=0
##temp=n
##while n>0:
##    r=n%10
##    sum=sum+r
##    n=n//10
##print(sum)
##    

'''
2.WAP to find the number is strong number or not '''

##n=int(input("enter number to find: "))
##sum=0
##temp=n
##while n>0:
##    r=n%10
##    fact=1
##    for i in range(1,r+1):
##        fact=fact*i
##    sum+=fact
##    n=n//10
##if temp==sum:
##    print("yes")
##else:
##    print("no") 
    
'''
3.Python Program to Find the Square Root  '''

##n=int(input("enter a num to find square root: "))
##op=n**0.5
##print(op) 

'''
4.Python Program to Calculate the Area of a Triangle '''

##b=int(input("enter base: "))
##h=int(input("enter height: "))
##area=0.5*b*h
##print(area) 

'''
5.Python Program to Solve Quadratic Equation  '''

##a=int(input("enter number : "))
##b=int(input("enter number to swap: "))
##a,b=b,a
##print(a)
##print(b) 

'''
6.Python Program to Swap Two Variables '''

##k=int(input("enter number of kilometers : "))
##m=k*1000
##print(m,"meters") 

year=int(input("enter year to check: "))
if (year%400==0 or year%4==0 and year%100==0):
    print("yes")
else:
    print("no")
