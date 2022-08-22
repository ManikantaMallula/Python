##st = list('hello beautiful world')
##s = " "
##st1 = []
##for i in range(len(st)):
##  if st[i] == s:
##    st1.pop(i-1)
##    st[i-1],st[i+1] = st[i+1],st[i-1]
##    st1.append(st[i-1])
##    st1.append(s)
##    st1.append(st[i+1])
##    st1.pop(i+1)
##  else:
##    st1.append(st[i])
##print(''.join(st1))

##========================================================================

##n=int(input("enter number of rows: "))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print(j,end=" ")
##    print()
    
##====================================================================
    
##n=int(input("enter num of rows: "))
##for i in range(1,n+1):
##    m=n
##    for j in range(1,n+1):
##        print(m,end=" ")
##        m=m-1
##    print()
##
##======================================================================

##n=int(input("enter num of rows: "))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print(n+1-i,end=" ")
##    
##    print()
##
####======================================================================

##n=int(input("enter number of rows: "))
##for i in range(1,n+1):
##    for j in range(1,i):
##        print(j,end=" ")
##    print(i)

##===============================
n=int(input("enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()











    
