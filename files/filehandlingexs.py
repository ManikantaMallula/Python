                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #1.Write a program in python to replace all word “the” by another word “them” in a file “poem.txt”.











##with open("poem.txt","w+") as f:
##    f.write("the")
##    f.seek(0)
##    data=f.readline()
##    print("printing data before replace")
##    print(data)
##with open("poem.txt","w+") as f:
##    f.write("them")
##    f.seek(0)
##    data=f.readline()
##    print("printing data after replace")def read_lastnlines(fname,n):
##	with open('file1.txt') as f:
##		for line in (f.readlines() [-n:]):
##			print(line)
##
##read_lastnlines('file1.txt',3)
##    print(data)


#2.Write a program in python to replace a character by another character in a file “story.txt”. (Accept both the characters from the user)

##with open("story.txt","r+") as f:
##    a=input("enter some character: ")
##    b=input("enter another chatacter to replace: ")
##    d=f.read()
##    d=d.replace(a,b)
##    f.write(d)
##    data=f.read()
##    print(data)

##f = open("story.txt")
##d = f.read()
##a = input("Enter character to be replaced")
##b = input("Enter character that will replaced")
##d = d.replace(a,b)
##f.close()
##f = open("story.txt","w")
##f.write(d)
##f.close()
    


##Write a program in python to replace all the ‘a’ by ‘@’ in a file “data.txt”.

##with open("data1.txt","r+") as f:
##    data=f.read()
##    print("printing data before replace: ",data)
##    data=data.replace("a","@")
##    print("printing data after replace: ",data)


##
##Write a program in python to read file “data.txt” and display only those lines whose length is more than 40 characters.
'''
f = open("data.txt","r")
d = f.readlines()
for i in d:
    if len(i) > 40:
        print(i)'''

##
##Write a program in python to remove all duplicate lines from the file “story.txt”.

'''
f = open("story1.txt", "r")
d = f.readlines()
m = [ ]
for i in d:
     if i not in m:
        m.append(i)
print(m)
f.close()
f = open("story1.txt", "w")
for i in m:
     f.write(i)   
f.close()'''




##
##Write a program in python to display only unique words from the file “story.txt”.

'''f = open("story.txt", "r")
d = f.read()
d = d.split()
str = " "
m = []
for i in d:
  if i not in str:
       str=str+i
       print(i, end=" ")
f.close()'''

##
##Write a program in python to count the frequency of each vowels in a file “task.txt”.


'''f = open("task.txt", "r")
d = f.read()
va=ve=vo=vu=vi=0
for i in d:
     if i=='a' or i=='A':
         va=va+1
     if i=='e' or i=='E':
         ve=ve+1
     if i=='i' or i=='I':
         vi=vi+1
     if i=='o' or i=='O':
         vo=vo+1
     if i=='u' or i=='U':
         vu=vu+1
print("Frequency of vowel \"a\" is", va)
print("Frequency of vowel \"e\" is", ve)
print("Frequency of vowel \"i\" is", vi)
print("Frequency of vowel \"o\" is", vo)
print("Frequency of vowel \"u\" is", vu)'''


##
##Write a program in python to count those words whose length is more than 7 characters in a file “story.txt”.
'''f=open("story.txt", "r")
d=f.read()
d=d.split()
c=0
for i in d:
  if len(i)>7:
    c=c+1
print("Total words are :", c)'''
##
##Write a program in python to count those lines from the file “div.txt” which are starting from ‘T’ or ‘M’.

'''f=open("div.txt", "r")
d=f.readlines()
c=0
for i in d:
     if i[0] == 'M' or i[0] == 'T':
        c=c+1
print("Total lines are :", c)'''

##
##Write a program in python to count those lines from the file “div.txt” which are not starting from ‘M’.

'''f=open("div.txt", "r")
d=f.readlines()
c=0
for i in d:
     if i[0] != 'M':
        c=c+1
print("Total lines are :", c)'''



##
##Write a program in python to display those words from a file “image.txt” which are ending from alphabet ‘m’.

'''f=open("image.txt",'r')
d=f.read()
d=d.split()
c=0
for i in d:
    if i[-1]=='m':
        c=c+1
print("Total words are :", c)'''


##
##Write a program in python to read all lines of file “data.txt” using readline() only.


'''f=open("data.txt")
d=f.readlines()
print(d)
f.close()'''



##
##Write a program in Python to copy the entire content from file “data.txt” to “story.txt”
'''
f = open("data.txt", "r")
f1 = open("story.txt","w")
d = f.read()
e = f1.write(d)
f.close()
f1.close()
print(e)

'''




##
##Write a program in Python to copy the alternate lines from file “data.txt” to “story.txt
'''f = open("data.txt", "r")
f1 = open("story.txt","w")
d = f.readlines()
for i in range(len(d)):
    if i%2==0:
        print(i)
f.close()
f1.close()'''

##
##Write a program in Python to read the entire content from file “data.txt” and copy the contents to “story.txt” in upper case.
'''f = open("data.txt", "r")
f1 = open("story.txt","w")
d = f.read().upper()
e = f1.write(d)
f.close()
f1.close()
print(e)'''

