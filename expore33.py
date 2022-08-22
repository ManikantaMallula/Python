'''1) create a nested list by taking list elements from the user like below
[1,2,[3,4],[5,6,7],8,9] '''

##l=[]
##i=0
##while i<=5:
##    a=eval(input("enter list value: "))
##    l.append(a)
##    i+=1
##print(l)


''' 2) write a program on to retrieve the data from the file and use seek() and tell() method '''

##with open("a11.txt","r") as f:
##    d=f.read()
##    a=f.tell()
##    print(a)
##    f.seek(5)
##    print(f.readline())
    
    

''' 3) write a program on rlock in multithreading '''

##from threading import *
##
##class A:
##    def __init__(self, balance):
##        self.balance=balance
##        self.l=RLock()
##
##    def disp(self):
##        name = current_thread().name
##        self.l.acquire()
##        for i in range(2):
##            print(f'this is {name} thread running 2 times')
##        
##        self.l.acquire()
##        self.l.release()
##        self.l.release()
##        
##        for j in range(2):
##            print('another for loop for {name}')
##        
##a= A(3)
##t1=Thread(target=a.disp, name = 'alex')
##t2=Thread(target=a.disp, name = 'John')
##t1.start()
##t2.start()
##t1.join()
##t2.join()

''' 4) wap to create three functions and three threads for each functions and run those threads '''

##from threading import Thread
##
##def fun1():
##    print('first function')
##    
##def fun2():
##    print('second function')
##    
##def fun3():
##    print('third function')
##
##t1=Thread(target=fun1)
##t2=Thread(target=fun2)
##t3=Thread(target=fun3)
##t1.start()
##t2.start()
##t3.start()
##
##
##for i in [fun1,fun2,fun3]:
##    t=Thread(target=i)
##    t.start()
##    t.join()


''' 5) wap to print the next 100th decimal of entered user input 
input = 129, output = 200 , if input = 334, output=400 '''

##a=int(input('enter a number to print nect num'))
##
##m=100
##
##while m<a:
##    m += 100
##print(m)
    








