''' itertools.combinations will return a generator of the
k-combination sequence of a list.​

In other words: It will return a generator of
tuples of all the possible k-wise combinations of the input list. '''

##from itertools import *
##a=[1,2,3,4,5]
##b=list(combinations(a,2))
##print(b)

##from itertools import *
##def even(n):
##    return n%2==0
##l=[0,2,4,12,18,13,14,22,23,44]
##r=list(dropwhile(even,l))
##print(r)

from itertools import *

def groupby(l):
    groups=groupby(l,key=lambda x:x[1])
    for key,group in groups:
        print(key,list(group))
l = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)]
groupby(l)
