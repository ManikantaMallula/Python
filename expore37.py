'''n1.write a python program on logging '''

##from logging import* 
##
##debug("This is Debug")
##info("This is Info")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")


'''2.write a python program to remove all the occurances of the given number '''

##l=[1,2,7,100,8,8]
##a=8
##k=[]
##for i in l:
##    if i!=a:
##        k.append(i)
##print(k)

''' 3.write a python program to exact the numbers in a given string and print sum,minimum and maximum of those numbers '''

##l=input("enter the string")
##op=[]
##for i in l:
##    if i.isdigit():
##        op.append(int(i))
##print(max(op))
##print(min(op))
##print(sum(op))

'''4.write a python program on sprial number 
eg:-9 8 7     
    2 1 6        
    3 4 5 '''


##l=[[0 for i in range(a)] for j in range(a)]
##n=9
##low=0
##high=a-1
##count=int(a+1)//2
##
##for i in range(count):
##    for j in range(low,high+1):
##        l[i][j]=n
##        n-=1
##    for j in range(low+1,high+1):
##        l[j][high]=n
##        n-=1
##    for j in range(high-1,low-1,-1):
##        l[high][j]=n
##        n-=1
##    for j in range(high-1,low,-1):
##        l[j][low]=n
##        n-=1
##    low+=1
##    high-=1
##    
##for i in range(a):
##    for j in range(a):
##        print(l[i][j],end=" ")
##    print()








'''    
5.create a list of combinations of entered number like below
input: 5
list must be created as [4,4,4,33,33,22,22,1,1,1]'''


##a=int(input("enter tghe number: "))
##l=[]
##for i in range(a-1,0,-1):
##    if i==1 or i==a-1:
##        l.append(i)
##        l.append(i)
##        l.append(i)
##    else:
##        l.append(str(i)*2)
##        l.append(str(i)*2)
##print(l)
##        

'''5.create a list of combinations of entered number like below
input: 5
list must be created as [4,4,4,33,33,22,22,1,1,1] '''

##a=int(input("enter tghe number: "))
##l=[]
##for i in range(a-1,0,-1):
##    if i==1 or i==a-1:
##        l.append(i)
##        l.append(i)
##        l.append(i)
##    else:
##        l.append(str(i)*2)
##        l.append(str(i)*2)
##print(l)
##        


##import turtle
##turtle.speed(3)
##turtle.bgcolor('black')
##turtle.pensize(3)
##def func():
##    for i in range(200):
##        turtle.right(1)
##        turtle.forward(1)
##turtle.color('red', 'pink')
##turtle.begin_fill()
##turtle.left(140)
##turtle.forward(111.65)
##func()
##turtle.left(120)
##func()
##turtle.forward(111.65)
##turtle.end_fill()
##turtle.hideturtle()
##turtle.done()
