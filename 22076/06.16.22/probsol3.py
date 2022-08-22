'''program:
write a program to merge characters of two strings into single string by taking characters alternatively.
Input:
Take any two strings(note:The string contains alpha numeric characters also)
ex:
s1=""
s2=""

Output:
The output should be a single string such a way that input strings characters are printed alternatively.

Explanation:
For example,if the given string1 is "gopi" and string2 is "venkat".

The output should be "gvoepmikat"

Example1:

Sample Input:
priya12
45rohit
Sample Output:
p4r5iryoah1i2t '''

s1=input("enter 1st string: ")
s2=input("enter 2nd string: ")
i=0
j=0
op=""
while i<len(s1) or j<len(s2):
    if i<len(s1):
        op=op+s1[i]
        i=i+1
    if j<len(s2):
        op=op+s2[j]
        j=j+1
print(op)
    
