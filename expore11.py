'''1.write a python program to find the Nth term in a fibonacci series using recursion.  '''

##def feb(n):
##    if n<=0:
##        return 0
##    elif n<=1:
##        return 1
##    else:
##        return (feb(n-1)+feb(n-2))
##n=int(input("enter Nth term number to find: "))
##print(feb(n))


'''
2.write a python program to implement matrix multiplication '''

##s=[[1,2,3],[4,5,6],[7,8,9]]
##l=[[10,20,30],[40,50,60],[70,80,90]]
##y=[[0,0,0],[0,0,0],[0,0,0]]
##
##for i in range(len(s)):
##    for j in range(len(s[0])):
##        for k in range(len(y)):
##            y[i][j]=y[i][j]+(s[i][j]*l[j][i])
##for i in y:
##    print(i)




'''
3.write a python program to draw a circle of square using turtle.'''



def square(side_length):
    for i in range(4):
        turtle.fd(side_length)
        turtle.lt(90)

square (150)

turtle.penup()
        ####New Square###
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(30)
turtle.right(180)
turtle.right(45)
turtle.pendown()


def square(side_length):
    for i in range(4):
        turtle.fd(side_length)
        turtle.lt(90)
square (150)




''' 4.write a python program even and odd using list comprehension. '''



##l=[i for i in range(1,20) if i%2==0]
##l1=[i for i in range(1,20) if i%2!=0]
##
##print(l)
##print(l1)



'''
5.write a python program  to print the number from a given number N till 0 using recursion. '''

##def recur(n):
##    if n>0:
##        print(n)
##        
##    return recur(n-1)
##print(recur(20))
