'''
Max Contiguous Subarray:
Given a list of integers, write a program to
identify contiguous sub-list that has the largest
sum and print the sub-list. Any non-empty slice
of the list with step size 1 can be considered as
contiguous sub-list.

Input:
The input will contain space-separated integers,
denoting the elements of the list.

Output
The output should be space-separated integers.

Explanation
For example, if the given list is [2, -4, 5, -1, 2,
-3], then all the possible contiguous sub-lists
will be,
[12:31 PM] Mounika Yarramasu
Explanation
For example, if the given list is [2, -4, 5, -1, 2,
-3], then all the possible contiguous sub-lists
will be,
[2]
[2,-4]
[2,-4, 5]
[2,-4, 5, -1]
[2,-4, 5, -1, 2]
[2,-4, 5, -1, 2, -3]
[-4]
[-4, 5]
[-4, 5, -1]
[-4, 5, -1, 2]
[-4, 5, -1, 2, -3]
[5]
[5, -1]
[5, -1, 2]
[5, -1, 2, -3]
[-1]
[-1, 2]
[-1, 2, -3]
[2]
[2, 3]
[-3]

Sample Input 1
2 -4 5 -1 2 -3
Sample Output 1
5 -1 2
Sample Input 2
-2 -3 4 -1 -2 1 5 -3
Sample Output 2
4 -1 -2 1 5 '''


##l1 =[2, -4, 5, -1, 2,-3]
##lists=[]
##aa=[]
##k=[]
##for i in range(len(l1)+1):
##    for j in range(i):
##        lists.append(l1[j:i])
##
##for i in lists:
##    aa.append(i)
##
##
##    add=0
##    for j in i:
##        add+=j
##    k.append(add)
####max_a=max(k)
##
##index_a=k.index(max(k))
##print(aa[index_a])

##l =[2, -4, 5, -1, 2,-3]
##l1=[]
##l2=[]
##l3=[]
##for i in range(len(l)+1):
##    for j in range(i):
##        l1.append(l[j:i])
##for j in l1:
##    l2.append(j)
##    add=0
##    for k in j:
##        add+=k
##    l3.append(add)
##max_l3=max(l3)
##print(max_l3)
##index_l3=l3.index(max(l3))
##print(l1[index_l3])





































