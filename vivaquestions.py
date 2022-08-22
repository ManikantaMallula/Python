1.What is python?
ans:
===
  Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:
== == ==== ===
web development (server-side),
software development,
mathematics,
system scripting

2).What are features of python?
ans:
====
  There are many features in Python, some of which are discussed below –

=>Easy to code: Python is a high-level programming language
=>Free and Open Source
=>Object-Oriented Language
=>GUI Programming Support
=>High-Level Language
=>Extensible feature
=>Python is Portable language
=>Python is Integrated language

3).Which types of applications we can developed by Python?
ans:
====
=>Blockchain applications
=>Command-line applications
=>Audio and Video applications
=>Game app development
=>System administration applications
=>Machine learning applications
=>Business applications

4).What is python virtual machine(pvm)?
ans:
===
  Python Virtual Machine (PVM) is a program which provides programming environment. The role of PVM is to convert the byte code instructions into machine code so the computer can execute those machine code instructions and display the output

5).What is python memory management?
ans:
====
  Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.

6)What is pep8 and tell the some pep8 standards?
ans:
====
  PEP in Python stands for Python Enhancement Proposal.It is a set of rules that specify how to write and design Python code for maximum readability.
 
=> indentation.
=> maximum line length 79 words.
=> Blank Lines.
=> Whitespaces in Expressions and Statements.
=> Naming Conventions.

7).What are keywords in python?
ans:
====
  Keywords in python are reserved words that have special meaning.They are generally used to define type of variables. Keywords cannot be used for variable or function names. There are following 33 keywords in python
  And,Or,Not,If,Elif,Else,For,While,Break,As,Def,Lambda,Pass,Return,TrueFalse,Try,With,Assert,Class,Continue,Del,Except,Finally,
  From,Global,Import,In,Is,None,Nonlocal,Raise,Yield

8.What are identifiers and its rules in python?
ans:
====
  The Python identifier is made with a combination of lowercase or uppercase letters, digits or an underscore. These are the valid characters. Lowercase letters (a to z) Uppercase letters (A to Z) Digits (0 to 9)

9.What are datatypes in python?
ans:
===
Numbers.
String.
List.
Tuple.
Dictionary
set 
boolean 
complex

10.What are literals and constants in python?
ans:-A literal is a succinct and easily visible way to write a value. Literal represents the possible choice in primitive data types for that language.
====
1. String literals
2. Numeric literals
3. Boolean literals
4.Special literals:none
5.Literal Collections
   list
   tuple
   set
   dict

11.What are comments and constants in python?
ans:
====
comments:
  Python provides three kinds of comments including block comment, inline comment, and documentation string.

Constants:
    A constant is a type of variable whose value cannot be changed. It is helpful to think of constants as containers that hold information which cannot
    be changed later.

11)What are comments in python?
a)-Comments can be used to explain the python code.
  -Comments can be used to make the code more readable.
  -Comments can be used to prevent the execution when testing code.

Examples:
#This is a comment
print("Hello, World!")

""" or '''
This is a comment
written in
more than just one line
""" or '''
print("Hello, World!")                      '''

12.What are operators and its types in python.?
ans:
===
a)-Operators are special type of functions, that takes one or more arguments and produces a new value.
Types of Operators are :

1)-Arithmatic Operator
   +,-,*,/,%,//,**
2)-Assignment Operator
   =,+=,-+,-+,/=,%=,**=,//=
3)-Relational Operator
  >,>=,<,<=,==,!=
4)-Membership Operator
   in,not in
5)-Identity Operator
   is, is not
6)-Boolean Operator
   and , or, not
7)-Bitwise Operator
   ~,&,|,^,<<,>>

13.What are generators.?
ans:
====
  A generator is a special type of function it returns an iterator object with a sequence of values. In a generator function, a yield statement is used


14.What is difference between filter() and map() and reduce()?
ans:
====
The map() Function
=== ===== =========  
 map() function is used to apply same functionality to every element.
The syntax is:
=== ====== ===
  map(function, iterable(s))

filter:
=======
   We can use filter() function to filter required values

The syntax is:
=== ===== ===
  filter(function, iterable(s))

Reduce:
=======
 reduce() function reduces the group of elements into a single element.
  
The syntax is:
=== ====== ===
reduce(function, sequence[, initial])

15.What are iterators.?
ans:
====
  An iterator is an object that contains a countable number of elements that can be iterated 

16.What is the difference between Python Arrays and lists?
Ans:
====
  Arrays and lists, in Python, have the same way of storing data. But, arrays can hold only a single data type elements whereas lists can hold any data type elements.

Example:
========
import array as arr
My_Array=arr.array('i',[1,2,3,4])
My_list=[1,'abc',1.20]
print(My_Array)
print(My_list)

