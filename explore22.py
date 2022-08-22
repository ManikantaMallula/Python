'''
1.write a python program in shutil module using copy method
'''
##import shutil
##source=r"C:\Users\em22076\Desktop\files.txt"
##destination=r"C:\Users\em22076\Desktop\files1.txt"
##shutil.copyfile(source,destination)
'''
2.write a python program in os module using rename method
'''
##import os
##source=r"C:\Users\em22076\Desktop\files1.txt"
##destination=r"C:\Users\em22076\Desktop\newfiles1.txt"
##os.rename(source,destination)
'''
3.write a python program in fibonacci series using outer and inner functions
'''
##def outer(n):
##    def inner():
##        a=0
##        b=1
##        for i in range(n):
##            c=a+b
##            a=b
##            b=c
##            print(c)
##    return inner()
##num=int(input("enter range:"))
##outer(num)
    
'''
4.write a python program in heapq module
'''
##import heapq
##a=[4,7,3,4,5,2,1]
##heapq.heapify(a)
##print(a)
##heapq.heappush(a,11)
##print(a)
##heapq.heappop(a)
##print(a)
##heapq.heapreplace(a,1)
##print(a)
'''
5.write a python program in shallow copy and deep copy
'''
######shallow copy####
##l1=[[1,2,3],[4,5,6]]
##l2=l1.copy()
##print(l2)
##l1[1][2]=8
##print(l1)
##print(l2)
######Deep copy####
##import copy
##l1=[[1,2,3],[4,5,6]]
##l2=copy.deepcopy(l1)
##print(l2)
##l1[1][1]=89
##print(l1)
##print(l2)
