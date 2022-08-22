
''' 1.Write a Python class to get all possible unique subsets from a set of distinct integers.
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]] '''

##class A:
##    def aa(self,a):
##        return self.bb([],sorted(a))
##    def bb(self,c,aa):
##        if aa:
##            return self.bb(c,aa[1:])+self.bb(c+[aa[0]],aa[1:])
##        return [c]
##a=[4,5,6]
##print(A().aa(a))

''' output:
    [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]'''

''' 10. Write a python program to find factorial , Fibonacci series, sum of digits, product of digits, reverse of a number, amstrong number. '''


##def fact(func):
##    def inner(n):
##        s=1
##        for i in range(1,n+1):
##            s*=i
##        return s
##    return inner
##
##@fact
##def main(n):
##    return n
##
##n=int(input("enter a number to find factorial: "))
##print(main(n))

''' output:
enter a number to find factorial: 4
24 '''


##def fibb(func):
##    def inner():
##        a,b=0,1
##        for i in range(10):
##            s=a+b
##            a=b
##            b=s
##            print(b)
##    return inner
##
##@fibb
##def main():
##    return n
##main()

''' output:
1
2
3
5
8
13
21
34
55 '''




##def sod(func):
##    def inner(a,b):
##        print("sum of digits {} and {} is {}".format(a,b,a+b))
##    return inner
##@sod
##
##def main(a,b):
##    return a,b
##
##a=int(input("enter a value to find sum: "))
##b=int(input("enter b value to find sum: "))
##main(a,b)

''' output:
enter a value to find sum: 10
enter b value to find sum: 20
sum of digits 10 and 20 is 30 '''


##def pro(func):
##    def inner(a,b):
##        print("product of digits {} and {} is {}".format(a,b,a*b))
##    return inner
##@pro
##
##def main(a,b):
##    return a,b
##
##a=int(input("enter a value to find product: "))
##b=int(input("enter b value to find product: "))
##main(a,b)


''' output:
enter a value to find product: 10
enter b value to find product: 100
product of digits 10 and 100 is 1000 '''

##
##def revr(func):
##    def inner(n):
##        temp=n
##        op=""
##        while n>0:
##            d=n%10
##            op+=str(d)
##            n=n//10
##        print(int(op))
##    return inner
##            
##@revr           
##def main(n):
##    return n
##n=int(input("enter a number to reverse: "))
##main(n)

'''output:
enter a number to reverse: 123
321 '''


##def arms(func):
##    def inner(n):
##        t=n
##        s=0
##        p=len(str(n))
##        while t>0:
##            d=t%10
##            s+=d**p
##            t=t//10
##        if n==s:
##            print("given number {} is an armstrong number".format(n))
##        else:
##            func(n)
##    return inner
##@arms
##
##def main(n):
##    print("given number {} is not  an armstrong number".format(n))
##n=int(input("enter a number to check armstrong or not: "))        
##
##main(n)

''' output:
enter a number to check armstrong or not: 153
given number 153 is an armstrong number

enter a number to check armstrong or not: 145
given number 145 is not  an armstrong number '''

'''
3. Write a Python class which has two methods get_String and print_String.
get_String accept a string from the user and print_String print the string in upper case '''

##class String:
####    def __init__(self,name):
####        self.name=name
##    def get_string(self):
##        self.name=input("enter some string: ")
##    def print_string(self,name):
##        
##        print(global.name.upper())
##s=String()
##s.get_string()
##
##s.print_string()
        



''' 4. Write a Python program to count the frequency of words in a file '''

''' In the given Class DateFormatter, implement the method format() such that it accepts the date (date month year), separated by comma / space or both and return the date in the format of YYYY-MM-DD. 
Eg.: 21,May,2012 / 21 May 2012 / 21, May, 2012 
Output : 2012-05-21  '''



        



##from datetime import date
##class Dateformatter:
##    def __init__(self,date,month,year):
##        self.date=date
##        self.month=month
##        self.year=year
##    def format(self):
##        print("{}-{}-{}".format(self.year,self.month,self.date))
##a=Dateformatter(21,"may",2012)
##a.format()
##
##


'''from datetime import date
class Dateformatter:
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
    def format(self):
        print("{}-{}-{}".format(self.year,self.month,self.date))
a=Dateformatter(21,"may",2012)
a.format()

output:

2012-05-21 '''
''' output:

2012-05-21 '''


''' .Write a Python program to extract characters from various text files and puts them into a list. '''

with open("file.txt","r") as f:
    l=[]
    a=f.readlines()
    for i in a:
        l.append(i)
print(l)

'''
output:
    ['abc\n', 'happy\n', 'new\n'] '''
















