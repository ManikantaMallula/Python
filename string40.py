'''1. How would you confirm that 2 strings have the same identity? '''

##a=input("enter some string: ")
##b=input("enter some string: ")
##if id(a)==id(b):
##    print("yes")
##else:
##    print("no")
    




'''2. How would you check if each word in a string begins with a capital letter? '''

##s=input("enter some string to find: ")
##if s.istitle():
##    print("yes each word in a string begins with a capital letter")
##else:
##    print("no each word in a string begins with a capital letter")


''' 3. Check if a string contains a specific substrin '''

##s=input("enter main string: ")
##sub=input("enter sub string to find: ")
##if sub in s:
##    print("main string {} contains sub string {}".format(s,sub))
##else:
##    print("main string {} not contains sub string {} ".format(s,sub))
##


''' 4. Find the index of the first occurrence of a substring in a string '''

##s=input("enter some string: ")
##a=s[0]
##b=s.count(a)
##print(b)




''' 5. Count the total number of characters in a string '''

##s=input("enter some string to find : ")
##print("total number of characters in {} is {}".format(s,len(s)))
      
''' 6. Count the number of a specific character in a string '''

##s="enter some string"
##print(s.count("r"))


    
'''7. Capitalize the first character of a string '''

##s=input("enter some string to captalize: ")
##s1=s.capitalize()
##print(s1)

'''8. What is an f-string and how do you use it? '''



'''9. Search a specific part of a string for a substring '''

##s="Happy new year"
##sub="new"
##print(s.index(sub))




''' 10. Interpolate a variable into a string using format() '''

##a="happy"
##b="new"
##print("{} {}".format(a,b))



''' 11. Check if a string contains only numbers '''

##s=input("enter some string to find: ")
##if s.isdigit():
##    print(" given string contains only numbers")
##else:
##    print(" given string contains some other characters")


''' 12. Split a string on a specific character '''

##s=input("Enter some string to split: ")
##l=s.split()
##print(l)

''' 13. Check if a string is composed of all lower case characters '''

##s=input("enter some string: ")
##if s.islower():
##    print("yes")
##else:
##    print("no")
    
''' 14. Check if the first character in a string is lowercase '''

##s=input("enter some string: ")
##if s[0].islower():
##    print("yes")
##else:
##    print("no")




''' 15. Can an integer be added to a string in Python? '''

##s=input("enter some string: ")
##n=int(input("enter an integer number: "))
##print(s+str(n))


''' 16. Reverse the string “hello world” '''

##s="hello world"
##print(s[::-1])

    

''' 17. Join a list of strings into a single string, delimited by hyphens '''

##l=["happy","new","year"]
##s="-"
##op=s.join(l)
##print(op)

    


''' 18. Check if all characters in a string conform to ASCI '''

##s=input("enter some string: ")
##print(s.isascii())


''' 19. Uppercase or lowercase an entire string '''

##s=input("enter some string: ")
##print(s.upper())
##print(s.lower())

''' 20. Uppercase first and last character of a string '''

##s=input("Enter some string: ")
##print(s[0].upper() + s[1:-1] + s[-1].upper())



''' 21. Check if a string is all uppercase '''

##s=input("enter some string: ")
##if s.isupper():
##        print("yes")
##else:
##    print("no")


''' 22. When would you use splitlines()? '''

##s="HAPPY NEW YEAR"
##l=s.split()
##print(l)


''' 23. Give an example of string slicing '''

##s="happy"
##print(s[2])

''' 24. Convert an integer to a string '''

##n=int(input("enter a number: "))
##print(str(n))


''' 25. Check if a string contains only characters of the alphabet '''

##s=input("enter some string: ")
##if s.alpha():
##    print("yes")
##else:
##    print("no")
    

''' 26. Replace all instances of a substring in a string '''

##s="happy new year"
##sub=s.replace("new","sad")
##print(sub)

''' 27. Return the minimum character in a string '''

##s="happy"
##print(min(s))


'''28. Check if all characters in a string are alphanumeric '''

##s=input("enter some string: ")
##print(s.isalpha())

''' 29. Remove whitespace from the left, right or both sides of a string '''

##s="   happy new year  "
##print(s.rstrip())
##print(s.lstrip())
##print(s.strip())

'''30. Check if a string begins with or ends with a specific character? '''

##s="happy"
##print(s[0]=="h")

''' Solve without using builtin methods: '''
##
##1. WAP to print middle charector of the string

##s=input("enter some string: ")
##print(s[len(s)//2])

'''2. WAP to print half reverse of the string 
##
##Input: KNOWLEDGE
##Output: EGDELKNOW '''

##s="KNOWLEDGE"
##print(s[-1:-6:-1]+s[:4])


''' 3. WAP to remove all the vouels from the given string '''

##s=input("enter some string: ")
##v=["a","e","i","o","u","A","E","I","O","U"]
###l=[]
##op=str()
##for i in s:
##    if i not in v:
##        #l.append(i)
##        op=op+i
##print(op)


''' 4. WAP to insert * in front of every vouels in the string. 
##
##Input: BANANA
##Output: B*AN*AN*A  '''

##s="BANANA"
##v=["A","E","I","O","U"]
##op=str()
##for i in s:
##    if i in v:
##        i="*"+i
##    op=op+i
##print(op)

##
''' 5. WAP to count number of words in the string. '''

##s=input("enter some string: ")
##count=1
##for i in s:
##    if i==" ":
##        count+=1
##print(count)

''' 6. WAP to remove extra space from the given string '''

##s=input("enter some string: ")
##for i in s:
##    if i != "":
##        print(i,end="")


''' 7. WAP to insert string in between the given string 
##Input: Ojas technologies 
##Output: Ojas innovative technologies '''

##s1="Ojas technologies"
##s2="innovative"
##
##for i in s1:
##    if i==" ":
##        i=i+s2+" "
##    print(i,end="")

''' 8. WAP to find the ascci value of given char '''

##s=input("enter a character to find ascci value: ")
##print(ord(s))


''' 9. insert ojas in front of every string '''

##s1="happy new year"
##s2="ojas"
##for i in s1:
##    print(i,end=" ")
##    print(s2,end=" ")

'''10. insert ojas in every extra space in the string '''

##s1=" happy new year"
##s2="ojas"
##for i in s1:
##    print(i,end="")
##    if i==" ":
##        print(s2,end=" ")























