##3. Check if a string contains a specific substrin

s=input("enter main string: ")
sub=input("enter sub string to find: ")
if sub in s:
    print("main string {} contains sub string {}".format(s,sub))
else:
    print("main string {} not contains sub string {} ".format(s,sub))