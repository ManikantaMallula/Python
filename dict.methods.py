'''clear()	Removes all the elements from the dictionary
The clear() method removes all the elements from a dictionary.
dictionary.clear() '''

##d={"a":1,"b":2}
##d.clear()
##print(d)

'''copy()	Returns a copy of the dictionary
dictionary.copy()'''

##d1={"a":1,"b":2}
##d2=d1.copy()
##print(d2)

'''fromkeys()	Returns a dictionary with the specified keys and value
The fromkeys() method returns a dictionary with the specified keys and the specified value.
dict.fromkeys(keys, value)'''

####x = ('key1', 'key2', 'key3')
####y = (1,2,3)
####thisdict = dict.fromkeys(x, y)
####print(thisdict)

'''get()	Returns the value of the specified key'''

##d1={'Apple': 25.67, 'Kiwi': 30,'Orange':40}
##print(d1)
##v1=d1.get('Kiwi')
##print(v1)

'''items()	Returns a list containing a tuple for each key value pair'''

##d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}
##
##d2=d1.items()
##print(d2)
##for d2 in d1.items():
##    print(d2)

'''keys()	Returns a list containing the dictionary's keys'''

##d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}
##print(d1)
##d1.keys()
##s=d1.keys()
##print(s)

'''pop()	Removes the element with the specified key'''

##d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}
##print(d1)
##print(d1.pop("Kiwi"))
##print(d1)


'''popitem()	Removes the last inserted key-value pair'''

##d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}
##print(d1)
##d1.popitem()
##print(d1)

'''setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value'''

d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}
d1.setdefault('dragon')
print(d1)

'''update()	Updates the dictionary with the specified key-value pairs'''

##d1={"Praveen":"Python","Kiran":"Java"}
##d2={"RS":"Django","DR":"C"}
##d3=d1.update(d2)
##print(d1)
##print(d2)
##print(d3)

'''values()	Returns a list of all the values in the dictionary'''

##d1={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}
##print(d1)
##d1.values()
##s=d1.values()
##print(s)
##for val in d1.values():
##    print(val)
















