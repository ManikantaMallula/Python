'''given alist of integers write a program to print the count of all possible unique combinations of numbers
whose sum is equal to k
explanation:for example if given list of integers and k are 
2 4 6 1 3
6
all possible combinations of the given list are
(6,)(2,)(4,)(1,)(  3,)
(2,4)(1,2)(3,4)(4,6)(1,4)(2,3)(2,6)(3,6)(1,6)(1,3)
(3,4,6)(2,3,6)(1,2,6)(1,2,3)(1,4,6)(1,3,4)(2,3,4)(1,3,6)
(2,3,4,6)(1,2,3,4)(1,2,4,6)(1,2,3,6)(1,3,4,6)
out of all the above combinations  the unique combinations with the sum equal to 6 are
6
2 4
2 1 3
so the output should be the count of unique combinations which is 3
for example if the given list of integers and k are
-1 4 5 6 7 8 2 4 5 2 3 8
7
The unique combinations with the sum equal to 7 are
7
-1 8
3 4
2 5
-1 3 5
-1 4 4
-1 2 6
2 2 3
-1 2 2 4
so the output should be the count of unique combinations which is 9
input:  2 4 6 1 3
         6
output:  3
Note: Dont use permutations and combiations method '''


l=[1,2,3,4,5]
l1=[]
l2=[]
sum=0
count=0
for i in l:
    l1.append(i)
    #print(l1)
    for j in l1:
        print(j)
        sum+=j
        l2.append(sum)
        if sum==6:
            count+=1
        else:
            pass
print(count)
        
    





























    
