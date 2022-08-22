'''1.write a program to print the kth largest number in the list'''

##s=[10,50,15,66,88,22]
##a=sorted(s,reverse=True)
##print(a)
##k=int(input("enter a num: "))
##print(a[k-1])    

'''2.write a finction with name sum of cubes a to b that takes two
integers and sum of cubes from a to b'''

#a=int(input("enter a value: '))


'''3.write a program to remove duplicates numbers'''
##a=input("enter some numbers: ")
##set_a=set(a)
##print(set_a)

'''4 write a program that given function will return the second character in the word passed to the function'''

##def secondchr(a):
##    msg=a[1]
##    return msg
##a=input("enter a word: ")
##print(secondchr(a))


'''5.write a program to remove n key-value pairs from the dictionary
if they present'''

b={
    "name":"raju",
    "company":"ojas"
    }
a=input().split()
for i in a:
    if i in b:
        del b[i]
print(b)