##
##Write a program in Python to read the entire content from file “data.txt” and copy only those words to “story.txt” which start from vowels.

'''
f = open("data.txt", "r")
f1 = open("story.txt","w")
d = f.read().lower()
e = d.split()
for i in e:
    if  i[0] in ['a', 'e', 'i', 'o', 'u']:
        f1.write(i)
f.close()
f1.close()
print(e)'''


##
##Write a program in Python to read the entire content from file “data.txt” and copy only those words in separate lines to “story.txt” which are starting from lower case alphabets .
'''f = open("data.txt", "r")
f1 = open("story.txt","w")
d = f.read().lower()
e = f1.write(d)
f.close()
f1.close()
print(e)
'''

##
##Write a program in Python to read file “data.txt” and copy only those lines to “story.txt” which are starting from alphabets “A” or “T”.
'''f = open("data.txt", "r")
f1 = open("story.txt","w")
d=f.read()
e =d.split()
for i in e:
     if i[0] == 'M' or i[0] == 'T':
        f1.write(i)
f.close()
f1.close()
'''
##
##Write a program in Python which display the longest word from file “star.txt”

'''f = open("star.txt", "r")
d = f.read()
L = d.split()
longword = " "
for i in L:
    if  len(i) > len(longword):
      longword = i
print("longest word is ,",longword)
f.close()

'''



##
##Write a program in Python which display the longest line from file “star.txt”
'''f = open("star.txt", "r")
d = f.readlines()
longline = " "
for i in d:
    if  len(i) > len(longline):
      longline = i
print("longest line is : ", longline)
f.close()'''

##
##Write a program in Python to read the file “star.txt” and display the entire content after removing leading and trailing spaces.
'''f = open("star.txt", "r")
d = f.readlines()
for i in d:
    print(i.strip())
f.close()
'''


##
##Write a program in python that read the content from file “sumit.txt” and display all numbers.

'''f = open("sumit.txt", "r")
d = f.read()
for i in d:
    if i.isdigit():
        print(i)
f.close()
'''


##
##Write a program in Python that display the second and second last line from the file “life.txt”
##f = open("life.txt", "r")
##d = f.readlines()
##print("Second line is :",d[1])
##print("Second last line is :",d[-2])
##f.close()


##
##Consider a binary file “data.dat” which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type. Do the following task in a file 
##
##Write a function addrec() to add a record in a file. 
##
##Write a function disp() to display all the records from the file. 

##Write a function specific_disp(room_no) which takes room number as argument and display its details. 
##
##Write a function mod(room_no) which takes room number as argument and modify it’s details. 
##
##Write a function del(room_no) which takes room number as argument and delete it’s record from file “data.dat” 
##
##Write a menu driven program which shows all operations on Binary File 
##
##Add Record 
##
##Display All Record 
##
##Display Specific Record 
##
##Modify Record 
##
##Delete Record 
##
##Use “data.dat” file which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type 
##
##Write a function disp75() in Python to display only those records of students from file “school.dat” who scored more than 75 percent marks. Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage] 
##
##Write a function dispname() in Python which will display only names of all the students from file “school.dat”. Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage] 
##
##Write a function disp12() in Python which will display records of class 12th students from file “school.dat”. Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage] 
##
##Write a function search(name) in Python which will display record of a student from file “school.dat” whose name is passed as an argument. Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage] 
##
##Write a function disp_mob(model no.) in Python which will display the record of a mobile from “mobile.dat” whose model number (integer type) is passed as an argument. Structure of “mobile.dat” is [Mobile id, Mobile brand, Model No., Price] 


''' 1.Write a Python program to read last n lines of a file. '''


##n=int(input("enter how many lines you want: "))
##with open("b11.txt","r") as f:
##    obj=f.readlines()
##    for i in obj[-n::]:
##        print(i,end='')



'''2.Write a Python program to read a file line by line and store it into a list. '''

##with open("b11.txt","r") as f:
##    l=[]
##    obj=f.readlines()
##    for i in obj:
##        l.append(i)
##print(l)

'''3.Write a Python program to read a file line by line store it into a variable. '''

##with open("b11.txt","r") as f:
##    a=f.readlines()
##    print(a)

''' 5. Write a Python program to count the frequency of words in a file '''

##from collections import *
##
##with open("b11.txt","r") as f:
##    op=f.read().split()
##print(Counter(op))
    

''' 6. Write a Python program to read a random line from a file. '''
##from random import *
##with open("b11.txt","r") as f:
##    obj=f.readlines()
##print(choice(obj))

'''7.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt. '''

##def main(n):
##    for i in n:
##        f=open(i+".txt","w")
##        f.close()
##        print(f.name)
##a="abcdefghijklmnopqrstuvwxyz"
##n=[]
##
##for i in a:
##    n.append(i)
##    
##main(n)
        
'''8.Write a Python program to extract characters from various text files and puts them into a list. '''

import glob
char_list = []
files_list = glob.glob("b11.txt")
for file_elem in files_list:
   with open(file_elem, "r") as f:
       char_list.append(f.read())
print(char_list)




















