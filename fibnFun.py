def feb():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f=feb()
for x in f:
    print(x)