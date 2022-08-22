'''Write a Program to create a class by name Students, and initialize attributes like name, age,
and grade while creating an object.  '''

##class Student:
##    def __init__(self,name,age,grade):
##        self.x=name
##        self.y=age
##        self.z=grade
##    def display(self):
##        print(self.x,self.y,self.z)
##s1=Student("durga",44,"A+")
##s1.display()
        


'''Write a Program to create an empty valid class by name Students, with no properties '''
##class Empty:
##    pass
##s1=Empty()
##print(s1)


'''Write a program that prints the class name using its object. '''
##class Student:
##    pass
##print(Student().__class__.__name__)



'''Write a program, to create a child class Teacher that will inherit the properties of Parent class Staff '''

##class Staff:
##    def __init__(self,org):
##        self.org=org
##    def m1():
##        print(self.org)
##        
##class Teacher(Staff):
##    def __init__(self,DOJ,org):
##        self.DOJ=DOJ
##        self.org=org
##    def m2(self):
##        print("name of the org -",self.org,"date of joining -",self.DOJ)
##a=Teacher("ojas","10-07-2000")
##a.m2()


        
'''Create a Vehicle class without any variables and methods '''

##class Vehicle:
##    print("printing this statement without any variables and methods")



'''Create a child class Bus that will inherit all of the variables and methods of the Vehicle class  '''

##class Vehicle:
##    def __init__(self,company,brand):
##        self.company=company
##        self.brand=band
##    def m1(self):
##        print(self.company)
##class Bus(Vehicle):
##    def __init__(self,wheels,company,brand):
##        self.wheels=wheels
##        self.__init__(self,company,brand)
##    def m2(self):
##        print("company name-",self.company,"number of wheels it has-",self.wheels,self.brand)
##a=Bus(6,"Bajaj","Ex")
##a.m2()


''' Define a property that must have the same value for every class instance (object)  '''







''' Check type of an object '''

##class Master:
##    pass
##        
##    
##o=Master()
##print(type(o))



'''Write a Python program that checks if one class is a subclass of another? '''

##class Vehicle:
##    pass
##class School_bus(Vehicle):
##    pass
##
##print(issubclass(School_bus,Vehicle))





'''Determine if School_bus is also an instance of the Vehicle class '''

##class Vehicle:
##    pass
##class School_bus(Vehicle):
##    pass
##o=School_bus()
##print(isinstance(o,Vehicle))

##class Vehicle:
##    pass
##class School_bus(Vehicle):
##    pass
##o=School_bus()
##print(isinstance(o,Vehicle))









