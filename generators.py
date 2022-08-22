##def count(n):
##    print("countdown starts")
##    while(n>0):
##        yield n
##        n=n-1
##s=count(5)
##for i in s:
##    print(i)


##def gen():
##    yield "a"
##    yield "b"
##    yield "c"
##g=gen()
####for i in g:
####    print(i)
##print(next(g))
##print(next(g))
##print(next(g))
##print(next(g))

#To generate 1st n numbers

##def gen(num):
##    n=1
##    while n<num:
##        yield n
##        n+=1
##g=gen(5)
##for i in g:
##    print(i)


##def feb():
##    a,b=0,1
##    while True:
##        yield a
##        a,b=b,a+b
##f=feb()
##
##for i in f:
##    if i<100:
##        print(i)

##l=[x*x for x in range(1000000000000000)]
##print(l[0])






##def acc():
##    total=0
##    value=None
##    while True:
##        value=yield total
##        if value is None:
##            break
##        total+=value
##generator=acc()
##next(generator)
##print(generator.send(1))
##print(generator.send(10))
##print(generator.send(100))
##print(generator.send(35))


##class A:
##    def __init__(self,n):
##        self.n=n
##    def m1(self):
##        while self.n!=1:
##            if self.n%2==0:
##                self.n=self.n//2
##                print(self.n)
##            else:
##                self.n=3*self.n+1
##                print(self.n)
##a=A(20)
##a.m1()
            

a=100
b=1000
c=a*b
d=""
for i in str(c):
    if len(d)==1 or len(d)==4:
        d+=","+"0"
    
    else:
        d+=i
print(d)






































