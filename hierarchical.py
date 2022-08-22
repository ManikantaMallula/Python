'''1. Hierarchical Inheritance '''

##class Father:
##	
##	def showF(self):
##		print("Father Class Method")
##class Son(Father):
##	
##	def showS(self):
##		print("Son Class Method")
##		
##class Daughter(Father):
##	
##	def showD(self):
##		print("Daughter Class Method")
##		
##d = Daughter()
##d.showF()
##d.showD()
##s = Son()
##s.showF()
##s.showS()


''' 2. hierarchical inheritance with constructur '''

##class Father:
##	def __init__(self):
##		print("Father Class Constructor")
##	def showF(self):
##		print("Father Class Method")
##class Son(Father):
##	def __init__(self):
##		print("Son Class Constructor")
##	def showS(self):
##		print("Son Class Method")
##		
##class Daughter(Father):
##	def __init__(self):
##		print("Daughter Class Constructor")
##	def showD(self):
##		print("Daughter Class Method")
##		
##d = Daughter()
##d.showF()
##d.showD()
##s = Son()
##s.showF()
##s.showS()
##
##
'''3. hierarchical inheritance with constructur with parameters '''


class Father:
    def __init__(self,surname):
        self.surname=surname
    def showF(self):
        print("Father surname is",self.surname)
class Son(Father):
   
    def showS(self):
        print("Son surname is ",self.surname)
		
class Daughter(Father):
   
    def showD(self):
        print("Daughter surname is",self.surname)
		
d = Daughter("chakali")
d1=Son("chakali")
d.showF()
d.showD()
d1.showS()

'''4. hierarchical inheritance with constructur over riding '''
                          

##
##class Father:
##    def __init__(self):
##        
##        self.surname="chakali"
##    def showF(self):
##        print("Father surname is",self.surname)
##class Son(Father):
##    def __init__(self):
##        self.surname="madiwal"
##   
##    def showS(self):
##        print("Son surname is ",self.surname)
##		
##class Daughter(Father):
##    def __init__(self):
##        self.surname="mallula"
##   
##    def showD(self):
##        print("Daughter surname is",self.surname)
##		
##d = Daughter()
##d1=Son()
##d1.showF()
##d.showF()
##d.showD()
##d1.showS()
##


''' 5.  hierarchical inheritance constructor over riding with parameters '''

##
##class Father:
##    def __init__(self,n):
##        
##        self.age=n
##    def showF(self):
##        print("Father name is  is",self.age)
##class Son(Father):
##    def __init__(self,m):
##        self.age=m
##   
##    def showS(self):
##        print("Son age is ",self.age)
##		
##class Daughter(Father):
##    def __init__(self,s,m):
##        self.name=s
##        self.age=m
##        self.car="bmw"
##   
##    def showD(self):
##        print("Daughter name is",self.name)
##        print("the car name is:",self.car)
##        print("the daughter is :",self.age)
##		
##d = Daughter("harini",12)
##print(d.age)
##d.showD()
##d1=Son(25)
##print(d1.age)
##d1.showS()


'''6.hierarchical inheritance Constructor with Super Method '''

##class Father:
##    def __init__(self):
##        self.surname="chakali"
##    def showF(self):
##        print("Father surname",self.surname)
##class Son(Father):
##    def __init__(self):
##        super().__init__()
##        
##    def showS(self):
##        print("Son surname",self.surname)
##		
##class Daughter(Father):
##    def __init__(self):
##        super().__init__()
##    def showD(self):
##        print("Daughter surname",self.surname)
##		
##d = Daughter()
##d.showF()
##d.showD()
##d1 = Son()
##d1.showF()
##d1.showS()
'''7.hierarchical inheritance Constructor with Super Method  with parameters'''

##
##class Father:
##    def __init__(self,surname):
##        self.surname=surname
##    def showF(self):
##        print("Father surname",self.surname)
##class Son(Father):
##    def __init__(self,surname,age):
##        super().__init__(surname)
##        self.age=age
##        
##    def showS(self):
##        print("Son surname",self.surname)
##        print("is age ia", self.age)
##		
##class Daughter(Father):
##    def __init__(self,surname,age):
##        super().__init__(surname)
##        self.age=age
##    def showD(self):
##        print("Daughter surname",self.surname)
##        print("the doughter age is ",self.age)
##		
##d = Daughter("chakali",19)
##d.showF()
##d.showD()
##d1 = Son("ckakali",25)
##d1.showF()
##d1.showS()
## 
