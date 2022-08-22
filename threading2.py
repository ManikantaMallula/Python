### 12. ChildThreadConstructor.py

##from threading import *
##
##class Mythread(Thread):
##    def __init__(self):
##        Thread.__init__(self)
##        print("child thread constructor printing")
##    def run(self):
##        print("child thread method printing")
##t=Mythread()
##t.start()
##print("main thread")

###13. ChildThreadConstructor2.py

##from threading import *
##
##class Mt(Thread):
##    def __init__(self,a):
##        Thread.__init__(self)
##        self.a=a
##        print("child thread constructor printing")
##    def run(self):
##        print("child thread method printing",a)
##t=Mt(10)
##t.start()
##print("main thread printing")


###14. CreateThreadWOinheriting1.py

##from threading import *
##class Mt:
####    def __init__(self,a,b):
####        self.a=a
####        self.b=b
####        print("printing mt constructor")
##    def run(self,a,b):
##        print(a,b)
##        print("printing mt method")
##t=Mt()
##
##op=Thread(target=t.m,args=(10,20))
##op.start()

###15. SingleTaskingUsingThread1.py

##from threading import *
##class M:
##    def m(self):
##        
##        self.a()
##        self.b()
##        self.c()
##    def a(self):
##        print("question 1 solved")
##    def b(self):
##        print("question 2 solved")
##    def c(self):
##        print("question 3 solved")
##o=M()
##t=Thread(target=o.m)
##t.start()

### Multitasking using Multiple Thread
##
##from threading import *
##
##class Hotel:
##    def __init__(self,t):
##        self.t=t
##    def food(self):
##        for i in range(1,6):
##            print(self.t,i)
##
##h1=Hotel("take order from table: ")
##h2=Hotel("serve order to table: ")
##t1=Thread(target=h1.food)
##t2=Thread(target=h2.food)
##t1.start()
##t2.start()

#17. MultitaskingUsingMultiThread2.py
# Multitasking using Multiple Thread
# Two Threads acting on same method

##from threading import *
##
##class Flight:
##    def __init__(self,available):
##        self.available=available
##    def book(self,need):
##        print("available seats= ",self.available)
##        if self.available>=need:
##            name=current_thread().name
##            print("{} seat is alloted for {}".format(self.available,name))
##            self.available-=need
##        else:
##            print("sorry all seats are reserved")
##f=Flight(1)
##t1=Thread(target=f.book,args=(1,),name="alex")
##t2=Thread(target=f.book,args=(1,),name="john")
##t1.start()
##t2.start()
##            

##from threading import *
##
##class F:
##    def __init__(self,a):
##        self.a=a
##        self.l=Lock()
####        print(self.l)
##    def book(self,n):
##        self.l.acquire(blocking=True)
##        if self.a>=n:
##            name=current_thread().name
##            print(f"{self.a} seat is alloted for {name}")
##            self.a-=n
##        else:
##            print("sorry no seats available")
##        self.l.release()
##f=F(2)
##t1=Thread(target=f.book,args=(1,),name="John")
##t2=Thread(target=f.book,args=(1,),name="alex")
##t3=Thread(target=f.book,args=(1,),name="smith")
##t1.start()
##t2.start()
##t3.start()
##t1.join()
##t2.join()
##t3.join()
##print("mani thread")
##                  

##from threading import *
##class F:
##    def __init__(self,a):
##        self.a=a
##        self.l=RLock()
##        print(self.l)
##    def book(self,n):
##        self.l.acquire()
##        self.l.acquire()
##        print(self.l)
##        print("available seats: ",self.a)
##        if self.a >=n:
##            name=current_thread().name
##            print(f"{self.a} seat is alloted for {name}")
##            self.a-=n
##        else:
##            print("sorry all seats has allotad")
##        self.l.release()
##        self.l.release()
##f=F(2)
##t1=Thread(target=f.book,args=(1,))
##t2=Thread(target=f.book,args=(1,))
##t3=Thread(target=f.book,args=(1,))
##t1.start()
##t2.start()
##t3.start()
##t1.join()
##t2.join()
##t3.join()
##print("main thread")

##from threading import *
##class F:
##    def __init__(self,a):
##        self.a=a
##        self.l=BoundedSemaphore(3)
##        print(self.l)
##    def book(self,n):
##        self.l.acquire()
##        print(self.l)
##        print("available seats: ",self.a)
##        if self.a>=n:
##            name=current_thread().name
##            print(f"{self.a} seat is alloted for {name}")
##            self.a-=n
##        else:
##            print("sorry all seats are alloted")
##        self.l.release()
##f=F(2)
##t1=Thread(target=f.book,args=(1,),name="John")
##t2=Thread(target=f.book,args=(1,),name="alex")
##t3=Thread(target=f.book,args=(1,),name="smith")
##t1.start()
##t2.start()
##t3.start()
##t1.join()
##t2.join()
##t3.join()
##print("mani thread")

# DeadLock
##from threading import *
##l1 = Lock()
##l2 = Lock()
##
##def bookticket():
##	l1.acquire()
##	print('Bookticket Locked on plan')
##	print('Bookticket wants to lock Class')
##	l2.acquire()
##	print('Bookingticket locked seat')
##	l2.release()
##	l1.release()
##	print('Booking ticket done')
##	
##def cancelticket():
##	l2.acquire()
##	print('cancelticket Locked on Class')
##	print('cancelticket wants to lock Plan')
##	l1.acquire()
##	print('cancelingticket locked seat')
##	l1.release()
##	l2.release()
##	print('canceling ticket done')	
##	
##t1 = Thread(target=bookticket)
##t2 = Thread(target=cancelticket)
##t1.start()
##t2.start()







