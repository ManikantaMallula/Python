'''1. Write a program to swap given two numbers without temporary variable. '''
##a=10
##b=20
##a,b=b,a
##print(a)
##print(b)
##
##output:-
##20
##10

''' 2. Write a program to accept 4 numbers from command prompt add
them using two variables.  '''
##a=4
##c =0
##for i in range(4):
##    b = int(input("enter number"))
##    c+=b
##print("sum of 4 numbers are:",c)
##output:-
##4
##10
##20
##30
##40
##100

'''
 3. Write a program which accepts an int values as command line
 argument and    print the next multiple of 100. 

    Ex: Input: 35 

    Output: 100 

    Input: 435 

    Output: 500 
'''
##a=100
##num=int(input())
##while True:
##    if num<a:
##        print(a)
##        break
##    else:
##        a=a+100
##output:-
##35
##100
##435
##500
'''
4. Write a program ThreeDPalindrome 

    In this program accept a 3 digit integer as a
    command line argument and return the String true
    if the integer is a Palindrome or the String false otherwise '''
##a=int(input("enter the number"))
##temp=a
##rev=0
##while a>0:
##    dig=a%10
##    rev=rev*10+dig
##    a=a//10
##
##if temp==rev:
##    print("Palindrome")
##else:
##    print("false")
##
##output:-121
##true
##123
##false

'''
5. A class RussianMultiplication is given to you. Implement the
following method in that class: getProduct(int num1, int num2). 
If either number is not positive then return -1. Return the product
of the two numbers. Calculate the product using Russian multiplication.  

Russian Multiplication Method:  

The Russian peasant multiplication, also called the
Russian peasant algorithm, uses a halving and doubling
method to multiply whole numbersWhen halving, disregard any
remainder. Just put the quotient in the halving columnWhen the
number in the halving column is 1, cross out all rows that have an
even number in the halving columnthe answer is found by adding the
remaining numbers in the doubling column  

Example # 1: 11 × 12   
  
  
Halving                              Doubling  
  
   11                    ×                  12   
  
   5                      ×                  24   
  
   2                      ×                  48  ---> Disregard this since 2 is even  
  
   1                      ×                  96   

The product of 11 and 12 is: 12 + 24 + 96 = 132   '''
##a=int(input("enter the number"))
##b=int(input("enter the number"))
##c=a*b
##if a<0 or b<0:
##    print("-1")
##else:
##    print(c)
##output:-a=-1,b=20
##-1
##a=11,b=12
##132
'''
6.  A class Student is given to you. Add details in the Student class.  

Student:  

Instance Variables: studentId : PUBLIC  , studentName : PUBLIC ,  

Marks: PRIVATE, grade: PRIVATE  

PUBLIC Methods: displayDetails(): ,  

PRIVATE METHOD : calculateGrade(): 

Default constructor  

A constructor that that takes the following parameter: studentId, studentName, marks.  

Note that grade is not set either through constructor or setter as it is a calculated value.  

  

Methods  

displayDetails(): This method should display the details of the student in the following format:  

Student [name=John Smith, studentId=123, marks=95, grade=A]  

  

calculateGrade(): This is a private method that calculates the grade based on the marks that is set. If marks is above 90, grade is set to A. If marks is between 80 and 90, grade is set to B, if marks is between 70-80 grade is set to C, if marks is between 60-70, grade is set to D, if marks is less than 60, grade is set to E.Use this method when you need to set or reset grade.  
'''
 
'''
7. Write a python  program on SumOfDigits, which accepts a two digit number
as command line argument and prints the sum of its digits.  

Ex: Input: 35  

Output: 8  

Input: 88  

Output: 16  

  

Note: Do not use Conditional or Looping statements while solving the problem.  
'''
##a=(input("enter the number"))
##sum=0
##for i in a:
##    sum+=int(i)
##print(sum)
##output:-
##35
##8
##88
##16
'''
8. Write a python program EvenOrOdd, which accepts a whole number as
command line argument and prints “Even Number” if the number is Even
and prints “Odd Number” if the number is Odd. If the input is not a
number, print “Error”.  
'''
##a=input()
##if a.isalpha():
##    print("Error")
##elif int(a)%2==0:
##    print("even")
##else:
##    print("odd")
##output:-
##tarak:-error
##2:-even
##3:-odd

