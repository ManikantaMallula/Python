# Open for Appending and then reading
##f = open('pythona.jpg', mode='ab+')
##print('File Name:', f.name)
##print('File Mode:', f.mode)
##print('File Readable:', f.readable())
##print('File Writable:', f.writable())
##print('File Closed:', f.closed)
##f.close()
##print('File Closed:', f.closed)

##from pickle import *
##
##class Employee:
##    def __init__(self,ename,eid,salary):
##        self.ename=ename
##        self.eid=eid
##        self.salary=salary
##    def display(self):
##        print(self.ename,self.eid,self.salary)
##a=Employee("alex",22014,10000)
##b=Employee("john",22015,15000)
##
##
##with open("pic.txt","wb") as f:
##    dump(a,f)
##    dump(b,f)
##
##with open("pic.txt","rb") as f:
##    op=load(f)
##    op.display()


##class A:
##    def __init__(self,a):
##        self.a=a
##    def m(self):
##        print(self.a)
##class B(A):
##    def __init__(self,a,b):
##        super().__init__(a)
##        self.b=b
##    def m1(self):
##        print(self.a,self.b)
##o=B(10,20)
##from pickle import *
##
##with open("www.txt","wb") as f:
##    dump(o,f)
##print("pickling is completed")


from pickle import *
with open("www.txt","rb") as f:
    op=load(f)
f.m1()


##with open("ww.txt","r") as f:
##    a=f.readlines()
##for i in a[-3::]:
##    print(i)
    



































