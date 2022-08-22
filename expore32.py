'''1.write a program to count elements in a file? '''

##with open("ex.txt","r") as f:
##    c=f.read().split(" ")
##    print(c.count())
    


'''2.write a python program on atleast three magic methods?'''

##class Magic:
##
##    def __new__(cls,num):
##       
##        return super().__new__(cls)
##        
##    def __init__(self,num):
##        
##        self.num = num
##        
##    def __str__(self):
##        return('str fuction')
##
##    def __add__(self,other):
##        return self.num+other.num
##
##    def __iadd__(self,add):
##        self.num += add
##
##    def __lt__(self,other):
##        return self.num < other.num
##ob = Magic(10)
##ob2 = Magic(20)
##print(ob)
##print(ob+ob2)
##print(ob<ob2)
##ob+=34
##print(ob)


'''3.Write python program on multithreading?'''

##import threading
##
##def fun():
##    for i in range(5):
##        print('gud mrng')
##
##    for i in range(3):
##        print('happy new year')
##
##t = threading.Thread(target=fun)
##t2 = threading.Thread(target=fun)
##t.start()
##t2.start()
##t.join()
##t2.join()
##
##for i in range(4):
##    print('after thread')


'''4.Write a dictionary to a file in Python '''
##
##s = {"1":"happy", "2":"new", "3":"year"}
##
##with open('ex3.txt', 'w') as f:
##    f.write(f'{s}')


'''5.write the program to Get Yesterday’s date using Python?'''

##import datetime
##
##d = datetime.datetime.today()
##
##yesterday = d - datetime.timedelta(10)
##
##print(yesterday)









