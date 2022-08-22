''' 1. What about two asterisks (**)?

in a function definition, argument with double asterisks as prefix helps in sending
multiple keyword arguments to it from calling environment'''

##def info(**marks):
##    print(marks)
##info(sub1=90,sub=70,sub3=65)

'''2.Write a function called fizz_buzz that takes a number.
-If the number is divisible by 3, it should return “Fizz”.
-If it is divisible by 5, it should return “Buzz”.
-If it is divisible by both 3 and 5, it should return “FizzBuzz”.
-Otherwise, it should return the same number. '''

##def check(num):
##    if num%3==0 and num%5==0:
##        print("FizzBuzz")
##    else:
##        if num%3==0:
##            print("Fizz")
##        elif num%5==0:
##            print("Buzz")
##        else:
##            print(num)
##print(check(15))
##print(check(6))
##print(check(10))
##            

'''3.Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with
a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
-0 EVEN
-1 ODD
-2 EVEN
-3 ODD '''

##def showNumbers(limit):
##    for i in range(limit):
##        if i%2==0:
##            print("-",i," even")
##        else:
##            print("-",i," odd")
##limit=int(input("enter a number: "))
##showNumbers(limit)          

'''4.Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20. '''


##def sumOfmultiples(n):
##     for i in range(1,n+1):
##         if i%3==0 or i%5==0:
##             print(i,end=" ")
##a=int(input("enter the number: "))
##sumOfmultiples(a)

'''5.Write a function that prints all the prime numbers between 0 and limit where limit is a parameter. '''

##def prime(n):
##    for i in range(0,n+1):
##        if i>1:
##            for j in range(2,i):
##                if i%j==0:
##                    break
##            else:
##                print(i)
##
##n=a=int(input("enter the number: "))
##prime(n)

'''6.Write a function for checking the speed of drivers. This function should have one parameter: speed.
1.If speed is less than 70, it should print “Ok”.
2.Otherwise, for every 5km above the speed limit (70),
it should give the driver one demerit point and print the total number of demerit points.
For example, if the speed is 80, it should print: “Points: 2”.
3.If the driver gets more than 12 points, the function should print: “License suspended”'''

##def drivers(speed):
##    if speed<=70:
##        print("OK")
##    elif speed>70:
##        sub=speed-70
##        mul=sub//5
##        if mul>12:
##            print("License suspended")
##        else:
##            print("total number of demerit points: ",mul)
##a=int(input("enter speed: "))
##drivers(a)  
 

''' 7.What is the result of “bag” > “apple”? '''

##def max(a,b):
##    print(a>b)
##a=input("enter some string: ")
##b=input("enter some string: ")
##max(a,b)

''' 8.What is the result of f“{2+2}+{10%3}”? '''
##def result():
##    print(f"{2+2}+{10%3}")
##result()
 
'''9.Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it.
And also it must return both addition and subtraction in a single return '''


##def calculation(a,b):
##    add=a+b
##    sub=a-b
##    print("addition and subtraction of {} and {} is addition={} and addition {}".format(a,b,add,sub))
##a=int(input("enter a value: "))
##b=int(input("enter b value: "))
##calculation(a,b)
##    

##def calculation(a,b):
##    add=a+b
##    sub=a-b
##    return (add,sub)
##a=int(input("enter a value: "))
##b=int(input("enter b value: "))
##print(calculation(a,b))


'''10. Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it. '''

##def outer(a,b):
##    def inner():
##        sum=a+b
##        print(sum)
##    inner()
##
##o=outer(20,10)

'''11.Write a recursive function to calculate the sum of numbers from 0 to 10 '''

##def recursive(n):
##    if n==0:
##        return n
##    else:
##
##        return n+recursive(n-1)
##n=10
##print(recursive(n))
    
'''12. Assign a different name to function and call it through the new name '''

##def welcome():
##    print("good morning")
##
##new=welcome
##new()

''' 13.Generate a Python list of all the even numbers between 4 to 30 '''

##def even(n):
##    l=[]
##    for i in range(4,n+1):
##        if i%2==0:
##            l.append(i)
##    return l        
##n=30
##print(even(n))


''' 14.Return the largest item from the given list '''


##def largest(l):
##    print(max(l))
##l=[1,2,3,4,5,6,7]
##largest(l)

'''15.Create a function showEmployee() in such a way that it should accept employee name,
and it’s salary and display both, and if the salary is missing in function call it should show it as 9000 '''

##def showEmployee(name,salary=9000):
##    print(name,salary)
##
##showEmployee(name="ravi")
##showEmployee(name="ravi",salary=10000)

    












