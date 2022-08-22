import itertools
l1=[]
l2=[]
mylist=[]
combinations=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
game=True

##def board():
##    print(" ","| "," ","| ")
##    print("-","|","-"," |","-")
##    print(" ","| "," ","| ")
##    print("-","|","-"," |","-")
##    print(" ","| "," ","| ")
##board()
while game==True:
    user1=int(input("select any 1 position: "))
    while user1 in mylist:
        user1=int(input("position already taken,select anyother position: "))
    mylist.append(user1)
    l1.append(user1)
    comb=list(itertools.combinations(l1,3))
    if len(l1)>=3:
        for i in combinations:
            perm=list(itertools.permutations(i))
            for k in perm:
                if k in comb:
                    print("user 1 win")
                    game=False
                    
    if game==True:
        user2=int(input(" enter 2 position: "))
        while user2 in mylist:
            user2=int(input("position already taken: "))
        mylist.append(user2)
        l2.append(user2)
        comp=list(itertools.combinations(l2,3))
        if len(l2)>=3:
            for i in combinations:
                perm=list(itertools.permutations(i))
                for k in perm:
                    if k in comp:
                        print("user 2 wins")
                        game=False
    
print("game over")                  
##    
##import string,random
##c= list(string.ascii_letters + string.digits + "!@#$%^&*()")
##print(c)
##def func():
##    n=int(input("enter any number"))
##    random.shuffle(c)
##    l=[]
##    for i in range(n):
##        l.append(random.choice(c))
##    print("".join(l))
##func()



        






























