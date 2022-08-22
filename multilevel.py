''' 1. maltilevel inheritance '''
##
##class Father:
##	
##	def showF(self):
##		print("Father Class Method")
##		
##class Son(Father):
##	
##	def showS(self):
##		print("Son Class Method")
##		
##class GrandSon(Son):
##	
##	def showG(self):
##		print("GrandSon Class Method")
##		
##g = GrandSon()
##g.showF()
##g.showS()
##g.showG()

''' 2. maltilevel inheritance with constructur '''
##
##class University:
##    def __init__(self):
##        print("it is university")
##    def show(self):
##        print("it is university method")
##class Collage(University):
##    def __init__(self):
##        print("it is collage ")
##    def show1(self):
##        print("it is collage method")
##class Student(Collage):
##    def __init__(self):
##        print("it is student ")
##    def show2(self):
##        print("it is student method")
##obj=Student()
##obj.show()
##obj.show1()
##obj.show2()

''' 3. maltilevel inheritance  constructur with parametrs '''

##class University:
##    def __init__(self,name):
##        self.name=name   
##    def show(self):
##        print("it is university method")
##class Collage(University):
##    
##    def show1(self):
##        print("it is collage method")
##class Student(Collage):
##    
##    def show2(self):
##        print("the student name is ",self.name)
##       
##obj=Student('vadeppa')
##
##obj.show2()

''' 4. multi_leve inheritance constructor over riding '''

##
##class University:
##    def __init__(self):
##        self.name="vadeppa"  
##    def show(self):
##        print("it is university method",self.name)
##class Collage(University):
##    def __init__(self):
##        self.name="rakesh"
##    def show1(self):
##        print("it is collage method",self.name)
##class Student(Collage):
##    def __init__(self):
##        self.name="Tharak"
##    def show2(self):
##        print("the student name is ",self.name)
##      
##
##obj=Student()
##
##obj.show2()
##
''' 5.  multi_level inheritance constructor over riding with parameters '''


##class University:
##    def __init__(self,name):
##        self.name=name
##       
##        
##    def show(self):
##        print("it is university method")
##class Collage(University):
##    def __init__(self,sal):
##        self.sal=sal
##
##    def show1(self):
##        print("it is collage method")
##class Student(Collage):
##    def __init__(self,idno,name,sal):
##        self.idno=idno
##        self.name=name
##        self.sal=sal
##    def show2(self):
##        
##        print("the student job is ",self.idno)
##        print("the student name is ",self.name)
##        print("the student sal is ",self.sal)
##
##
##obj=Student(22070,'vadeppa',25000)
##
##obj.show2()
##


'''6.multi_level inheritance Constructor with Super Method '''

##
##class GrandFather:
##    def __init__(self):
##        self.surename="vadeppa"
##    def show(self):
##        print("it is grand father method",self.surename)
##class Father(GrandFather):
##    def __init__(self):
##        super().__init__()
##        
##    def show2(self):
##        print("the surename is ",self.surename)
##        
##      
##class Son(Father):
##    def __init__(self):
##   
## 
##        super().__init__()
##        
##    def show3(self):
##        print("it is sure name is ",self.surename)
##       
##obj=Son()
##obj.show3()
##obj.show2()
##


'''7. multi_level inheritance Constructor  Super Method with parameters '''
##class GrandFather:
##    def __init__(self, surename):
##        self.surename=surename
##    def show(self):
##        print("it is grand father method",self.surename)
##class Father(GrandFather):
##    def __init__(self,surename,car):
##        super().__init__(surename)
##        self.car=car
##    def show2(self):
##        print("the surename is ",self.surename)
##        
##        print("the surename is ",self.car)
##class Son(Father):
##    def __init__(self,surename,car,hit):
##        #super().__init__(surename,car)
##        self.hit=hit
##        super().__init__(surename,car)
##        
##    def show3(self):
##        print("it is sure name is ",self.surename)
##        print("it is car name is ",self.car)
##        print("it is hit name is ",self.hit)
##
##obj=Son("Ambani","BMW",12)
##obj.show3()
##obj.show2()
