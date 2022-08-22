''' 1) take a list of 8 numbers
lst = [1,2,3,4,5,6,7,8]
and add the alternative numbers in list 

after first iteration list should be [4,6,8,10,12,14]
after second iteration [12,16,20,24]
after third iteration [32,40]

when list is having two elements print that list in the output '''

l1=[1,2,3,4,5,6,7,8]
l2=[]
while len(l1)!=2:
    
    for i in range(len(l1)-2):
        k = l1[i] + l1[i+2]
        l2.append(k)
    
    l1 = l2
    l2 = []
    print(l2)
    print(l1)


