s=input("enter some string: ")
f=input("enter a letter to find num of times occurred: ")
result=0
for x in s:
  if x==f:
    result+=1
print(result)
