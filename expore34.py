'''1. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python. '''


##def bold(func):
##    def inner():
##        return "<b>"+func()+"<\b>"
##    return inner
##
##def italic(func):
##    def inner():
##        return "<i>"+func()+"<\i>"
##    return inner
##
##def underline(func):
##    def inner():
##        return "<u>" + func() + "<\u>"
##    return inner
##@bold
##@italic
##@underline
##
##def main():
##    return "Ojas"
##print(main())
##
##def make_bold(fn):
##    def wrapped():
##        return "<b>" + fn() + "</b>"
##    return wrapped
##
##def make_italic(fn):
##    def wrapped():
##        return "<i>" + fn() + "</i>"
##    return wrapped
##
##def make_underline(fn):
##    def wrapped():
##        return "<u>" + fn() + "</u>"
##    return wrapped
##@make_bold
##@make_italic
##@make_underline
##def hello():
##    return "hello world"
##print(hello()) ## returns "<b><i><u>hello world</u></i></b>"


''' 2. Write a Python program to extract specified size of strings from a give list of string values using lambda.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8
After extracting strings of specified length from the said list:
['practice', 'solution'] '''

##l=['Python', 'list', 'exercises', 'practice', 'solution']
##
##op= list(filter(lambda x: len(x)==8, l))
##print(op)



''' 3. Write a Python program to create a deep copy of a given dictionary. Use copy.copy '''

##from copy import *
##d={"apple":100,"banana":60,"watermelon":[50,60,70]}
##d1=copy(d)
##d["banana"]=80
##print(d)


'''4. Write a Python Program to Check a Number is a Spy Number or Not? note:- without  forloop. '''

##n=int(input("enter any number to check spy or not"))
##t=n
##s=0
##m=1
##while n>0:
##    d=n%10
##    s+=d
##    m*=d
##    n=n//10
##if s==m:
##    print("given number is spy nuber")
##else:
##    print("given number is not spy nuber")

'''5. Write a Python program to find the XOR of two given strings interpreted as binary numbers.
Input:
['0001', '1011']
Output:
0b1010
Input:
['100011101100001', '100101100101110']
Output:
0b110001001111 '''



##s1='100011101100001'
##s2='100101100101110'
##s=''
##
##for i in range(len(s1)-1,-1,-1):
##    if s1[i]==s2[i]:
##        s+='0'
##    else:
##        s+='1'
##
##print(s[::-1])



 
