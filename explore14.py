'''1.WAP to call parent class static static method from child class static method.'''

##class Teacher(object):
##
##    @staticmethod
##    def show():
##        print("Parent Class Static Method")
##
##class Student(Teacher):
##    @staticmethod
##    def display():
##        Teacher.show()
##        
##
##a=Student()
##a.display()

'''2.write demo programs for method overriding,constructor overriding,program with variable number of arguments.'''

##class P:  #method overriding
##    @staticmethod
##    def m1():
##        print("parent class method execution")
##class C(P):
##    @staticmethod
##    def m1():
##        print("child class method execution")
##a=C()
##a.m1()


##class P: #constructor overriding
##    def __init__(self):
##        print("parent class constructor execution")
##class C(P):
##    def __init__(self):
##        print("child class constructor execution")
##s=C()

##class A:
##    def sum(self,*a):
##        total=0
##        for x in a:
##            total+=x
##        print(total)
##s=A()
##s.sum()
##s.sum(10)
##s.sum(10,20)
##s.sum(10,20,30)

'''3.create one object for child class and using that object print both constructor print statemts from parent classes.'''


##class A:
##    def __init__(self):
##        print("parent class constructor execution")
##class B(A):
##    def __init__(self):
##        super().__init__()
##        print("child class constructor execution")
##a=B()



'''4.wap that take a two two strings from input and return the combination of the two string characters like below:
input:
string1="harry"
string2="micheal"
output:
['hm','ai','rc','rh','ae','ya','l']'''

s1="harry "
s2="micheal"
##op=[]
##l1=s1.split()
##l2=s2.split()
##i,j=0,0
##print(s1[2])
##
##while j<=len(s2):
##    op.append((s1[i],s2[j]))
##    i+=1
##    j+=1
##    
##print(op)

k=len(s2)
p=""
l5=[]

try:
    for i in range(k):
        for j in s1[i]:
            for m in s2[i]:
                p=j+m
                l5.append(p)

except:
    l5.append(m)



print(l5)






















