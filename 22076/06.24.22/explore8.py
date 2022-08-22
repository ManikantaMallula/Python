''' 1) write a python program to print string in right angle triangle 
input:python
output:
p
p y
p y t
p y t h
p y t h o
p y t h o n'''


##s=input("enter some string: ")
##l=len(s)
##for i in range(0,l+1):
##    for j in range(0,i):
##        print(s[j]+" ",end="")
##    print()
##            


'''

2) Write a Python program to split a given dictionary of lists into list of dictionaries. '''

##d={"ravi":[10,20,30],"raju":[40,50,60]}
##l=[{"ravi":10,"raju":40},{"ravi":20,"raju":50},{"ravi":10,"raju":60}]



d={"ravi":[10,20,30],"raju":[40,50,60]}
l1=[]
l2=[]
d1={}
for k in d.keys():
    l1.append(k)
for v in d.values():
    l2.append(v)
op=d1.fromkeys(l1,l2)
for k,v in d1.items():
    x=(d3[k]==v)
    print(x)









''' 3)WPP to accept student name and marks from the keyboard and creates a dictonary.Also display student marks by taking stundent name as input. '''

##n=int(input("enter num of student: "))
##d={}
##for i in range(n):
##    name=input("enter student name: ")
##    marks=int(input("enter student marks: "))
##    d[name]=marks
##print(d)
##while True:
##    name=input("enter student name to search: ")
##    marks=d.get(name,-1)
##
##    if marks==-1:
##        print("student not found")
##    else:
##        print(name,marks)
##    option=input("do u want to find another student marks[yes/no]: ")
##    if option=="no":
##        break
##print("thanks for using app")


''' 4) write a program to print a program like below

          1   
        1   1
      1   2   1
    1   3   3   1
  1   4   4   4   1
1   5   5   5   5   1 '''
                     


##n = 5
##for i in range(n):
##    for j in range(n-i-1 ):
##        print(' ', end='')
##    for k in range(2 * i + 1):
##        print("*", end='')
##    print()





''' 5) write a function which is taking another funciton as an argument '''

##def feb():
##    a=0
##    b=1
##    def func(func):
##        a=b
##        b=a+b
##        return a,b
##    return func
##f=feb(func)
##print(f)


##def pray(text): 
##    return text.capitalize() 
##  
##def greet(func): 
##    
##    greeting = func("Hello Guys.") 
##    print(greeting)
##  
###greet(wish) 
##greet(pray) 





























