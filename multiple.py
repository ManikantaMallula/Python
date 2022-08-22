##1.multilevel inheritance
##class Father:
##    def m1(self):
##        print("father istance method execution")
##class Mother:
##    def m2(self):
##        print("mother istance method execution")
##class Son(Father,Mother):
##    def m3(self):
##        print("son class instance method execution")
##s=Son()
##s.m3()
##s.m2()
##s.m1()

        

# 2.Constructor in Inheritance
##class Father:
##    def __init__(self):
##        print("father class constructor method execution")
##
##    def m1(self):
##        print("father class method execution")
##        
##class Mother:
##    def __init__(self):
##        print("mothet class constructor execution")
##    def m2(self):
##        print("mother class method execution")
##
##class Son(Father,Mother):
##    def __init__(self):
##        print("son class constructor execution")
##    def m3(self):
##        print("son class method execution")
##s=Son()
##s.m3()
##s.m1()
##s.m2()


# 3.Constructor with Parameter in Inheritance

class Father:
    def __init__(self,a):
        self.a=a
        print("father constructor execution")
    def m1(self):
        print("father method execution",self.a)
class Mother:
    def __init__(self,b):
        self.b=b
        print("mother constructor execution")
    def m2(self):
        print("mother method execution",self.b)
class Son(Father,Mother):
    def __init__(self,a,b,c):
##        Father.__init__(self,a)
##        Mother.__init__(self,b)
        super().__init__(a)
        Mother.__init__(self,b)
        self.c=c
        
    def m3(self):
        print(self.a,self.b,self.c)
s=Son(10,20,30)
s.m3()

'''5.wap to take a list and sort the list not using the sorted or sort() method
input:  [2,5,12,6,1,4]
output:   [1,2,4,5,6,12]
and not using max() or min() method'''





















