## 1.Single Inheritance

##class Father:
##    money=10000
##    def show(self):
##        print("parent class instance method execution")
##
##    @classmethod
##    def showmoney(cls):
##        print("parent class method")
##
##    @staticmethod
##    def stat():
##        a=10
##        print("static class method",a)
##
##class Son(Father):
##    def display(self):
##        print("son class instance method execution")
##
##s=Son()
##s.display()
##s.show()
##s.showmoney()



# 2.Constructor in Inheritance


##class Father:
##    def __init__(self):
##        self.money=10000
##        print("father class constructor execution")
##    def show(self):
##        print("father class method execution",self.money)
##class Son(Father):
##    def display(self):
##        print("son class method execution",self.money)
##s=Son()
##s.display()
##s.show()


# 3.Constructor with Parameter in Inheritance

##class Father:
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##        print("father class constructor execution")
##    def show(self):
##        print("father class method execution",self.b)
##class Son(Father):
##    def display(self):
##        print("son class methods execution",self.a)
##s=Son(10,20)
##s.display()
##s.show()

## 4.ConstructorOverriding

class Father:
    def __init__(self):
        self.a=10
        print("father class constructor execution")

    def show(self):
        print("father class instance method execution")
class Son(Father):
    def __init__(self,b):
        self.b=b
        print("son class constructor execution")
    def display(self):
        print("son class method execution",self.b)
s=Son(20)
##s.display()
##s.show()

        
## 5.Constructor Overriding with Parameter

##class Father:
##    def __init__(self,m):
##        self.money=m
##        print("Father class constructor execution")
##    def show(self):
##        print("father class instance method execution")
##class Son(Father):
##    def __init__(self,r):
##        self.money=r
##        self.car="BMW"
##        print("son class constructor execution")
##    def display(self):
##        print("son class method execution")
##s=Son(10000)
##s.display()
##print(s.car)
##print(s.money)

    
##class Father:					
##	def __init__(self, m):
##		self.money = m
##		print("Father Class Constructor")
##		
##	def show(self):
##		print("Father Class Instance Method")
##		
##		
##class Son(Father):				
##	def __init__(self, r):
##		self.money = r
##		self.car = 'BMW'
##		print("Son Class Constructor")
##		
##	def disp(self):
##		print("Son Class Instance Method")
##
##s = Son(2000)
##print(s.money)
##print(s.car)
##s.disp()
##s.show()

# 6.Constructor with Super Method

##class Father:
##    def __init__(self):
##        print("father class constructor execution")
##
##    def show(self):
##        print("father class method execution")
##
##class Son(Father):
##    def __inif__(self):
##        super().__init__()
##        print(" son constructor execution")
##
##    def display(self):
##        print("son method execution execution")
##s=Son()
##s.show()
##s.display()

##class Father:					
##	def __init__(self):
##		print("Father Class Constructor")
##		
##	def show(self):
##		print("Father Class Instance Method")
##		
##		
##class Son(Father):
##    def __init__(self):
##        super().__init__()
##        print("Son Class Constructor")
##		
##		
##    def disp(self):
##        print("Son Class Instance Method")
##
##s = Son()
##s.disp()
##s.show()




# 7. Constructor Parameter with Super Method

##class Father:
##    def __init__(self,a):
##        self.a=a
##        print("father class constructor exevcution")
##    def show(self):
##        print("father class method execution")
##
##class Son(Father):
##    def __init__(self,a,b):
##        self.b=b
##        super().__init__(a)
##        print("son class constroctor execution")
##    def display(self):
##        print("son method execution")
##        print(self.a,self.b)
##s=Son(10,20)
##s.display()
##s.show()
##    
        

##class Father:					# Parent Class
##	def __init__(self, m):
##		self.money = m
##		print("Father Class Constructor")
##		
##	def show(self):
##		print("Father Class Instance Method:", self.money)
##		
##		
##class Son(Father):				# Child Class
##	def __init__(self, j, m):
##		super().__init__(m)		# Calling Parent Class Constructor
##		self.job = j
##		print("Son Class Constructor")
##		
##		
##	def disp(self):
##		print("Son Class Instance Method", self.job)
##
##s = Son('Python', 1000)
##s.disp()
##s.show()



























