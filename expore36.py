'''1) wap to create class and create two
objects from that class and add those two objects using _add_
(operator overloading)'''

##class Employee:
##    def __init__(self,name,salary):
##        self.name=name
##        self.salary=salary
##
##    def emp_Details(self):
##        print("The Name of the Employee is {} and Salary is {}".format(self.name,self.salary))
##
##    def __add__(self,other):
##        return self.salary+other.salary
##
##e1=Employee("tarak",999990)
##e2=Employee("mohan",999999)
##print(e1+e2)


'''2) wap to create a generator by using send method'''

##def func():
##    while True:
##        val = yield
##        yield val*10
##
##
##g=func()
##next(g)
##print(g.send(1))
##next(g)
##print(g.send(10))
##next(g)
##print(g.send(100))

'''3) wap to create the generator comprehension '''
##gen=(i**2 for i in range(1,11))
##for i in gen:
##    print(i)
'''
4) print a function n number of times using decorator '''

##def calculation(func):
##    def calc(*args,**kwargs):
##        cal=func(*args,**kwargs)
##        return cal
##    return calc
##@calculation
##def addition(a,b):
##    return a+b
##@calculation
##def subtraction(a,b):
##    return a-b
##@calculation
##def multiplication(a,b):
##    return a*b
##@calculation
##def division(a,b):
##    return a*b

''' 5) write a python program to check the how many instance variables are there in a class. '''

##import itertools
##class Employee:
##    counter=0
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##        Employee.counter +=1
##obj1=Employee("Bazequa",23)
##obj2=Employee("Fatima",23)
##obj3=Employee("Sravani",21)
##obj4=Employee("Cherpaly",21)
##print(Employee.counter)

