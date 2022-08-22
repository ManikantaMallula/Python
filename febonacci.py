n=eval(input("enter the range: "))
a=0
b=1
for x in range(n):
    a,b=b,a+b
    print(a)
    print(b)