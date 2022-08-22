''' 1.Create a class Teacher with name, age, and salary attributes,
where salary must be a private attribute that cannot be accessed outside the class. '''

##class Teacher:
##    def __init__(self):
##        self.name="Vadeppa"
##        self.age=26
##        self.__salary=50000
##    def display(self):
##        print(self.name,self.age,self.__salary)
##s=Teacher().display()


##class Teacher:
##    name="Vadeppa"
##    age=26
##    __salary=50000
##
##    def display(self):
##        print(self.name,self.age,self.__salary)
##s=Teacher().display()
##print(Teacher.name)
##print(Teacher.__salary)


''' 2.Write a Python class Square, and define two methods that return the square area and perimeter. '''

##class Square:
##    def __init__(self,n):
##        self.n=n
##
##    def squareArea(self):
##        print("square of the area :",self.n**2)
##    def perimeter(self):
##        print("perimeter :",self.n*4)
##s=Square(100).squareArea()
##s1=Square(100).perimeter()




''' 3.How to copy all properties of an object to another object in Python? '''

##class Copy:
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def m1(self):
##        print(self.a,self.b)
##s1=Copy(10,20)
##s1.m1()
##s2=s1
##s1.m1()


''' 4.Create a method called Factorial() which allows to calculate the factorial of an integer.  
Test the method by instantiating the class.  ''' 

##class Fact:
##    def __init__(self,n):
##        self.n=n
##    def Factorial(self):
##        fact=1
##        for i in range(1,n+1):
##            fact=fact*i
##        print(fact)
##n=int(input("enter some number to find factorial :"))
##s=Fact(n).Factorial()





''' 5.Create a student object via an instantiation on the Student class and then test the displayStudent method. '''



class Student:
    def display(self):
        print("isplayStudent method execution")
s=Student().display()
        
















































