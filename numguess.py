import random
n1=int(input("enter starting range: "))
n2=int(input("enter end range: "))
count=0
x=random.randint(n1,n2)
print(x)
if x%5==0:
        print("number is divisible of 5")
if x%3==0:
        print("number is divisible of 3")
if x%2==0:
    print("number is an even number")
if x%2!=0:
    print("number is odd number")

while count<3:
    
    guess=int(input("guess a number between {} and {}: ".format(n1,n2)))
    count+=1

    if count==2:
        print("last chance")
    elif guess<x:
              print("guessed number is very small")
    elif guess>x:
        print("guessed number is very big")
##    elif count>=2:
##        print("no more chances,game over",x)
    elif guess==x:
        print("you won the game",x)
        break
    else:
        print("No more chances")
        print("answer is: ",x)
        


