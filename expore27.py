'''
1) take a list and output has to be repeated of the second half of the list elements 
input = [1,2,3,4,5,6]
output = [4,5,6,4,5,6] '''

l=[1,2,3,4,5,6]
k=len(l)//2

op=l[k:]
print(op)
for i in op:
    op.append(i)
    
print(op)   





''' 2) Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9) '''
''' 3) Write a Python program that matches a string that has an a followed by zero or more b's '''
''' 4) Write a Python program that matches a word at the beginning of a string '''
''' 5) open a file and enter a lists like each list is having two or more elements in to the file and retrieve their details in the ouput in lists '''
