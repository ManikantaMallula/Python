''' Write a  Python Program using Multithreading ,
Consider a couple who is having a Joint account and both are having their ATM cards.
They come to different ATMs and try to withdraw some amount at the same time.
Let’s say the total balance in the account is 500 and Wife tries to withdraw 450
and the husband tries to withdraw 100. When they swipe the card for withdrawing money,
the balance shown will be 500. Two threads will be created for the transaction,
out of which only one thread should be successful and the other should fail.
If both the threads get successful then its a loss to the bank.
So, the threads should be in synchronization so that one fails and the other wins.'''

from threading import *

class Ja:
    def __init__(self,ab):
        self.ab=ab
        self.l=Lock()
        print("current balance in joint ac: ",self.ab)
    def wife(self,w):
        name=current_thread().name
        if w<=self.ab:
            self.l.acquire(blocking=True)
            self.ab-=w
            print(f" hi {name} {w} amount withdraw is success")
            print("current balance in joint ac: ",self.ab)
        else:
            print("sorry insuffient balance: ",self.ab)
        self.l.release()
    def hus(self,w):
        name=current_thread().name
        self.l.acquire(blocking=True)
        if w<=self.ab:
            self.ab-=w
            print(f" hi {name} {w} amount withdraw is success")
            print("current balance in joint ac: ",self.ab)
        else:
            print(f"sorry {name} insuffient balance: ",self.ab)
        self.l.release()
s=Ja(500)
t1=Thread(target=s.wife,args=(450,),name="husbund")
t2=Thread(target=s.hus,args=(450,),name="wife")
##t3=Thread(target=s.wife,args=(1000,))
t1.start()
t2.start()
##t3.start()
t1.join()
t2.join()
##t3.join()
            
        