Output:
=======
array(‘i’, [1, 2, 3, 4]) [1, ‘abc’, 1.2]


17.What is pickling and unpickling?
ans:
====
   pickling:
   ========
       pickle converts the python object to byte stream by using dumps. This process is known as pickling.
       #writing state of an object to a file is known as pickling.
  unpickling:
  ==========
       unpickling converts the byte stream to python object by using loads.this process is known as unpickling
       #reading state of an object from a file is known as unpickling.

18.difference between range and xrange.?
ans:
====
range() –Range will generate the list of objects.
xrange() – XRange will generate the object in 2.7 version we used.

19.What is break, continue and pass?
ans:
====
Break:
======
    The break statement in Python terminates the current loop and resumes execution at the next statement
continue:
=========
    The continue statement it will skip the particular element and transfer to next statement
pass:
=====  
   pass is a place holder it does not do anything 

20.What are functions in Python?
Ans: 
===
  A function is a block of code which is executed only when it is called. To define a Python function, the def keyword is used. 

(or)

A function is a block of code which only runs when it is called.
 yow can pass data, known as parameters, into a functions
 function is defined using def keyword.

There are 4 types of functions.
1)User Defined Function.
2)Built-in Function.-> print(),type(),input(),sorted(),max(),max(),id,(),help()....
3 )lambda Function.
04)Recursive function.

20.What are closures? 
ans:
====
  closure function is inner functions that are enclosed within the outer function is called as a closures funcations

21.What is recursive function?
ans:
====
   recursive funcation which calls itself within a function is called as recursive funcation.
example:
=======
 def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
print(fact(4))

22.what is lambda funcation.?
ans:
====
  An anonymous function is known as a lambda function. This function can have any number of parameters but, can have just one statement.
(or)
Lambda is an anonymous function in Python, that can accept any number of arguments, but can only have a single expression. 
It is generally used in situations requiring an anonymous function for a short time period.

Example:
========
a = lambda x,y : x+y
print(a(5, 6))

23.What are generators?
ans:
====
Functions that return an iterable set of items are called generators.

  A generator is a special type of function which does not return a single value it returns an iterator object with a sequence of values. In a generator function, a yield statement is used rather than a return statement.
example:
=======
  def my_gen(x):
  while(x>0):
    if x%2==0:
      yield 'Even'
    else:
      yield 'Odd'
    x-=1

for i in my_gen(7):
  print(i)

24.what is __init()__.?
ans:
====
   __init__ is a constructor  method  in Python the Constructor will be executed automatically at the time of object creation

25.what is self keyword.?
ans:
====
   self represents the instance of the class.By using the “self” keyword we can access the attributes and methods of the class in python
      
The self is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:



26.what is difference between method overloading and method overriding.?
ans:
====
  method overloading:
  ====== ============
              same funcation name and different paremeters but same class is called as a method overloading
class A():
    def prod(a,b):
        p=a+b
        print(p)
    def prod(a,b,c):
        p=a+b+c
        print(p)
x=A()
x.prod(3,5,7)

  method overriding:
  ====== ===========
              same funcation name and same paremeters but different class is called as method overriding
class A():
    def show(self):     
        print("inside A")
class B():
    def show(self):    
        print("inside B")
x=A()
y=B()
x.show()
y.show()

13)What are conditional statements(if,else,elif) and looping statements(while,for) in python?
a)-Use if to specify a block of code to be executed, if a specified condition is true. 
-Use else to specify a block of code to be executed, if the same condition is false. 
-Use else if to specify a new condition to test, if the first condition is false.

The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
The else keyword catches anything which isn't caught by the preceding conditions.

while loop
With the while loop we can execute a set of statements as long as a condition is true.
for loop
A for loop is used for iterating over a sequence.

27.What is Pythonpath?
Answer:
=======
   PYTHONPATH is an environment variable which you can set to add additional directories where Python will look for modules and packages.
   This is especially useful in maintaining Python libraries that you do not wish to install in the global default location

28.what is method.?
ans:
====
   method is a collection of varibles and attributes a is called as a method.    #The object method is the behavior of the object

29.What is monkey patching?
Answer:
=======
    In Python, the term monkey patch only refers to dynamic modifications of a class or module at run-time.


30.What is namespace in Python?
Answer: 
=======
  Namespace is a system that has unique name for each and every object in python.An object might be variable or a method.
There are global namespace and local namespace,builtin,enclosed or non local.

18) What are scope of variables?

a)Local scope and global scope
1)-Local scope: a variable which define inside the function is called local variable.
2)-global scope: a variable which defines outside the function is called global variable.
3)built-in:we have values like print,type,input,max,sorted.....
4)enclosing scope: variable is used to work with the nested function and it does not belogs to the inner function.


31.what is super().
ans:
====
  The parent class members can be accessed in child class using the super keyword.

