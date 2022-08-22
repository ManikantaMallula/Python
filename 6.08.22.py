''' 1.How do you print duplicate characters from a string? '''
##
##s=input("enter some string: ")
##l=len(s)
##for i in range(0,l):
##    count=1
##    for j in range(i+1,l):
##        if (s[i]==s[j] and s[i]!=""):
##            count+=1
##            s=s[:j]+"0"+s[j+1:]
##    
##    if(count>1 and s[i]!="0"):
##        print(s[i])
##
''' 4.How do you check if a string contains only digits? '''
##
##s=input("enter some string: ")
##num="0123456789"
##count=0
##dig=0
##for i in s:
##    count+=1
##    if i in num:
##        dig+=1
##if count==dig:
##    print("given string contains only digits")
##else:
##    print("given string contains some other elements also")
##
##9. remove chracter
##        
##s=input("enter some string: ")
##r=input("enter some character to remove: ")
##
##for i in s:
##    if i!=r:
##        print(i,end="")




''' 7.Check if the string is anagram or not , if not make it anagram. '''

##s1=input("enter 1st string: ")
##s2=input("enter 2nd string: ")
##count=0
##count1=0
##for i in s2:
##    if i in s1:
##        count+=1
##for j in s1:
##    if j in s2:
##        count1+=1
##if count1==len(s1) and count1==len(s2):
##    print("given string is an anagram")
##else:
##    print("given string is not an anagram")
    
        
''' 5.How do you print the first non-repeated character from a string? '''

##a=input("enter some string: ")
##b=""
##c=""
##for i in a:
##    if i not in b:
##        b=b+i
##    else:
##        c=c+i
##for i in b:
##    if i not in c:
##        print(i)
##        break
    

''' Given string str, How do you find the longest palindromic substring in str? '''



s1="happy new malayalam mam rider year"
s2=""
count1=0
count2=0
max=0
s3=""
for i in s1:
    count1+=1
    if i==" ":
        s2=s1[count2:count1-1]
        count2=count1
        if s2==s2[::-1]:
            add=0
            for i in s2:
                add+=1
                if max<add:
                    max=add
                    if max==add:
                        s3=s2[:max]
print(s3)
                
        




























