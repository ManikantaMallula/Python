n=int(input("enter num of rows: "))
for i in range(1,n+1):
    m=n
    for j in range(1,n+1):
        print(m,end=" ")
        m=m-1
    print()
