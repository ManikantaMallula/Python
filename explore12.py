''' 1.write a python program using oops concept finding prime number or not '''

##class Prime:
##    def __init__(self,n):
##        self.n=n
##    def checking(self):
##        count=0
##        if n>2:
##            for i in range(2,n+1):
##                if n%i==0:
##                    count+=1
##            if count==2:
##                print("Yes its a prime number")
##            else:
##                print("Yes its a prime number")
##                
##
##n=int(input("enter a number to check :"))                    
##a=Prime(n)
##a.checking()
        

''' 2.write a program on instance method, static method, class method using some examples '''

##class Methods:
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def instance(self):
##        print("instance method execution-",self.a,self.b)
##
##    @classmethod
##    def classm(cls,c):
##        cls.c=c
##        print("class method execution-",cls.c)
##
##    @staticmethod
##    def statm(d):
##        print("static method execution-",d)
##s=Methods(10,20)
##s.instance()
##s.classm(30)
##s.statm(40)



''' 3.write a program on single inheritance '''

##class Parent:
##    def __init__(self,surname):
##        self.surname=surname
##    def m1(self):
##        print(self.surname)
##class Child(Parent):
##    def __init__(self,name,surname):
##        self.name=name
##        super().__init__(surname)
##    def m2(self):
##        print(self.surname,self.name)
##s=Child("Chakali","vadeppa")
##s.m2()
##s.m1()



''' 4.write a python program using oops concepts find a fibonacci series '''

##class Feb:
##    def __init__(self,n):
##        self.n=n
##    def febb(self):
##        a,b=0,1
##        while b<50:
##            a,b=b,a+b
##            print(b)
##
##n=50            
##f=Feb(n)
##f.febb()

            
        





''' 5.write a python program using oops concepts find armstrong number '''

##class Armstrong:
##    def __init__(self,n):
##        self.n=n
##        
##    def check(self):
##        sum=0
##        temp=self.n
##        while temp>0:
##            rem=temp%10
##            sum+=rem**3
##            temp=temp//10
##        if sum==self.n:
##            print("YES Armstrong number")
##        else:
##            print("Not an Armstrong number")
##n=int(input("Enter a number:"))
##s=Armstrong(n)
##s.check()
##            
        




























