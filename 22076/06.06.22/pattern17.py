'''1. Write a program to print the following Patterns
  1 2 3 4 5 
  1 2 3 4 5  
  1 2 3 4 5 
  1 2 3 4 5 
  1 2 3 4 5 '''
##n=int(input("enter number of rows: "))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print(j,end=" ")
##    print()

''' 2.Write a program to print the following Pattern
  5 4 3 2 1 
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1 '''


##n=int(input("enter num of rows: "))
##for i in range(1,n+1):
##    m=n
##    for j in range(1,n+1):
##        print(m,end=" ")
##        m=m-1
##    print()

''' 3.Write a program to print the following Pattern
  5 5 5 5 5 
  4 4 4 4 4 
  3 3 3 3 3 
  2 2 2 2 2 
  1 1 1 1 1 '''

##n = int(input("enter num of rows: "))
##for i in range(1, n + 1):
##    for j in range(1, n + 1):
##        print(n + 1 - i, end=" ")
##
##    print()

''' 4.Write a program to print the following Pattern
  1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5 '''

##n=int(input("enter number of rows: "))
##for i in range(1,n+1):
##    for j in range(1,i):
##        print(j,end=" ")
##    print(i)


'''5.Write a program to print the following Pattern
  1 
  2 2 
  3 3 3 
  4 4 4 4 
  5 5 5 5 5 '''
##n=int(input("enter num of rows: "))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(i,end=" ")
##    print()

''' 6.Write a program to print the following Pattern
  1 
  2 3  
  4 5 6 
  7 8 9 10 
  11 12 13 14 15 '''
##
##n=1
##for i in range(6):
##    for j in range(i):
##        print(n,end=" ")
##        n=n+1
##
##    print()


''' 7.Write a program to print the following Pattern
  5 
  4 4 
  3 3 3 
  2 2 2 2 
  1 1 1 1 1 '''

##n=5
##for i in range(5):
##    for j in range(0,i+1):
##        print(n-i,end=" ")
##        
##    print()
    

''' 8.Write a program to print the following Pattern
  1 
  2 3 
  3 4 5 
  4 5 6 7 
  5 6 7 8 9 '''

##n=6
##for i in range(n):
##    for j in range(i):
##        print(i,end=" ")
##        i=i+1
##    print()


'''9.Write a program to print the following Pattern
  A 
  B C
  D E F
  G H I J
  K L M N O '''

##value=65
##for i in range(1,6):
## for j in range(i):
##     print(chr(value),end=" ")
##     value=value+1
## print()


''' 10.Write a program to print the following Pattern
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * '''

##for i in range(6):
##    for j in range(6):
##        print("*",end=" ")
##    print()


''' 11.Write a program to print the following Pattern
   * 
   * * 
   * * * 
   * * * * 
   * * * * * '''

##n=6
##for i in range(n):
##    for j in range(i):
##        print("*",end=" ")
##        
##    print()
##    



''' 12.Write a program to print the following Pattern
    * * * * * 
    *       * 
    *       * 
    *       * 
    * * * * *  '''

##n=5
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if (i==1 or i==n or j==1 or j==n):
##            print("*" ,end=" ")
##        else:
##            print(" ",end=" ")
##    print()

''' 13.Write a program to print the following Pattern
          * 
        * * * 
      * * * * * 
    * * * * * * * '''

##n=5
##for i in range(1,n+1):
##    print(" "*(n-i),"*"*(2*i-1))


''' 14.Display Multiplication Table in given range using Nested for loops
15.Display Prime Numbers in the given range using nested for loops 

16.Write a program to print the following Pattern
	1
              3  2
       6   5   4
10  9   8   7   '''

'''  17.Write a program to print the following Pattern
10  9  8   7
     6   5  4
           3  2
               1 '''




n=1
k=4
for i in range(4):
    print(k*"  ",end=" ")
    k-=1
    for j in range(i):
        print(n,end=" ")
        n=n+1
    print()
 

##n=10
##for i in range(4):
##    space="  "*i
##    print(space,end=" ")
##    for j in range(4-i):
##        print(n,end=" ")
##        n=n-1
##    print("")


##n=10
##k=0
##for i in range(4,0,-1):
##    print(k*" ",end=" ")
##    k+=4
##    for j in range(i):
##        print(n,end=" ")
##        n=n-1
##    print()
        


##n=10
##space=0
##for i in range(4):
##    print(space*" ",end=" ")
##    space+=4
##    for j in range(4-i):
##        print(n,end=" ")
##        n=n-1
##    print()





##n=10
##k=0
##for i in range(4):
##    print(k*" ",end=" ")
##    k+=4
##    for j in range(4-i):
##        print(n,end=" ")
##        n=n-1
##    print()




































