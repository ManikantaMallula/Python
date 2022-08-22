'''1.Write a Python program to triple all numbers of a given list of integers. Use Python map.'''

##l=(1,2,3,4,5,6,7,8)
##op=map(lambda x:x+x+x,l)
##print(list(op))

'''2. Write a Python program to add three given lists using Python map and lambda.'''

##l=(1,2,3,4,5,6,7,8)
##op=map(lambda x:x+3,l)
##print(list(op))

'''3. Write a Python program to listify the list of given strings individually using Python map '''

##l=["apple","ball","Car"]
##op=map(list,l)
##print(list(op))

'''4. Write a Python program to create a list
containing the power of said number in bases raised to the corresponding number in the index using Python map'''

##l=[10,20,30,40,50,60,70,80]
##index=[1,2,3,4,5,6,7,8,9]
##op=list(map(pow,l,index))
##print(op)

'''5. Write a Python program to square the elements of a list using map() function.'''

##l=[10,20,30,40,50,60,70,80]
##op=list(map(lambda x:x*x,l))
##print(op)

'''6. Write a Python program to convert all the characters in uppercase
and lowercase and eliminate duplicate letters from a given sequence. Use map() function'''

##def change_cases(s):
##    return str(s).upper(),str(s).lower()
##s=["a","g","a","B","c","H"]
##op=list(map(change_cases,s))
##print(set(op))

'''7. Write a Python program to add two given lists and find the difference between lists. Use map() function'''

##def add(l1,l2):
##    return l1+l2,l1-l2
##l1=[10,20,30,40]
##l2=[5,10,15,20]
##op=(map(add,l1,l2))
##print(list(op))


'''8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.'''

##l=[1,2,3,4,5]
##t=(1,2,3,4,5)
##
##r1=list(map(str,l))
##r2=tuple(map(str,t))
##print(r1)
##print(r2)










































