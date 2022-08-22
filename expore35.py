'''1.Python Program to Reverse a Stack using Recursion'''

##def func(n,ls):
##   
##    if len(n)==0:
##        print(ls)
##    else:
##        m = n.pop()
##        ls.append(m)
##        recur(n,ls)
##    
##    
##lst = [1,2,3,4,5]
##lst2 = []
##func(lst,lst2)


'2.Python Program to Append the Content of One File to the End of Another File'

##with open('aaaa.txt','w') as f:
##    f.write('hello world and welcome to the coding')
##    
##with open('bbbb.txt','w') as f:
##    f.write('im learning python everyday')
##
##with open('aaaa.txt','a') as f:
##    with open('bbbb.txt','r') as f2:
##        f.write(f2.read())
##


'3.Python Program to Create a Class and Get All Possible Distinct Subsets from a Set'

##from itertools import combinations
##sets=[1,2,3,4]
##l=set()
##for i in range(len(sets)):
##    n=list(combinations(sets,i))
##    for j in n:
##        lst.add(j)
##print(l)




'4.How can you randomize the items of a list in place in Python?'
##import random
##
##l=[1,2,3,4,5]
##
##n=random.shuffle(l)
##
##print(l)





'''5.write a python program on showing 
KeyboardInterrupt,
ArithmeticError,
StopIteration
AssertionError
ImportError'''

'KeyboardInterrupt Error'
##n=5
##try:
##    for i in range(n):
##        m=input('>:')
##
##except KeyboardInterrupt:
##    print('Hello user you have pressed ctrl-c button.')
##
##for i in range(n):
##    print(i)

'Arithmetic Error'
##n = 5
##m = 0
##try:
##    print(n/m)
##except ArithmeticError:
##    print('cant calculate by zero')

'stop iteratin error'
##try:
##    lst=[1,2,3]
##    lst2=iter(lst)
##    for i in range(4):
##        print(next(lst2))
##
##except StopIteration:
##    print('list out of range')

'Assertion Error'
try:
    a=1
    b=0
    assert b>0, 'not equal'
    
except AssertionError as msg:
    print(msg)


'Import Error'
##try:
##    from itertools import all
##
##except ImportError:
##    print('error')





