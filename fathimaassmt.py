'''
1. 4.Write a Python class to get all possible unique subsets from a set of distinct integers.

Input : [4, 5, 6]

Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
'''

##from itertools import combinations
##a=[4, 5, 6]
##b=[]
##for i in range(len(a)+1):
##    b.append(combinations(a,i))
##for i in b:
##    print(list(i),end=" ")

##output:
##[()] [(4,), (5,), (6,)] [(4, 5), (4, 6), (5, 6)] [(4, 5, 6)]
'''
2. Write a Python class to find the three elements that sum to zero from a set of n real numbers.

Input array : [-25, -10, -7, -3, 2, 4, 8, 10]

Output : [[-10, 2, 8], [-7, -3, 10]]
'''
##from itertools import combinations
##a=[-25, -10, -7, -3, 2, 4, 8, 10]
##b=[]
##for i in range(len(a)+1):
##    if sum(a)==0:
##        b.append(combinations(a,3))
##print(b)


'''
3. Write a Python class which has two methods get_String and print_String.
get_String accept a string from the user and print_String print the string in upper case
'''
##class String:
##    def get_string(self,string):
##        self.string=string
##    def print_string(self,string):
##        self.string=string
##        print(self.string.upper())
##string=input("Enter a string:")
##a=String()
##a.get_string(string)
##a.print_string(string)

##output:
##Enter a string:hello world
##HELLO WORLD
'''
4. Write a Python program to count the frequency of words in a file
'''
##f=open("file.txt",mode="r")
##r=f.read()
##r=r.split()
##count=0
##for i in r:
##    count+=1
##print("The count is:",count)

##output:
##The count is: 90
'''    
5. .Write a Python program to extract characters from various text files and puts them into a list.
'''
##f=open("file.txt",mode="r")
##r=f.read()
##r=r.split()
##f=open("file1.txt",mode="r")
##re=f.read()
##re=re.split()
##r.extend(re)
##print(r)

##output:
##['3.', 'Write', 'a', 'Python', 'class', 'which', 'has', 'two', 'methods', 'get_String',
##    'and', 'print_String.', 'get_String', 'accept', 'a', 'string', 'from', 'the', 'user', 'and',
##    'print_String', 'print', 'the', 'string', 'in', 'upper', 'case', '4.', 'Write', 'a', 'Python',
##    'program', 'to', 'count', 'the', 'frequency', 'of', 'words', 'in', 'a', 'file', '5.', '.Write', 'a',
##    'Python', 'program', 'to', 'extract', 'characters', 'from', 'various', 'text', 'files', 'and', 'puts',
##    'them', 'into', 'a', 'list.', '6.', 'Write', 'a', 'Python', 'program', 'to', 'generate', 'the', 'running',
##    'product', 'of', 'the', 'elements', 'of', 'an', 'given', 'iterable.', '7.', 'A', 'class', 'Student', 'is',
##    'given', 'to', 'you.', 'Add', 'details', 'in', 'the', 'Student', 'class.', '3.', 'Write', 'a', 'Python', 'class',
##    'which', 'has', 'two', 'methods', 'get_String', 'and', 'print_String.', 'get_String', 'accept', 'a', 'string', 'from',
##    'the', 'user', 'and', 'print_String', 'print', 'the', 'string', 'in', 'upper', 'case', '4.', 'Write', 'a', 'Python', 'program',
##    'to', 'count', 'the', 'frequency', 'of', 'words', 'in', 'a', 'file']
'''
6. Write a Python program to generate the running product of the elements of an given iterable.
'''
##from itertools import product
##a=[1,2,3]
##b=[4,5,6]
##c=product(a,b)
##for i in c:
##    print(i)

##output:
##(1, 4)
##(1, 5)
##(1, 6)
##(2, 4)
##(2, 5)
##(2, 6)
##(3, 4)
##(3, 5)
##(3, 6)

