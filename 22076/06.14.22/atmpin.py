

s=input("ENTER PIN NUMBER: ")
if len(s)==6 or len(s)==4:
    if s.isdigit():
        print("valid pin")
    else:
        print("invalid pin")
else:
    print("invalid pin")


    
