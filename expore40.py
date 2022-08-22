'''1).Write a Python program to remove and print every third number from a list of numbers until the list becomes empty '''

##def func(l):
##    pos=3-1
##    index=0
##    l1=len(l)
##
##    while l1>0:
##        index=(pos+index)%l1
##        print(l.pop(index))
##        l1-=1
##l=[1,2,3,4,5,6,7]
##func(l)
##print(l)


    
    

''' 2).. Write a Python program to count the number of students of individual class.
Sample Output:
Counter({'VI': 3, 'V': 2, 'VII': 1}) '''

##from collections import *
##c=(("V",1,),("VI",1),("V",2),("VI",2),("V",3),("VII",3))
##op=Counter(class_name for class_name,no_s in c)
##print(op)



'''3).Write a Python program to concatenate all elements in a list into a string and return it '''

##l=["o","j","a","s"]
##s=""
##for i in l:
##    s+=i
##print(s)


''' 4).Write a Python program to convert a float to ratio.  

Expected Output :

21/5 '''

##f=21.5
##l=str(f).split(".")
##print(l)
##op=str(f).replace("/",".")
##print(op)

##from fractions import *
##f=21.5
##print(Fraction(f).limit_denominator())

''' 5).Write a Python function that prints out the first n rows of Pascal’s triangle '''

##n=int(input("enter no of rows: "))
##for i in range(n):
##    print(" "*(n-i),end="")
##    
##    print(" ".join(map(str,str(11**i))))




##def pascal_triangle(n):
##   trow = [1]
##   y = [0]
##   for x in range(max(n,0)):
##      print(trow)
##      trow=[l+r for l,r in zip(trow+y, y+trow)]
##   return n>=1
##pascal_triangle(6) 