32.Differences between Methods and Constructors:
       Method                                                                            Constructor
      =======                                                                            ===========
1. Name of method can be any name                                 1. Constructor name should be always __init__
2. Method will be executed if we call that method                 2. Constructor will be executed automatically at the time of object creation.
3. method can be called any number of times.                      3. Constructor will be executed only once
4. Inside method we can write business logic                      4. Inside Constructor we have to declare and initialize instance variables

33.Shallow:
   =======
     Shallow Copy stores the references of objects to the original memory address.  
deep copy:
==== ==== 
   Deep copy stores copies of the object's value.

34.what is decorator.?
ans:
====
  it is a structured design pattern which add the new functionality to existing funcation without changing its behavior of the structure
(or)
Decorators in Python are essentially functions that add functionality to an existing function in Python without changing the structure of the function itself. 
  -They are represented the @decorator_name in Python and are called in a bottom-up fashion


35.what is regular expression.?
ans:
====
  Regular expression represents "pattern" of the value regular expression are used to validation to check wether it is matching with specific pattern or not.

      methods:
 #search - Anywhere first match.
 # match - it should be match from first.
 # findall - list of all matches.
 # split - returns a list where the string has been split at each match.
 # sub - replaces one or more matches with a string.

36 what is Return.?
 ans:
=====
   Return statements end the execution of a function and if return is not given  by default it returns None.
37what is print.?
ans:
==== 
   Print statement shows the human user a string representing what is going on inside the computer
   #The print () function prints the specified message to the screen, or other standard output device.
38.what is package.?
ans:
====
 A package is  nothing but a collection of Python modules

38.what is module.?
ans:
====
  in every python file is module

39.what is a class.?
 ans:
=====  
    class is a collection of objects inside the class we can write our methods and constructors.

40.what is object.?
ans:
====
  object is an instance of a class

41.what is abstraction.?
ans:
====
  Hiding the internal details and showing the essential details is called as a abstraction
ex:
==
  while riding a bike, you know that if you raise the accelerator, the speed will increase, but you don’t know how it actually happens.

42.what is encapsulation.?
ans:
====
  Binding the data into single unit is called as a encapsulation
ex:
===
  company, there are different sections like the accounts section, finance section, sales section etc

there are three types of access modifiers for a class in Python.

1.Access Modifier: Public:
  ===== ===== ======
        The members declared as Public are accessible from outside the Class through an object of the class.

2.Access Modifier: Protected:
   ===== ====== =======
         The members declared as Protected are accessible from outside the class but only in a class derived from it that is in the child or subclass.
   
               According to Python convention adding a prefix _(single underscore) to a variable name makes it protected. Yes, no additional keyword required.

3.Access Modifier: Private:
   ==== ====== ======
         These members are only accessible from within the class. No outside Access is allowed.

            While the addition of prefix __(double underscore) results in a member variable or function becoming private.

43.Class method vs Static Method.?
ans:
====
  class method                                                        static method
  ===== ======                                                        ====== ======
=> class method can create a @classmethod                             =>static method can create a @staticmethod
=> class method it take cls as the first parameters                   =>in static method No specific parameters are used.
=> It can access or modify the class state.                           =>It cannot access or modify the class state.
=> It can modify class-specific details                               =>It contains totally self-contained code.

ex:
===
class student:
    age = 24
    def __init__(self,name='bhargav',age=26):
        self.name = name
        self.age = age
    def display1(self):
        print(f'{self.name}{self.age}')
    @classmethod
    def classmethod1(cls,name,age):
        print(f'{name}{age}')
    @staticmethod
    def display(age):
        if age >18:
            print('Your are eligible')
        else:
            print('your not eligible')

obj=student('bhargav',23)
obj.display1()
obj.classmethod1('vamasi',34)
obj.display(24)

44.Difference between Object-Oriented and Procedural Oriented Programming
ans:
===
Object-Oriented Programming (OOP)                                                Procedural-Oriented Programming (Pop)
======  ======= =================                                                =========== ======== =========== ====
=>It is a bottom-up approach                                                     => It is a top-down approach

=>Program is divided into objects                                                => Program is divided into functions

=>Makes use of Access modifiers
‘public’, private’, protected’                                                   => Doesn’t use Access modifiers

=>It is more secure                                                              => It is less secure

=>Object can move freely within member functions                                 => Data can move freely from function to function within programs

=>It supports inheritance                                                        => It does not support inheritance


45.what are the types of inheritance.?
ans:
====
1. Single Inheritance:
   ===== =============
          Inheriting from one class to another class is known as single inheritence
Ex:
===
  class parent:
    def m1(self):
        print("parent method")
class child(parent):
    def m2(self):
        print("chiled method")
c=child()
c.m1()
c.m2()