'''
9. Write a python program Rounder, which accepts a whole number as
command line argument and prints the same number if the input is Odd.
If the input is even, it should print the next multiple of ten. If the
input is not a number or is negative, print the string:“Error”.  

Input: 44, output: 50  

Input: 45, output: 45 
'''
##a = input("enter values")
##if a.isdigit() and int(a)>0:
##    if int(a)%2==0:
##        c = int(a)%10
##        print(10-c+int(a))
##    else:
##        print(a)
##else:
##    print("error")
##output:-
##-1
##error
##44
##50
##45
##45
'''
10. Write a python program DigitChecker, which accepts a two digit number
as command line argument and prints Zero if the digits are same and if the
two digits are different, it prints their difference.  

Ex: Input: 52  

Output: 3  

Input: 88  

Output: 0  
'''
##a = input("ENTER two digit  NUMBER")
##c = a[0]
##d = a[1]
##if c==d:
##    print(0)
##else:
##    print(int(c)-int(d))
##output:-
##52
##3
##88
##0
'''
11. Write a python  program Box, which accepts 2 numbers as command
line argument and prints the following output:  

Input: 4 5  

Output:  

 *  *  *  *  *  

 *              *  

 *              *  

 *  *  *  *  *  

NOTE: Output stars must also be separated by a single space. The first argument is the number of rows and the second argument is the number of columns. Negative numbers or 0 should print “Error” and come out. Numbers up to 30 must be handled.  
'''
##a=int(input("enter the number"))
##b=int(input("enter the number"))
##for i in range(a):
##    for j in range(b):
##        if i==0 or i==a-1 or j==0 or j==b-1:
##            print("*",end="  ")
##        else:
##            print("  ",end="  ")
##    print()
##output:-
##enter the number4
##enter the number5
##*  *  *  *  *  
##*              *  
##*              *  
##*  *  *  *  *  


'''
12.  Write a python program StarPattern, which accepts a number as command line argument and prints the following output:  

Input: 4  

Output:  

*   

*  *   

*  *  *   

*  *  *  *  

NOTE: Output stars must also be separated by a single space. The number of
lines must equal the number passed as argument. Negative numbers or
zero should print “Error” and exit. Numbers up to 10 must be handled.  
'''
##a=int(input("enter the number"))
##for i in range(1,a+1):
##    for j in range(i):
##        print("*",end=" ")
##    print()

##Output:  
##
##*   
##
##*  *   
##
##*  *  *   
##
##*  *  *  *  
'''
13. Write a python program NumberPattern4, which accepts a number as command line argument and prints the following output:  

Input: 5  

Output:  

1  

2 4  

3 6 9  

4 8 12 16  

5 10 15 20 25  

  

NOTE: Output numbers must be separated by a single space. The number of lines must equal the number passed as argument. Negative numbers or zero as input should print “Error” and exit. Numbers up to 10 must be handled.  

 '''
##a=int(input("enter the number"))
##for i in range(1,a+1):
##    for j in range(1,i+1):
##        print(i*j,end=" ")
##    print()

##Output:  
##
##1  
##
##2 4  
##
##3 6 9  
##
##4 8 12 16  
##
##5 10 15 20 25  
'''
14. Write a python  program on Prime numbers '''
##a=int(input())
##for i in range(2,a):
##    if a%i==0:
##        print("not prime")
##        break
##else:
##    print("prime")
##output:-
##5
##prime
##4
##not prime
'''
15. Write a python  program on LeastNumber, which accepts two numbers as command
line arguments and prints the least number of the two. If the input is not a
number, print “Error”. '''
##a=(input("enter the number"))
##b=input("enter the number")
##if a.isnumeric():
##    if a<b:
##        print(a)
##    else:
##        print(b)
##else:
##    print("error")
##output:-
##12
##34
##12
##a
##error
'''
16. write a python program on finding a negative number or positive number  

 '''
##a=int(input("enter the number"))
##if a<0:
##    print("negative number")
##else:
##    print("positive number")
##output:-
##1
##positive number
##-1
##negative number

'''
17.  

In the given Class DateFormatter, implement the method format()
such that it accepts the date (date month year), separated by comma /
space or both and return the date in the format of YYYY-MM-DD.  

Eg.: 21,May,2012 / 21 May 2012 / 21, May, 2012  

Output : 2012-05-21  
'''


'''

18.write a python program on characterscounter 

  

Note the following points:  

The method should scan the given input, and count the number of times the given character “toFind” occurs in the input string. Return the number of times the given character occurs in the input string.  

If input is null or empty, return -1.  

Example input: “Hello World”, and 'H”, you must return 1, since 'H' occurs once in “Hello World”.  

The character must be searched for regardless of case. If upper case H is given as the character to find, the method must search for lower and uppercase 'H' and return the number of times it exists.  

 
 '''
