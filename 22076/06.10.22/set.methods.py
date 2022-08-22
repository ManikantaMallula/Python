# Set Methods

'''1.add()
Adds an element to the set '''

##s={"happy","new"}
##s.add("year")
##print(s)

'''2.clear()
Removes all the elements from the set '''

##s={"happy","new"}
##s.clear()
##print(s)

'''copy()
Returns a copy of the set '''

##s={"happy","new",1,3}
##s1=s.copy()
##print(s1)



'''difference()
Returns a set containing the difference between two or more sets
The difference() method returns a set that contains the difference between two sets.

Meaning: The returned set contains items that exist only in the first set, and not in both sets.'''

##s={"happy","new",1,3}
##s1={1,3,5}
##print(s1.difference(s))
##print(s.difference(s1))



'''difference_update()
Removes the items in this set that are also included in another, specified set'''

##s={"happy","new",1,3}
##s1={1,3,5}
##print(s1.difference_update(s))
##print(s.difference_update(s1))


'''discard()
Remove the specified item'''

##s={"happy","new",1,3}
##s.discard(1)
##print(s)



'''intersection()
Returns a set, that is the intersection of two other sets'''

##s1={1,2,3,4,5,6}
##s2={1,2,7,8,9}
##print(s2.intersection(s1))


'''intersection_update()
Removes the items in this set that are not present in other, specified set(s)'''

##s1={1,2,3,4,5,6}
##s2={1,2,7,8,9}
##s1.intersection_update(s2)
##print(s1)


'''isdisjoint()
Returns whether two sets have a intersection or not'''

##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "facebook"}
##z = x.isdisjoint(y)
##print(z)


'''issubset()
Returns whether another set contains this set or not'''

##s1={1,2,3,4,5,6}
##s2={1,2,6}
##print(s2.issubset(s1))
##print(s1.issubset(s2))


'''issuperset()
Returns whether this set contains another set or not'''

##s1={1,2,3,4,5,6}
##s2={1,2,6}
##print(s2.issuperset(s1))
##print(s1.issuperset(s2))


'''pop()
Removes an element from the set'''

##s1={1,2,3,4,5,6}
##s1.pop()
##print(s1)


'''remove()
Removes the specified element
This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.'''

##s1={1,2,3,4,5,6}
##s1.remove(5)
##print(s1)

'''symmetric_difference()
Returns a set with the symmetric differences of two sets
The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.

Meaning: The returned set contains a mix of items that are not present in both sets.'''

##s1={1,2,3,4,5,6}
##s2={1,2,6}
##print(s1.symmetric_difference(s2))

'''symmetric_difference_update()
inserts the symmetric differences from this set and another

The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.'''

##s1={1,2,3,4,5,8}
##s2={1,2,6,7}
##a=s1.symmetric_difference_update(s2)
###b=s2.symmetric_difference_update(s1)
##print(a)
###print(b)
##print(s1)
##print(s2)

'''union()
Return a set containing the union of sets
The union() method returns a set that contains all items from the original set, and all items from the specified set(s).

You can specify as many sets you want, separated by commas.

It does not have to be a set, it can be any iterable object.

If an item is present in more than one set, the result will contain only one appearance of this item.'''


##x = {"a", "b", "c"}
##y = {"f", "d", "a"}
##z = {"c", "d", "e"}
##result = x.union(y, z)
##print(result)


'''update()
Update the set with the union of this set and others
The update() method updates the current set, by adding items from another set (or any other iterable).

If an item is present in both sets, only one appearance of this item will be present in the updated set.

'''

##x = {"a", "b", "c"}
##y = {"f", "d", "a"}
##x.update(y)
##print(x)






