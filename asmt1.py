''' 1. Write a program to swap given two numbers without temporary variable. '''

##a=int(input("enter a value: "))
##b=int(input("enter b value: "))
##print("before swap: ",a,b)
##a,b=b,a
##print("after swap: ",a,b)

''' output:
before swap:  10 20
after swap:  20 10 '''

##############################################################################################################

''' 2. Write a program to accept 4 numbers from command prompt add them using two variables. '''

##a=int(input("enter a value: "))
##b=int(input("enter b value: "))
##c=int(input("enter c value: "))
##d=int(input("enter d value: "))
##
##x=a+b
##y=c+b
##print("addition of 4 values using 2 variables: ",x+y)
    
''' output:
enter a value: 10
enter b value: 20
enter c value: 30
enter d value: 40
addition of 4 values using 2 variables:  80  '''

##############################################################################################################


''' 3. Write a program which accepts an int values as command line argument and    print the next multiple of 100.
    Ex: Input: 35
    Output: 100
    Input: 435
    Output: 500 '''

##n=int(input("enter a number to find next multiple of 100: "))
##a=100
##while True:
##    if n<a:
##        print(a)
##        break
##    else:
##        a=a+100
        
''' enter a number to find next multiple of 100: 435
500
enter a number to find next multiple of 100: 35
100 '''


''' 4. Write a program ThreeDPalindrome '''



##############################################################################################################


''' 7. Write a python  program on SumOfDigits, which accepts a two digit number as command line argument and prints the sum of its digits. 
Ex: Input: 35 
Output: 8 
Input: 88 
Output: 16 
 
 '''

##n=input("enter a number to find sum: ")
##sum=0
##
##for i in n:
##    sum=sum+int(i)
##print(sum)

''' output
enter a number to find sum: 88
16
enter a number to find sum: 35
8 '''
    
##############################################################################################################

''' 8. Write a python program EvenOrOdd, which accepts a whole number as command line argument and prints “Even Number”
if the number is Even and prints “Odd Number” if the number is Odd. If the input is not a number, print “Error”.  '''

##n=int(input("enter a number to even or odd: "))
##
##if n%2==0:
##    print("given number ",n,"is even number")
##elif n%2!=0:
##    print("given number ",n,"is odd number")
##else:
##    print("given number ",n,"is not number : Error")
    

''' output:
enter a number to even or odd: 5
given number  5 is odd number

enter a number to even or odd: 10
given number  10 is even number  '''


##############################################################################################################

''' 9. Write a python program Rounder, which accepts a whole number as command line argument and prints the same number
if the input is Odd. If the input is even, it should print the next multiple of ten. If the input is not a number or is negative,
print the string:“Error”. 
Input: 44, output: 50 
Input: 45, output: 45 '''

##n=int(input("enter a number : "))
##
##if n%2!=0:
##    print(" given number {} is an odd number hence result : {}".format(n,n))
##elif n%2==0:
##    while n%10!=0:
##        if n%10==0:
##            pass
##        else:
##            n+=1
##    print(n)
##
##elif n<0:
##    print("given number ",n,"is not number or negative : Error")

''' output:
enter a number : 45
 given number 45 is an odd number hence result : 45

enter a number : 44
50

enter a number : -1
 given number -1 is an odd number hence result : -1 '''

##############################################################################################################

'''11. Write a python  program Box, which accepts 2 numbers as command line argument and prints the following output: 
Input: 4 5 
Output: 
 *  *  *  *  * 
 *              * 
 *              * 
 *  *  *  *  * 
NOTE: Output stars must also be separated by a single space. The first argument is the number of rows and the second argument is the number of columns.
Negative numbers or 0 should print “Error” and come out. Numbers up to 30 must be handled. '''


##n=int(input())
##m=int(input())
##
##for i in range(n+1):
##    for j in range(m+1):
##        if i==1 or i==n or j==n:
##            print("*",end=" ")
##        else:
##            print(" ",end="")
##    print()


''' 12.  Write a python program StarPattern, which accepts a number as command line argument and prints the following output: 
Input: 4 
Output: 
*  
*  *  
*  *  *  
*  *  *  * 
NOTE: Output stars must also be separated by a single space. The number of lines must equal the number passed as argument.
Negative numbers or zero should print “Error” and exit. Numbers up to 10 must be handled. '''

##n=int(input("enter a number: "))
##
##if n<0:
##    print("given number",n,"is negative number : ERROR")
##else:
##    for i in range(0,n+1):
##        for j in range(0,i+1):
##            print("*",end="")
##        print()

''' output:
enter a number: 4
*
**
***
****
*****

enter a number: -1
given number -1 is negative number : ERROR
'''



##############################################################################################################

''' 14. Write a python  program on Prime numbers '''

