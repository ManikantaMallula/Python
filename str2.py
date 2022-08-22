s=input("enter some string: ")
l=[]
#print("length of string is:",l)
words=s.split()
words_count={}
for word in words:
    words_count[word]=words.count(word)
for key, values in words_count.items():
    print(key,values)
