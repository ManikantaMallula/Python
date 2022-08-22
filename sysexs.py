'''1.write a python program in prime number using outer and inner function '''

##from sys import argv
##num=int(argv[1])
##count=0
##for i in range(1,num):
##    if num%i==0:
##        count+=1
##if count>1:
##    print("Not prime")
##else:
##    print("Prime")

'''2.write a python program in armstrong number using outer and inner function'''
##from sys import argv
##num=int(argv[1])
##s=0
##temp=num
##while temp>0:
##    r=temp%10
##    s+=r**3
##    temp=temp//10
##if num==s:
##    print("Armstrong")
##else:
##    print("Not Armstrong")
'''3.write a python program in strong number using outer and inner function'''
##from sys import argv
##from math import factorial
##num=int(argv[1])
##temp=num
##s=0
##while temp>0:
##    r=temp%10
##    s=s+factorial(r)
##    temp=temp//10
##if num==s:
##    print("Strong number")
##else:
##    print("Not strong number")

'''4.write a python program in palindrome for integers using inner and outer function'''
##from sys import argv
##num=int(argv[1])
##s=0
##temp=num
##while temp>0:
##    r=temp%10
##    s=s*10+r
##    temp=temp//10
##if num==s:
##    print("Palindrome")
##else:
##    print("Not palindrome")
'''5.write a python program in perfect number using outer and inner function'''
##from sys import argv
##num=int(argv[1])
##a=[]
##for i in range(1,num):
##    if num%i==0:
##            a.append(i)
##if sum(a)==num:
##    print("perfect number")
##else:
##    print("Not a perfect number")

'''6.write a python program in factorial number using outer and inner function'''
##from sys import argv
##num=int(argv[1])
##fact=1
##while num>0:
##    fact=fact*num
##    num=num-1
##print(fact)


'''7.write a python program in odd or even number using outer and inner function'''
##from sys import argv
##num=int(argv[1])
##if num%2!=0:
##    print("odd number")
##else:
##    print("even number")
'''8.write a python program in even or odd number using outer and inner function'''
##from sys import argv
##num=int(argv[1])
##if num%2==0:
##    print("even number")
##else:
##    print("odd number")
'''9.write a python program convert octal to decimal  using outer and inner function'''
##from sys import argv
##num=int(argv[1])
##s=0
##temp=num
##i=1
##while(temp):
##    digit=temp%10      
##    s+=digit*i
##    i=i*8
##    temp=temp//10
##print(s)
     
##
##'''10.write a python program in lcm number using outer and inner function '''
##from sys import argv
##num1=int(argv[1])
##num2=int(argv[2])
##if num1>num2:
##    big=num1
##else:
##    big=num2
##while(True):
##    if(big%num1==0) and (big%num2==0):
##            lcm=big
##            break
    big+=1
print(lcm)
