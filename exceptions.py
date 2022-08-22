##a=10
##b=0
##try:
##    print(a/b)
##    print("inside try")
##except ZeroDivisionError:
##    print("division by zero not allowed")
##print("rest of the code")


##a=10
##b=0
##try:
##    print(a/b)
##    print("inside try")
##except ZeroDivisionError:
##    print("division by zero is not possible")
##else:
##    print("inside else")
##print("rest of the code")

##a=10
##b=0
##try:
##    print(a/b)
##    print("inside try")
##except ZeroDivisionError:
##    print("division by zero is not possible")
##else:
##    print("inside else")
##finally:
##    print("inside finally block")
##
##print("rest of the code")

##a=10
##b=0
##try:
##    print(a/b)
##    print("inside try")
##except ZeroDivisionError as o:
##    print(o)
##print("rest of the code")

##a=10
##b=0
##try:
##    print(a/o)
##    print("inside try")
##except ZeroDivisionError as o:
##    print(o)
##except NameError as o:
##    print(o)
##print("rest of the code")


##a=10
##b=0
##try:
##    print(a/o)
##    print("inside try")
##except (ZeroDivisionError,NameError) as o:
##    print(o)
##
##print("rest of the code")


##a=10
##b=0
##try:
##    print(a/b)
##except:
##    print("exception handler")
##print("rest of the code")

##a=20
##assert a>=10, "invalid number"
##print("no error")
##assert a<=10, "invalid number"

##class Balance(Exception):
##    def __init__(self,a):
##        self.a=a
##        
##def check():
##    m=10000
##    w=9000
##    try:
##        bal=m-w
##        if(bal<=2000):
##            raise Balance("insufficient balance")
##        print(bal)
##    except Balance as b:
##        print(b)
##check()
        
