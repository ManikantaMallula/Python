first_number=int(input("enter a first number: "))
second_number=int(input("enter second number: "))
for i in range(first_number,second_number+1):
    num1=i
    num2=i
    sum=0
    while num1!=0:
        fact=1
        rem=num1%10
        num1=int(num1/10)
        for j in range(1,rem+1):
            fact=fact*j
        sum=sum+fact
    if sum==num2:
        print(i)

'''n=int(input("enter a number to find: "))
sum=0
temp=n
while temp>0:
    fact=1
    rem=temp%10
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    temp=temp//10
if n==sum:
    print("given number is a strong number")
else:
    print("given number is not a strong number") '''

