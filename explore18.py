'''1). wap take one example duck typing,
 in this methods you must take 3 defferent classes names and in each one class you must take 3 defferent methods '''








##'''2). wap take one example wrong method overloding '''
##
##class A:      
##    def m1(self,a=None,b=0):
##        print("class a method execution")
##class B(A):
##    def m1(self,a=None,b=0):
##        print("class b method execution")
##s=B().m1(10,20)




'''3). wap solve this pattern

  5 5 5 5 5
   * * * *
    3 3 3 
     * *
      1    '''


##n=5
##for i in range(n,0,-1):
##    for j in range(n,0,-1):
##        if i>=j:
##            
##            if i%2==1:
##                print(i,end=" ")
##            else:
##                print("*",end=" ")
##        else:
##            print(" ",end="")
##    print()
##    

'''4).wap  take one eaxmple in hierarchical method '''

##
##class Father:
##    def m(self):
##        print("father class method execution")
##class Daughter(Father):
##    def m1(self):
##        print("daughter class method execution")
##class Son(Father):
##    def m2(self):
##        print("son class method execution")
##s=Son()
##s.m2()
##s.m()
##l=Daughter()
##l.m1()
##l.m()

l=[1,2,[3,4,[5,6],7],8]
l1=[]
for i in l:
    if type(i)==list:
        for j in i:
            
            if type(j)==list:
                for k in j:
                    l1.append(k)
            else:
                l1.append(j)
    else:
        l1.append(i)
    
print(l1)   









'''5). What is the difference between Python Arrays and lists take one eaxmple ? '''
