'''1.write a python program in prime number using outer and inner function and using decorator '''

##def decor(func):
##    def inner():
##        n=int(input("enter a number a to check: "))
##        c=0
##        for i in range(1,n+1):
##            if n%i==0:
##                c+=1
##        if c==2:
##            print("yes it is a prime number",n)
##        else:
##            print("noo its not a prime number",n)
##    return inner
##
##@decor           
##def main():
##    return n
##    
##main()

'''
2.write a python program in armstrong number using outer
and inner function and using decorator '''
##def decor(m):
##    def inner():
##        n=int(input("enter a number"))
##        sum1=0
##        k=len(str(n))
##        tem=n
##        while(tem>0):
##            digit=tem%10
##            sum1=sum1+digit**k
##            tem=tem//10
##        if n==sum1:
##            print("it is Armstrong number")
##        else:
##            print("it is Not Armstrong")
##    return inner
##@decor
##def new():
##    return n
##new()

'''
3.write a python program in strong number using outer and inner function and using decorator '''


##def decor(main):
##    def inner():
##        n=int(input("enter a number to find: "))
##        t=n
##        s=0
##        while t>0:
##            r=t%10
##            f=1
##            for i in range(1,r+1):
##                f=f*i
##            s+=f
##            t=t//10
##        if n==s:
##            print("yes")
##        else:
##            print("no")
##    return inner
##                
##@decor
##def main():
##    return n
##main()

'''
4.write a python program in palindrome for integers using inner and outer function and using decorator '''


##def decor(main):
##    def inner():
##        n=int(input("enrer a number to find: "))
##        t=n
##        r=0
##        while t!=0:
##            d=t%10
##            r=r*10+d
##            t=t//10
##        if n==r:
##            print("yes")
##        else:
##            main()
##            
##    return inner
##        
##@decor
##def main():
##    print("no") 
##main()

'''
5.write a python program in perfect number using outer and inner function and using decorator '''


##def decor(func):
##    def inner():
##        n=int(input("enter a number to find: "))
##        s=0
##        for i in range(1,n):
##            if n%i==0:
##                s+=i
##        if s==n:
##            print("yes")
##        else:
##            func()
##            
##    return inner
##            
##@decor
##
##def main():
##    print("no")
##
##main()


'''
6.write a python program in factorial number using outer and inner function and using decorator '''

##def decor(main):
##    def inner():
##        n=int(input("enter a number to find: "))
##        s=1
##        for i in range(1,n):
##            s=s+s*i
##        print(s)
##    return inner
##
##@decor
##def main():
##    return n
##main()


'''
7.write a python program in odd or even number using outer and inner function and using decorator '''


##def decor(main):
##    def inner():
##        n=int(input("enter a number to find: "))
##        if n%2==0:
##            print("given num is an even number")
##        else:
##            main()
##    return inner
##@decor
##def main():
##    print("givn num is an odd number")
##
##main()

'''
9.write a python program convert octal to decimal  using outer and inner function and using decorator '''

##def decor(main):
##    def inner():
##        n=int(input("enter a octal number to convert decimal: "))
##        i=1
##        s=0
##        while n>0:
##            d=n%10
##            s=s+d*i
##            i=i*8
##            n=n//10
##        print(s)
##    return inner  
##@decor
##def main():
##    pass
##main()

'''
10.write a python program in lcm number using outer and inner function and using decorator '''


##def decor(main):
##    def inner():
##        a=int(input("enter a number: "))
##        b=int(input("enter a number: "))
##        if a>b:
##            max=a
##        else:
##            max=b
##        while True:
##            if (max%a==0) and (max%b==0):
##                lcm=max
##                break
##            max+=1
##        return lcm
##            
##    return inner
##            
##@decor            
##
##def main():
##    pass
##main()






