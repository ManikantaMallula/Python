''' 1)Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input. '''

##s=input("enter some string of words: ")
##u=0
##l=0
##for i in s:
##    if i.isupper():
##        u+=1
##    elif i.islower():
##        l+=1
##    else:
##        pass
##print("UPPER CASE ",u)
##print("LOWER CASE ",l)
        

'''  2)Python Program to Remove the ith Occurrence of the Given Word in a List. '''

##s=input("enter some words: ")
##l=s.split(" ")
##print(l)
##rm=int(input("enter a sub string to remove: "))
##l.pop(rm)
##print(l)


'''  3)Python Program to Merge Two Lists and Sort it. '''

##s=input("enter some values: ")
##l=s.split(" ")
##print(l)
##s1=input("enter some values: ")
##l1=s1.split(" ")
##print(l1)
##op=l+l1
##print(sorted(op))


'''  4)Python Program to Find the Gravitational Force between Two Objects. '''

''' Fg = refers to the gravitational force between two objects (N = kg⋅m/s2)
G = refers to the gravitational constant (G = 6.67 ×10−11N⋅m2/kg2)
m1 = refers to the mass of the first object in kilogram
m2 = refers to the mass of the second object also in kilogram
r = refers to the distance between the object in meters '''

##fg=int(input("enter gravitational force between two objects: "))
##m1=int(input("mass of the first object in kilogram: "))
##m2=int(input("mass of the second object in kilogram: "))
##r=int(input("enter distance between the object in meters: "))
##G =int(input("enter gravitational constant: "))
##
##gf=print((G*m1*m2)/r**2,"N")




'''  5) Write a Python Program for Even Number Pyramid Pattern '''

'''     0
       2 4
      6 8 10
     12 14 16 18 '''

##
##n=2
##for x in range(1,5):
##    for y in range(5,x,-1):
##        print(" ",end="")
##    for j in range(0,x):
##        print(str(n)+" ",end="")
##        n=n+2
##    print()
##        








