##a=input("enter the string").upper()
##c=input().upper()
##l=[]
##for i in a:
##    l.append(i)
##if c in l:
##    d=l.count(c)
##    print(d)
##else:
##    print("null")
##output:-
##Hello
##h
##1
##hello
##k
##null
'''
20. Write a python program on filtering consonants  

  

Note the following points:  

The method should scan the given input, remove all the consonants and return the resulting string.  

The output should contain only vowels and all other characters, including special characters should be filtered out.  

If input is null, return null.  

Example input: “Telephone”, Output: “eeoe”  '''
##a=input("enter the string")
##b="aeiou"
##for i in a:
##    if i in b:
##        print(i,end="")
##else:
##    print("null")
##output:-
##teleohone:
##eeoe

'''
22. Write a python program on adding elements from a list,product of
an elemnts 

from a list using functions? 

 '''
##def add(a):
##    add=0
##    for i in a:
##        add+=(i)
##    return add
##def mult(a):
##    mul=1
##    for i in a:
##        mul*=(i)
##    return mul
##x=[1,2,3,4]
##print(add(x))
##print(mult(x))
##output:
##10
##24
'''
23. Wap in which you are taking numbers from the user arranged
them in a list, sort them,reversethem, and print them 
'''
##a=int(input("enter"))
##l=[]
##for i in range(a):
##    b=int(input("enter the number"))
##    l.append(b)
##c=sorted(l)
##d=c[::-1]
##print(d)
##    output:
##enter3
##enter the number2
##enter the number3
##enter the number4
##[4, 3, 2]
'''
24. Write a Python program that iterate over elements
repeating each as many times as its count '''
##a=input().split()
##l=[]
##for i in a:
##    if i not in l:
##        l.append(i)
##for i in l:
##    print(i,"-",a.count(i))
##output:-
##this this is aa
##this - 2
##is - 1
##aa - 1

'''
25. Write a Python program to find the occurrences of 10 most common words in a given text. 
'''

'''
26. Write a Python program to count most and least common characters in
a given string '''
##a=input().split()
##l=[]
##count=0
##for i in a:
##    if i not in l:
##        l.append(i)
##        count+=1
##if count<=1:
##    print(count)

'''27. Write a Python program to sum all the items in a dictionary.'''
##a ={"a":1,"b":5,"c":8,"d":10}
##c=0
##for key,values in a.items():
##    c+=values
##print("sum of values",c)
##output
##sum of values 24
'''
31. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.   
Sample Output: 
Double the number of 15 = 30 
Triple the number of 15 = 45 
Quadruple the number of 15 = 60 
Quintuple the number 15 = 75 
'''
##def mul(a):
##    c=a*b
##    return c
##a=int(input())
##b=int(input())
##print(mul(a))
##output:-
##15
##2
##30
'''
32. Write a Python program to filter a list of integers using Lambda  
Original list of integers: 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
Even numbers from the said list: 
[2, 4, 6, 8, 10] 
Odd numbers from the said list: 
[1, 3, 5, 7, 9] 
'''
##l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##even=list(filter(lambda x:x%2==0,l))
##odd=list(filter(lambda x:x%2==1,l))
##print(even)
##print(odd)
##output:-
##[2, 4, 6, 8, 10]
##[1, 3, 5, 7, 9]
'''33.  Write a Python program to add two given lists using map and lambda. 

## Original list:
##[1, 2, 3]
##[4, 5, 6]
##Result: after adding two list
##[5, 7, 9]'''

##a =[1, 2, 3]
##b = [4, 5, 6]
##c= list(map(lambda x,y:x+y,a,b))
##print(c)
##output:-
##[5, 7, 9]


'''
36. Write a Python program to check the validity of password input by users  
Validation : 

At least 1 letter between [a-z] and 1 letter between [A-Z]. 

At least 1 number between [0-9]. 

At least 1 character from [$#@]. 

Minimum length 6 characters. 

Maximum length 16 characters. 
'''

##a=input()
##len_a=len(a)
##up=0
##lo=0
##num=0
##sp=0
##if len_a>=6 or len_a<=16:
##    for i in a:
##        if i.isupper():
##            up+=1
##        if i.islower():
##            lo+=1
##        if i.isalnum():
##            num+=1
##        if i=="$" or i=="#" or i=="@":
##            sp+=1
##if up>=1 and lo>=1 and num>=1 and sp>=1:
##    print("valid")
##else:
##    print("not valid")
##output:-
##123Tarak$
##valid


    
'''
36. Write a Python program to check if two given sets have no elements
in common.  
'''
##a={1,2,3}
##b={4,5,6}
##c=a.isdisjoint(b)
##print(c)       
