#1.
##fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
##newlist = [x for x in fruits if "a" in x]
##print(newlist)

##l1=["a","b","c","d","e","f"]
###It creates the same list as l1
##print([i for i in l1])

##l1=["a","b","c","d","e","f"]
##print([i.upper() for i in l1])

##l1=[1,2,3,4,5,6,7,8,9]
##print([i+1 for i in l1])

##print([i if i%2==0 else "invalid" for i in range(10)])

##l1=["a","b","c","d","e","f"]
##print([i.upper() if i!="a" else i for i in l1])
##print([i if i=="a" else i.upper() for i in l1])

##l1=["a","b"]
##l2=[1,2]
##print([i+str(j) for i in l1 for j in l2])

##s=[x*x for x in range(1,10)]
##print(s)

##s=[2*x for x in range(1,6)]
##print(s)


##l=[1,2,3,4,5,6,7,8,9,7,47,17]
##s=[x for x in l if x%2==0]
##print(s)

##words=["vadeppa","chakali","rakesh"]
##s=[w[0] for w in words]
##print(s)

##
##n1=[1,2,3,4,5,6]
##n2=[3,4]
##s=[x for x in n1 if x not in n2]
##print(s)

##k=[x for x in n1 if x in n2]
##print(k)

##s="the quick brown fox jumps for over the lazy dog".split()
##a=[[w.upper(),len(w)] for w in s]
##print(a)

#Tuple comprehensions


##s=(x*x for x in range(1,10))
##print(type(s))
##for i in s:
##    print(i)



##n1=[1,2,3,4,5,6]
##n2=[3,4]
##s=(x for x in n1 if x not in n2)
##print(s)
##for i in s:
##    print(i)

# prime numbers
##s=[x for x in range(2,10) if all((x%y!=0)  for y in range(2,x))]
##print(s)

##s={x*x for x in range(10)}
##print(s)

##l={1,2,3,4,5,6,7,8,9,10}
##s={2*x for x in l}
##print(s)

##s={x:x*2 for x in range(1,10)}
##print(s)






















