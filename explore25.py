'''
1.write a python program do multiplication program using generators and use sys module to find memory size
'''

##def gen(n):
##    for i in range(1,11):
##        yield i,"x",n,"=",i*n
##n=3
##g=gen(n)
##for i in g:
##    print(i)
    


'''
2..write a python program do multiplication program using function
'''
##def func():
##    n=int(input("enter which num table you want: "))
##    for i in range(1,11):
##        print("{} {} {} {} {}".format(i,"X",n,"=",i*n))
##func()


'''
3.Write a Python program to extract characters from various text files and puts them into a list.
'''

##with open("b11.txt","r") as f:
##    l=[]
##    a=f.readlines()
##    for i in a:
##        l.append(i)
##print(l)



'''
4. Write a Python program to create a file where all letters of English alphabet are listed by specified number
of letters on each line.
'''

from string import *
with open("n.txt","w") as f:
    n=int(input("enter how step  value: "))
    a=ascii_lowercase
    print(a)
    l=[a[i:i+n]+"\n" for i in range(0,len(a),n)]
    op=f.writelines(l)
print(op)




'''
5.write a python program in twin prime using outer and inner functions
'''





















