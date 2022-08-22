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

'''5.Python Program to Solve Quadratic Equation '''


'''
6.Python Program to Swap Two Variables '''

##a=int(input("enter number : "))
##b=int(input("enter number to swap: "))
##a,b=b,a
##print(a)
##print(b) 

'''7.Python Program to Convert Kilometres to Miles '''


##k=int(input("enter number of kilometers : "))
##m=k*1000
##print(m,"meters") 

''' 8.Python Program to Check Leap Year '''

##year=int(input("enter year to check: "))
##if (year%400!=0 and year%4==0 or year%100==0):
##    print("yes")
##else:
##    print("no")

''' 9.Python Program to Check Prime Number'''

##n=int(input("enter a number to find: "))
##if n>1:
##    for i in range(2,n):
##        if n%i==0:
##            print(n,"is not a prime number")
##            break
##    else:
##            print(n,"is a prime number")
##            
##else:
##    print(n,"is not a prime number")

''' 10.Python Program to Find the Factorial of a Number '''

##n=int(input("enter a number to find: "))
##fact=1
##for i in range(1,n+1):
##    fact=fact*i
##print(fact)
    
'''11.Python Program to Print the Fibonacci sequence '''

##def feb():
##    a,b=0,1
##    while True:
##        a=b
##        b=a+b
##        yield a
##f=feb()
##for x in f:
##    print(x)

'''12.Python Program to Check Armstrong Number '''

##n=int(input("enter a number to find: "))
##temp=n
##sum=0
##power=len(str(n))
##while n>0:
##    rem=n%10
##    print(rem)
##    sum=sum+rem**power
##    n=n//10
##    print(n)
##print(sum)
##if sum==temp:
##    print("is Armstrong Number")
##else:
##    print("is not an Armstrong Number")    


'''13.Python Program to Find Armstrong Number in an Interval '''

##start=int(input("enter starting range: "))
##end=int(input("enter end range: "))
##for i in range(start,end+1):
##    temp=i
##    sum=0
##    p=len(str(i))
##    while i>0:
##        rem=i%10
##        sum=sum+rem**p
##        i=i//10
##    if sum==temp:
##        print(temp,"Armstrong Number")
##    else:
##        print(temp,"not Armstrong Number")
        
'''14.Python Program to Find the Sum of Natural Numbers '''   

##n=int(input("enter a number to find: "))
##sum=0
##for i in range(1,n+1):
##    sum=sum+i
##    #print(i)
##print(sum)

'''15.Python Program to Find the Factors of a Number '''

##n=int(input("enter some number to find: "))
##l=[]
##for i in range(1,n+1):
##    if n%i==0:
##        l.append(i)
##print("the factors of",n,"is ",l)
        
'''16.Python Program to Convert Decimal to Binary, Octal and Hexadecimal '''

##dec=int(input("enter some number: "))
##print(bin(dec),"in binary")
##print(oct(dec),"in octal")
##print(hex(dec),"in Hexadecimal")

'''17.Python Program to Find LCM '''

a=float(input("enter a value: "))
b=float(input("enter b value: "))
if a>b:
    max=a
else:
    max=b
while True:
    if max%a==0 and max%b==0:
        print("lCM for {} and {} is {}".format(a,b,max))
        break
    max+=1x









    
