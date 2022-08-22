#4. write a program to print prime in the given range
start=eval(input("enter starting number: "))
end=eval(input("enter end number: "))
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break 
        else:
             print(num)