
'''1.Define Multiple inheritance and write an example? '''
##class A:
##    def __init__(self,a):
##        self.a=a
##    def m1(self):
##        print("class a method execution",self.a)
##class B:
##    def __init___(self,b):
##        self.b=b
##    def m2(self):
##        print("class b method execution",self.b)
##class C(A,B):
##    def __init__(self,a,b,c):
##        self.c=c
##        super().__init__(a)
##        B.__init__(self,b)
##    def m3(self):
##        print("class c method execution",self.c)
##s=C("10","20","30")
##s.m3()


''' 2.WAP on Duck type polymorphism. with example '''

##class Dog:
##    def sound(self):
##        print("bowe bowe")
##    def walk(self):
##        print("it is walk")
##class Cat:
##    def sound(self):
##        print("meaw meaw")
##    def walk(self):
##        print(" it is walk")
##class Duck:
##    def sound(self):
##        print("quak quak")
##    def walk(self):
##        print("it is walk")
##a=Dog()
##b=Cat()
##c=Duck()
##l=[a,b,c]
##def anysound(l):
##    for i in l:
##        i.walk()
##        i.sound()
##anysound(l)


'''3.demonstrate strong typing method in polymorphism with example '''

####3.demonstrate strong typing method in polymorphism with example
##class Duck:
##    def walk(self):
##        print("thapak thapak")
##class Horse:
##    def walk(self):
##        print("tabdak tabdak")
##class Cat:
##    def talk(self):
##        print("Meow Meow")
##def fun(obj):
##    if hasattr(obj, 'walk'):
##        obj.walk()
##    if hasattr(obj,'talk'):
##        obj.talk()
##d=Duck()
##fun(d)
##
##h=Horse()
##fun(h)
##
##c=Cat()
##fun(c)






'''4.write a program Russian Multiplication using class and object '''
##class Mult:
##    def russian(self,a,b):
##        res=0
##        while b>0:
##            if b&1:
##                res=res+a
##            a=a<<1
##            b=b>>1
##        return res
##obj=Mult()
##print(obj.russian(4,5))
##      





'''
5.write a program about ojas organization parent class is ojas and child class is OILC
write differnt batches as methods define batchs name with inheritance.'''

##class Ojas:
##    print("welcome to Ojas")
##    def __init__(self,salary):
##        self.salary=salary
##class Oilc(Ojas):
##    def __init__(self,salary):
##        self.salary=salary
##        
##    def python(self):
##        print("python 303 batch is best batch and their salary is ",self.salary)
##    def java(self):
##        print("java people is hard working batch and their salary is ",self.salary)
##s=Oilc(10000)
##s.python()
        
