'''

7. A class Student is given to you. Add details in the Student class.

Student:

Instance Variables: studentId : PUBLIC , studentName : PUBLIC ,

Marks: PRIVATE, grade: PRIVATE

PUBLIC Methods: displayDetails(): ,

PRIVATE METHOD : calculateGrade():

Default constructor

A constructor that that takes the following parameter: studentId, studentName, marks.

Note that grade is not set either through constructor or setter as it is a calculated value.

Methods

displayDetails(): This method should display the details of the student in the following
format:

Student [name=John Smith, studentId=123, marks=95, grade=A]

calculateGrade(): This is a private method that calculates the grade based on the marks
that is set. If marks is above 90, grade is set to A. If marks is between 80 and 90, grade
is set to B, if marks is between 70-80 grade is set to C, if marks is between 60-70,
grade is set to D, if marks is less than 60, grade is set to E.Use this method when you
need to set or reset grade
'''
##class Student:
##    __marks=0
##    __grade=None
##    def __init__(self,studentId,studentName):
##        self.studentId=studentId
##        self.studentName=studentName
##    def __calculateGrade(self):             
##        if self.__marks>90:
##            self.__grade="A"
##            return self.__grade
##        if self.__marks<=90 and self.__marks>80:
##            self.__grade="B"
##            return self.__grade
##        if self.__marks<=80 and self.__marks>70:
##            self.__grade="C"
##            return self.__grade
##        if self.__marks<=70 and self.__marks>=60:
##            self.__grade="D"
##            return self.__grade
##        if self.__marks<60 :
##            self.__grade="E"
##            return self.__grade
##    def displayDetails(self):
##        self.__marks=75
##        print(f"name={self.studentName},id={self.studentId} ,marks={self.__marks},grade={self.__calculateGrade()}")
##s=Student(22045,"Bazequa")
##s.displayDetails()

##output:
##name=Bazequa,id=22045 ,marks=75,grade=C

'''
8. In the given Class DateFormatter, implement the method format() such that it accepts the date (date month year), separated by comma / space or both and return the date in the format of YYYY-MM-DD.

Eg.: 21,May,2012 / 21 May 2012 / 21, May, 2012

Output : 2012-05-21

Note the following:

The input can have comma, space or both. No other separator is allowed

The month can be given in full form (January, February etc) or in short 3-Letter form (Jan, feb,mar, apr, may, jun, jul, aug, sep, oct, nov, dec) . This program should accept both types.

Output month should always be a number.

Validate for invalid values.

Return null for error in input.
'''
##import datetime
##a=datetime.datetime(10,May,2012)
##print(a,format(a))

'''
9. Write a python program on filtering consonants

Note the following points:

1. The method should scan the given input, remove all the consonants and return the resulting string.

2. The output should contain only vowels and all other characters, including special characters should be filtered out.

3. If input is null, return null.

4. Example input: “Telephone”, Output: “eeoe”

'''
##string=input()
##a="aeiouAEIOU"
##c=[]
##for i in string:
##    if i in a:
##        c.append(i)
##print("".join(c))

##output:
##Telephone
##eeoe
'''
10. Write a python program to find factorial ,
Fibonacci series, sum of digits, product of digits, reverse of a number, amstrong number.
'''
#Factorial

##def outer(num):
##    def inner():
##        num=int(input("enter number:"))
##        fact=1
##        while num>0:
##            fact=fact*num
##            num=num-1
##        print(fact)
##    return inner()
##@outer
##def fact():
##    pass
##fact

##output:
##enter number:5
##120

#Fibonacci

##def outer(num):
##    def inner():
##        num=int(input("enter number:"))
##        a=0
##        b=1
##        for i in range(1,num+1):
##            c=a+b
##            a=b
##            b=c
##            print(c)
##    return inner()
##@outer
##def fib():
##    pass
##fib

##output:
##enter number:5
##1
##2
##3
##5
##8
#sum of digits

##def outer(num):
##    def inner():
##        num=int(input("enter number:"))
##        temp=num
##        s=0
##        while num>0:
##            r=num%10
##            s=s+r
##            num=num//10
##        print(s)
##    return inner()
##@outer
##def sum1():
##    pass
##sum1

##output:
##enter number:1234
##10

#product of digits

def outer(num):
    def inner():
        num=int(input("enter number:"))
        temp=num
        s=1
        while num>0:
            r=num%10
            s=s*r
            num=num//10
        print(s)
    return inner()
@outer
def mul1():
    pass
mul1

#output:
##enter number:345
##60

#reverse of a number
##def outer(num):
##    def inner():
##        num=int(input("enter number:"))
##        temp=num
##        s=0
##        while num>0:
##            r=num%10
##            s=s*10+r
##            num=num//10
##        print(s)
##    return inner()
##@outer
##def rev1():
##    pass
##rev1
##
##output:
##enter number:123
##321


#armstrong number
##def outer(num):
##    def inner():
##        num=int(input("enter number:"))
##        temp=num
##        s=0
##        while num>0:
##            r=num%10
##            s=s+r**3
##            num=num//10
##        if temp==s:
##            print("Armstrong")
##        else:
##            print("Not armstrong")
##    return inner()
##@outer
##def arm1():
##    pass
##arm1

##output:
##enter number:153
##Armstrong
