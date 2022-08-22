s=input("enter some string : ")
l=[]
l=s.split(" ")
print(l)
count=0
word=input("enter a word to search: ")
for x in l:
    l.append(x)
    if x==word:
        count+=1
print(count)