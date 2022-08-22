##class Tarak:
##    def walk(self):
##        print("thapak thapak thapak thapak")
##class Horse:
##    def walk(self):
##        print("tabdak tabdak tabdak tabdak")
##class Cat:
##    def talk(self):
##        print("meow meow meow meow")
##class Vadeppa:
##    def talk(self):
##        print("everytime nonsense")
##class Sravani:
##    def talk(self):
##        print("buss buss buss buss")
##a=Tarak()
##b=Horse()
##c=Cat()
##d=Vadeppa()
##e=Sravani()
##l=[a,b]
##l1=[c,d,e]
##
##def func(l):
##    for i in l:
##        i.walk()
##func(l)
##
##def fun(l1):
##    for i in l1:
##        i.talk()
##fun(l1)

##class Duck:
##    def walk(self):
##        print("thapak thapak thapak thapak")
##class Horse:
##    def walk(self):
##        print("tabak tabdak tabdak tabdak")
##
##class Cat:
##    def talk(self):
##        print("meow meow meow meow")
##class Dog:
##    def talk(self):
##        print("bow bow bow bow")
##a=Duck()
##b=Horse()
##c=Cat()
##d=Dog()
##l=[a,b,c,d]
##
##def func(l):
##    for i in l:
##        if hasattr(i,"walk"):
##            i.walk()
##        if hasattr(i,"talk"):
##            i.talk()
##func(l)

# This Method Overloading Concept is not available in Python

##class A:
##    def m(self,a):
##        print("1st method",a)
##
##
##    def m(self):
##        print("2nd method")
##s=A()
##s.m()
##s.m(10)

# Method Overloading
##class A:
##    def m(self,a=None,b=0,c=None):
##        if a!=None and b!=0 and c!=None:
##            s=a+b+c
##        elif a!=None and b!=0:
##            s=a+b
##        else:
##            s="Provide at least two numbers"
##        return s
##a=A()
##print(a.m(10,20,30))

# Method Overriding

##class A:
##    def add(self,a,b):
##        print("addition",a+b)
##class B(A):
##    def mul(self,a,b):
##        print("multiplication",a*b)
##s=B()
##s.add(10,20)
##s.mul(10,20)

# Operator Overloading

##class A:
##    def __init__(self,a):
##        self.a=a
##        

# Operator Overloading
##class A:
##    def __init__(self,a):
##        self.a=a
##
##    def __mul__(self,b):
##        return self.a*b.a
##class B:
##    def __init__(self,a):
##        self.a=a
##s=A(10)
##l=B(2)
##print(s*l)





































