
''' 1. Define a function that accepts roll number and
returns whether the student is present or absent.  '''

##def func(n):
##    rollno=int(input("enter roll num between 1 to 10: "))
##    present=[1,4,6]
##    absent=[2,3,5,7,8,9,10]
##    if rollno in present:
##        print(rollno,"is present")
##    elif rollno in absent:
##        print(rollno,"is absent")
##    return func(n-1)
##func(10)


##def func(l):
##    a=int(input("enter roll num to check: "))
##    if a in l:
##        print("Present")
##    else:
##        print("Absent")
##l=[5,6,7,8]
##func(l)             

'''output:
enter roll num between 1 to 10: 5
5 is absent
enter roll num between 1 to 10: 4
4 is present
enter roll num between 1 to 10: 5
5 is absent '''

    
        
''' 2. a. Write a python program to print multiple arguments.
	b. Write a function that accepts variable length key value pair as
	arguments. '''

###a.
##def func(*n):
##    for i in n:
##        print(i)
##        
##func("a","b","c","d")

##def func(**n):
##    return n
##print(func(ojas=1,google=2))


      

'''output:
a
b
c
d '''





''' 3. 	 a. Write a python program to find the power of a number using recursion
b. Write a Python program of recursion list sum 
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21 '''


#a.
##def pow(a,b):
##    if b==0:
##        return 1
##    else:
##        x=a*pow(a,b-1)
##    return x
##a=int(input("enter a num to find power: "))
##b=int(input("enter power num: "))
##print(pow(a,b))

''' output:
enter a num to find power: 2
enter power num: 3
8 '''


###b.
##def func(l):
##    op=0
##    for i in l:
##        if type(i)==type([]):
##            op+=func(i)
##        else:
##            op+=i
##    return op
##print(func([1, 2, [3,4], [5,6]]))

''' output: 21 '''

        
'''4. Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will
calculate the addition of a and b
At last, an outer function will add 5 into addition and return it '''


##def outer(a,b):
##    sum=0
##    def inner():
##        sum=a+b
##        return sum
##    return inner()+5
##a=int(input("enter a value: "))
##b=int(input("enter b value: "))
##print(outer(a,b))

''' output:
enter a value: 20
enter b value: 25
50 '''


''' 5. 	a.  Assign a different name to function and call it through the new name
b. 15.Create a function showEmployee() in such a way that it should accept employee name,
and it’s salary and display both, and if the salary is missing in function call it should show
it as 9000 '''


#a.
##def wish():
##    print("good morning to all")
##greeting=wish
##greeting()

''' output: good morning to all'''

###b.
##def showEmployee(name,salary=9000):
##    print("name of the employee {} and his salary is {}".format(name,salary))
##showEmployee("alex",10000)
##showEmployee("John")

'''output:
    name of the employee alex and his salary is 10000
name of the employee John and his salary is 9000 '''


''' 
6.	 a. Write a Python function that takes a number as a parameter and check the number is prime or not. 
b. Write a Python function that checks whether a passed number is palindrome or not.  '''


##def prime(n):
##    count=0
##    for i in range(1,n+1):
##        if n%i==0:
##            count+=1
##    if count==2:
##        return True
##    else:
##        return False
##n=int(input("enter a number to check prim or not: "))
##print(prime(n))

##def func(n):
##    
##    temp=n
##    while n>0:
##        d=n%10
##        op=str(d)
##        n=n//10
##    if int(op)==temp:
##        return true
##    else:
##        return False
##print(func(121))


##def func(n):
##    temp=n
##    op=""
##    while n>0:
##        r=n%10
##        op+=str(r)
##        n=n//10
##    print(op)
##    print(temp)
##    if int(op)==temp:
##        return True
##    else:
##        return False
##n=int(input("enter a number to check : "))        
##print(func(n))

'''
output:
    enter a number to check : 121
121
121
True
'''


''' output:
enter a number to check prim or not: 7
True '''

    
''' 7. 	a. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

b. 	Write a Python program to create Fibonacci series upto n using Lambda

c.  Write a Python program to add two given lists using map and lambda.

d. Write a Python program to find palindromes in a given list of strings using
Lambda.  
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']

e. Using .sort() method, create a lambda function that sorts the list in descending order.
Refrain from using the reverse parameter.
(Hint: lambda will be passed to sort method's key parameter as argument)

f. Write a lambda function which takes z as a parameter and returns z*11 '''

