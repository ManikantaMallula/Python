''' 1write a program to print the list of elements of prinicipal diaognal
input:
3 3
1  2 3
10 20 30
5  10 15
output:[1, 20, 15] '''





'''
2.wap take a string sparate with space and done add,sub,mul,div?
eg:- input:-18 7
     output:-(25,12,126,2) '''

##s=input("enter some string using space seperate: ")
##l=s.split()
##sum,sub,mul,div=0,0,1,1
##l1=[]
##for i in l:
##    k=int(i)
##    l1.append(k)
##for i in l1:
##    sum+=i
##    sub=abs(sub-i)
##    mul*=i
##print(sum,sub,mul)





'''
3.In this question, we will provide an integer int_1, we have already declared the calculate_sum 
function for you in solution.py. The initial int_1 of this function represents the initial value, 
and you need to calculate the form a + aa + aaa + aaaa value, and finally print the result.
input:5
output:6170 '''


##s=input("enter a num in string form: ")
##n=int(s)
##l=[]
##for i in range(1,n):
##    k=int(s*i)
##    l.append(k)
##    
##print(sum(l))





'''
4.Please complete the code in solution.py to realize the function of get_sum.
get_sum function receives an array parameter nums.
Please use the lambda function to pass 
in two unknown number x and y for the get_sum function and take this
lambda function as the return value of the get_sum function. For the
parameter nums received by get_sum, 
if the length of the array num is an even number, return the sum of nums
by x times. If the length of the array num is an odd number, return the
sum of nums by -y times.
input:[1,2,3,4]
       2,3
output:20 '''

##l=eval(input("enter list values: "))
##x=int(input("enter a nuber to find collatz sequence: "))
##y=int(input("enter a nuber to find collatz sequence: "))
##k=len(l)
##if k%2==0:
##    op=sum(l)*x
##else:
##    op=sum(l)*(-y)
##print(op)





'''
5.Mathematicians have come up with a famous conjecture - the Collatz conjecture.

For any positive integer n, if n is even, make it n // 2.
If n is an odd number, make it 3 * n + 1.
If you follow this rule, you must end up with 1.
How many rounds of transformation will that number go through to become 1? '''



##n=int(input("enter a nuber to find collatz sequence: "))
##
##while n!=1:
##    if n%2==0:
##        n=n//2
##        print(n)
##    else:
##        n=3*n+1
##        print(n)





















