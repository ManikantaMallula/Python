'''1.Write a Python program to get all possible combinations of the elements of
a given list using itertools module. '''


##from itertools import *
##def comb(l):
##    op=[]
##    for i in range(1,len(l)+1):
##        op.append(tuple(combinations(l,1)))
##    return op
##l=[1,2,3,4]
##print(comb(l))

'''
2.Write a python program to create an iterator that returns consecutive keys
and groups from an iterable. '''

##from itertools import *
###s="aaaabbbbbbc"
##d={}
##s=[1,1,1,2,2,2,2,2,4,4,4,3,3]
##op=groupby(s)
##for i,j in op:
##    print(i,"-",list(j))


'''
3. Write a Python program to find the years where 25th of December be a
Sunday between 2000 and 2150. '''






'''
4.write a python program using generator write armstrong.  '''

##def arm():
##    s=int(input("enter start range: "))
##    e=int(input("enter end range: "))
##    for i in range(s,e+1):
##        l=len(str(i))
##        t=i
##        s=0
##        while t>0:
##            r=t%10 
##            s+=r**l
##            t=t//10
##        if i==s:
##            yield i
##op=arm()
##for i in op:
##    print(i)
####print(next(op))
####print(next(op))
    
        




'''
5.write a python program by using math module use 3 function for each
function one example. '''


##from math import *  
##
##print(fsum([1,2,3,4,5,6]))
##print(fsum((1,2,3,4,5,6)))
##
##print(factorial(4))
##print(factorial(5))
##
##
##print(remainder(9,2))
##print(remainder(153,10))








