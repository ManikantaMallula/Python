'''1) Find number of small words in a string and their length?
eg:-This is an offical page
output:- is-2 
         an-2 '''


##l="This is an offical page".split()
##l1=[]
##for i in l:
##    l1.append(len(i))
##m=min(l1)
##for j in l:
##    if len(j)==m:
##        print(j,len(j))


    
    








'''2) Find palindrome in a given string small and large words?
eg:- mom and dad speak malayalam with nitin
mom
dad
malayalam '''


##l="mom and dad speak malayalam with nitin".split()
##l1=[]
##l2=[]
##for i in l:
##    if i==i[::-1]:
##        l1.append(i)
##for j in l1:
##    l2.append(len(j))
##m=min(l2)
##n=max(l2)
##
##for k in l1:
##    if len(k)==m:
##        print("small word= ",k)
##    elif len(k)==n:
##        print("large word= ",k)






'''3) Find the digit is binary or not?
eg:-1011
is binary number

24:-
its is not a binary '''

##n=int(input("enter a number to find: "))
##
##while n>0:
##    r=n%10
##    if r!=0 and r!=1:
##        print("given number is not a binary number")
##        break
##    n=n//10
##    if n==0:
##        print("given number is a binary number")
##    
    




'''
4)Write a program to print the emojis.
😀
😘
🤗
😪
😷 '''


##
##print('\U0001F600')
##print('\U0001F618')
##print('\U0001F917')
##print('\U0001F62A')
##print('\U0001F637')


'''
5)WAP Login email page ?

example:- email_id='Prudhvi1998@gamil.com'
          password='Rolex123'

if email_id and password True 

output:- prudhvi your email-id successfully open

if email_id or password False

Prudhvi your enter wrong password try agin '''



##original_id="Prudhvi1998@gamil.com"
##original_pass="Rolex123"
##
##email=input("enter your email-id: ")
##passw=input("enter your password: ")
##if email==original_id and passw==original_pass:
##    print("prudhvi your email-id successfully open")
##else:
##    print("Prudhvi your enter wrong password try agin")
##    email=input("enter your email-id: ")






