#a
##marks= [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##print("Original list of tuples:")
##print(marks)
##print()
##marks.sort(key = lambda x: x[1])
##print("List of Tuples:")
##print(marks)

#b.
##from functools import reduce
##a=lambda n:reduce(lambda m,p:m+[m[-1]+m[-2]],range(n-2),[0,1])
##print(a(5))
''' output:
[0, 1, 1, 2, 3] '''


###c
##a=[1,2,4]
##b=[4,5,6]
##c=list(map(lambda x,y:x+y ,a,b))
##print(c)

''' output:
    [5, 7, 10] '''

###d.
##l=['php', 'w3w', 'Python', 'abcd', 'Java', 'aaa']
##s=list(filter(lambda x:x==x[::-1],l))
##print(s)



##s=list(filter(lambda x:(x=="".join(reversed(x) for x in l))))
##print(s)


###e.
##l=[5,6,12,3,4]
##l.sort(key=lambda x:-x)
##print(l)






###f.
##x=lambda z:z*11
##z=int(input("enter some valuea: "))
##print(x(z))

''' output:
enter some valuea: 10
110'''




''' output:
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)] '''

''' 8. 	a. Using List Comprehension Find all of the numbers from 1–1000
that are divisible by 8
b. Use list comprehension to contruct a new list but add 6 to each item. '''

###a.

##s=[x for x in range(1,1000) if x%8==0]
##print(s)


''' output:
    [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200,
     208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384,
     392, 400, 408, 416, 424, 432, 440, 448, 456, 464, 472, 480, 488, 496, 504, 512, 520, 528, 536, 544, 552, 560, 568, 576, 584, 592, 600, 608, 616, 624, 632, 640, 648, 656, 664, 672, 680, 688, 696, 704, 712, 720, 728, 736, 744,
     752, 760, 768, 776, 784, 792, 800, 808, 816, 824, 832, 840, 848, 856, 864, 872, 880, 888, 896, 904, 912, 920, 928, 936, 944, 952,
     960, 968, 976, 984, 992] '''

###b.
##l=[1,2,3,4]
##newlist=[x+6 for x in l]
##print(newlist)

''' output:
    [7, 8, 9, 10] '''




''' 10. First, create a range from 100 to 160 with steps of 10.
Second, using dict comprehension, create a dictionary where each number
in the range is the key and each item divided by 100 is the value. '''

##a=range(100,160,10)
##print(a)
##d={x:x%100 for x in a}
##print(d)

'''
output:
    {100: 100} '''


''' 9. string = "Practice Problems to Drill List Comprehension in Your Head."

Remove all of the vowels in a string (use string above)

Find all of the words in a string that are less than 5 letters (use string above)

Use a dictionary comprehension to count the length of each word in a sentence (use string above) '''





###a. using comprehension

##s="Practice Problems to Drill List Comprehension in Your Head."
##v=["a","e","i","o","u","A","E","I","O","U"]
##r=[x for x in s if x not in v]
##print(r)
##.................................


##s="Practice Problems to Drill List Comprehension in Your Head."
##v=["a","e","i","o","u","A","E","I","O","U"]
##r=[x for x in s if x not in v]
##op=""
##for i in s:
##    if i not in v:
##        op+=i
##print("after Removing all of the vowels in a string: ")     
##print(op)
##
##print("the words in a string that are less than 5 letters are : ")      
##l=s.split()
##for i in l:
##    if len(i)<5:
##        print(i)
##
##d={x:len(x) for x in l}
##print(d)

''' output:
after Removing all of the vowels in a string: 
Prctc Prblms t Drll Lst Cmprhnsn n Yr Hd.
the words in a string that are less than 5 letters are : 
to
List
in
Your
{'Practice': 8, 'Problems': 8, 'to': 2, 'Drill': 5, 'List': 4, 'Comprehension': 13, 'in': 2, 'Your': 4, 'Head.': 5} '''




''' 11. Using dict comprehension and a conditional argument create a
dictionary from the current dictionary
where only the key:value pairs with value above 2000 are take
n to the new dictionary. dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800,
                                "XPO":1700} '''

d1={"NFLX":4950,"TREX":2400,"FIZZ":1800,"XPO":1700}

d2={i:d1[i] for i in d1 if d1[i]>2000}
print(d2)


''' 12. Write a Python Set comprehension with an if clause example '''

##set1={1,2,3,4,5,6,8}
##s={x for x in set1 if x%2==0}
##print(s)










