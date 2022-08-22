s=input("enter some string: ")
l=[]
l=s.split()
for x in s:
  if x not in l:
    l.append(x)
for x in reversed(sorted(l)):
  print("{} occurred {} times".format(x,s.count(x)))