##n=int(input("enter a number to check prime or not: "))
##count=0
##for i in range(1,n+1):
##    if n%i==0:
##        count+=1
##if count==2:
##    print("given number",n,"is prime number")
##else:
##    print("given number",n,"is not prime number")


''' output:
enter a number to check prime or not: 7
given number 7 is prime number

enter a number to check prime or not: 10
given number 10 is not prime number '''

##############################################################################################################

''' 15. Write a python  program on LeastNumber, which accepts two numbers as command line arguments and prints the least number of the two. 
If the input is not a number, print “Error”. 
 '''

##n1=int(input("enter n1 value "))
##n2=int(input("enter n2 value "))
##
##if n1<n2:
##    print(" the least number of the two number is: ",n1)
##
##elif n1>n2:
##        print(" the least number of the two number is: ",n2)
##else:
##    print("ERROR")

''' output

enter n1 value 10
enter n2 value 15
 the least number of the two number is:  10 '''

##############################################################################################################

''' 16. write a python program on finding a negative number or positive number '''

##n=int(input("enter n1 value "))
##if n<0:
##    print("given number ",n,"is a negative number")
##else:
##    print("given number ",n,"is a positive number")

''' output

enter n1 value 10
given number  10 is a positive number    

enter n1 value -10
given number  -10 is a negative number '''


##############################################################################################################



''' 20. Write a python program on filtering consonants 
 
Note the following points: 
The method should scan the given input, remove all the consonants and return the resulting string. 
The output should contain only vowels and all other characters, including special characters should be filtered out. 
If input is null, return null. 
Example input: “Telephone”, Output: “eeoe” '''


##s=input("enter some string to filter: ")
##v=["a","e","i","o","u","A","E","I","O","U"]
##
##for i in s:
##    if i in v:
##        print(i,end="")

'''
output

enter some string to filter: manikanta
aiaa '''



''' 23. Wap in which you are taking numbers from the user arranged them in a list, sort them,reversethem, and print them '''

##l=[]
##n=int(input("how many nums you want"))
##
##for i in range(n):
##    num=int(input("enter a number: "))
##    l.append(num)
##l.sort(reverse=True)
##print(l)


''' output:
how many nums you want3
enter a number: 10
enter a number: 4
enter a number: 20
[20, 10, 4] '''


''' 24. Write a Python program that iterate over elements repeating each as many times as its count '''

##s=input("enter some string: ")
##l=[]
##l1=[]
##for i in s:
##    if s.count(i)>1:
##        l.append(i)
##for j in l:
##    if j not in l1:
##        l1.append(j)
##for k in l1:
##    print(k,s.count(k))

''' output:
enter some string: happyneww
p 2
w 2

'''


''' 25. Write a Python program to find the occurrences of 10 most common words in a given text. '''

##s=input("enter some string: ")
##l=[]
##l1=[]
##for i in s:
##    if s.count(i)>1:
##        l.append(i)
##for j in l:
##    if j not in l1:
##        l1.append(j)
##for k in l1:
##    print(k,"occured ",s.count(k),"times")

''' output:
enter some string: happy new year
a occured  2 times
p occured  2 times
y occured  2 times
  occured  2 times
e occured  2 times  '''


'''31. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.  
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75 '''

##def number(n):
##    r1=n*m
##    return r1
##m=int(input("enter an unknown number: "))
##n=int(input("enter a number: "))
##if m==2:
##    print(" Double the number of {}={}".format(n,(number(n))))
##      
##elif m==3:
##    print(" Triple the number of {}={}".format(n,(number(n))))
##elif m==4:
##    print(" Quadruple the number of {}={}".format(n,(number(n))))
##elif m==5:
##    print(" Quintuple the number of {}={}".format(n,(number(n))))

''' output
enter an unknown number: 3
enter a number: 15
 Triple the number of 15=45

enter an unknown number: 5
enter a number: 15
 Quintuple the number of 15=75 '''
    


''' 32. Write a Python program to filter a list of integers using Lambda 
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
  '''

##l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##
##even=list(filter(lambda x:x%2==0,l))
##odd=list(filter(lambda x:x%2!=0,l))
##print(even)
##print(odd)

'''
33.  Write a Python program to add two given lists using map and lambda. 
 Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9] '''

##l1=[1, 2, 3]
##l2=[4, 5, 6]
##
##op=list(map(lambda x,y:x+y,l1,l2))
##print(op)

''' output
[5, 7, 9] '''


''' 35.  Write a Python program to generate a float between 0 and 1,
inclusive and generate a random float within a specific range. Use random.uniform() '''


import random

op=random.uniform(0,1)
op1=random.rand
print("float between 0 and 1 ",op)
print("float between 0 and 1 ",op1)









































