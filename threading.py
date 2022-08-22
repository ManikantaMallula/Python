##from threading import *
##t=current_thread().getName()
##print(t)

##from threading import *
##def disp():
##    print("thread running")
##t=Thread(target=disp)
##t.start()
##print(current_thread().getName())

##from threading import *
##def disp(a,b):
##    print(a,b)
##t=Thread(target=disp,args=(10,20))
##t.start()
##
##import statistics
##
### Calculate the variance from a sample of data
##print(statistics.variance([1, 3, 5, 7, 9, 11]))
##print(statistics.variance([2, 2.5, 1.25, 3.1, 1.75, 2.8]))
##print(statistics.variance([-11, 5.5, -3.4, 7.1]))
##print(statistics.variance([1, 30, 50, 100]))
##
##input:
##[1, 3, 5, 7, 9, 11])
##[2, 2.5, 1.25, 3.1, 1.75, 2.8]
##[-11, 5.5, -3.4, 7.1])
##[1, 30, 50, 100]
##
##output:
##14
##0.47966666666666663
##70.80333333333333
##1736.9166666666667


##from threading import *
##def disp(a,b):
##    print(a,b)
##for i in range(5):
##    t=Thread(target=disp,args=(10,20))
##    t.start()

##from threading import *
##def disp():
##    for i in range(5):
##        print("child thread running")
##t=Thread(target=disp)
##t.start()
##for i in range(5):
##    print("main thread")

##from threading import *
##def disp():
##    print("child thread: ",current_thread())
##    print("default child thread: ",current_thread().getName())
##    current_thread().setName("doc thread")
##    print("new name: ",current_thread().getName())
##    
##t=Thread(target=disp)
##t.start()
##
##print("main thread: ",current_thread())
##print("default main thread: ",current_thread().getName())
##current_thread().setName("ojas")
##print("new name: ",current_thread().getName())

##from threading import *
##
##def disp():
##    pass
##t=Thread(target=disp)
##print("default thread name: ",t.getName())
##t.setName("ojas")
##print("default thread new name: ",t.getName())

##from threading import *
##def disp():
##    pass
##t=Thread(target=disp)
##t.start()
##print(t.name)

##from threading import *
##class Mythread(Thread):
##    print("priting mythread")
##t=Mythread()
##t.start()
##print(t.name)