2. Multi level Inheritance:
   ===== ===== ===========
                inheriting from one class to another class from that class same other class is know as a Multi level Inheritance
Ex:
===
  class Parent:
    def m1(self):
        print("parent method")
class Child(Parent):
    def m2(self):
        print("child method")
class Subchild(Child):
    def m3(self):
        print("sub child method")
s=Subchild()
s.m1()
s.m2()
s.m3()
    
3.Multiple Inheritance:
 ========= ============
                 Inheriting from multiple class into a single class at a time is known as Multiple Inheritance
Ex:
===
  class Car():
    def m1(self):
        print("car method")
class Bus():
    def m2(self):
        print("Bus method")
class Van(Car,Bus):
    def m3(self):
        print("van method")
v=Van()
v.m1()
v.m2()
v.m3()

4.Hierarchical Inheritance:
  ============ ============
                Inheriting from one class to multiple class witch are present same level is known a Hierarchical Inheritance.
Ex:
===
class P:
    def m1(self):
        print("it a p class")
class C(P):
    def m2(self):
        print('it is c class')
class S(P):
    def m3(self):
        print("it is S class")
s=S()
s1=C()
s.m1()
s1.m2()
s.m3()

5.Hybrid Inheritance :
 ======= ============
   combination of single,multiple multilevel and hierarchical is known as hybrid inheritance


46.what is polymorphism.?types of polymorphism.
ans:
===
  polymorphism means one name many forms by using multiple functionality with the same name is called as a polymorphism

they are two types of polymorphism
==== === ==== ===== === ==========
 1.Static Polymorphism:
 ======== =============
  Static polymorphism (static binding) is a kind of polymorphism that occurs at compile time. An example of compile-time polymorphism is method overloading.

ex:
===
class Employee1:
    
    def name(self):
        print("My name is praveen ")
    def salary(self):
        print("My salary is 30000")
    def age(self):
        print("my age is 23")

class Employee2:
    def name(self):
        print("My name is bhargav")
    def salary(self):
        print("My salary is 50000")
    def age(self):
        print("my age is 24")
def func(obj):#\\method overloading
    obj.name()
    obj.salary()
    obj.age()
    

emp1=Employee1()
emp2=Employee2()

func(emp1)
func(emp2)
 
2.Dynamic Polymorphism:
 ========= ============
    Runtime polymorphism or dynamic polymorphism (dynamic binding) is a type of polymorphism which is resolved during runtime. An example of runtime polymorphism is method overriding.

ex:
==
 class Employee:
    def __init__(self,name,age,no,salary):
        self.name=name
        self.age=age
        self.no=no
        self.salary=salary
    def earn(self):
        pass
class Childemployee1(Employee):
    def earn(self):# method overriding
        print("no money")
class Childemployee2(Employee):
    def earn(self):
        print("has money")

c1=Childemployee1
c1.earn(Employee)
d=Childemployee2
d.earn(Employee)

33)what is multithreading and multiprocessing?
a)-multithreading:--Multithreading enables us to run multiple threads runs concurrently(randomly).
GIL (Global Interpreter Lock)-it will allow single thread line by line.
  -multiprocessing:--multiprocessing two or more processors runs at same time.

47.What is GIL in Python Mcq?
ans:
====
   Python Global Interpreter Lock (GIL) is a type of process lock which is used by python whenever it deals with processes. ... This means that in python only one thread will be executed at a time.

37)what is exception handling?
ans:-An exception is a Python object that represents an error. 
Python provides a way to handle the exception so that the code can be executed without any interruption. 
If we do not handle the exception, the interpreter doesn't execute all the code that exists after the exception.

29) What is Comprehension and its types in python?
a)-Comprehension in python provides us with short and concise way to construct new sequences(list,set,dictionary etc)using sequences

21) What is call by value and call by reference?
a)-Pass by value: Copy of the actual object is passed. Changing the value of the copy of the object will not change the value of the original object.

  -Pass by reference: Reference to the actual object is passed. Changing the value of the new object will change the value of the original object.

20) What are different types of arguments?
a)-Default arguments :Default arguments are values that are provided while defining functions.

 - Positional arguments :During a function call, values passed through arguments should be in the order of parameters in the function definition.

 - Keyword arguments : When we call a function with some values, these values get assigned to the arguments according to their position.

 -variable length argument : we can add asterik * before argument the the parameter will print how many we given in it. it gives like tuples.

 -variable length keyword argument : we can add two asterik * before the parameter and it will give output like key value pair, (dictionary).

19) What is difference between parameters and arguments?
a)-In Python, the terms parameter and argument are used interchangeably. 
 -Parameters are the input variables bounded by parentheses when defining a function, 
 -whereas arguments are the values assigned to these parameters when values passed into a function (or method) during a function call.
