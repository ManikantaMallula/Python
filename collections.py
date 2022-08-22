''' The collections which we will study in python collections module are:

OrderedDict
defaultdict
counter
namedtuple
deque '''


'''1. OrderedDict
With an OrderedDict, the order of insertion is maintained when key and values are inserted into the dictionary.
If we try to insert a key again, this will overwrite the previous value for that key. '''

##from collections import *
##r=OrderedDict([(1,"alex"),(2,"john")])
##for k,v in r.items():
##    print(k,v)

''' 2. Default Dict
The default dictionary can contain duplicate keys. The advantage of using the default dictionary is
that we can collect items which belong to the same key. Let’s look at a code snippet which demonstrates the same: '''

##from collections import *
##
##marks=[("a",1),("b",2),("c",3),("a",5),("c",4)]
##d=defaultdict(list)
##for k,v in marks:
##    d[k].append(v)
##print(list(d.items()))

'''3. Counter
The Counter collections allow us to keep a count of all the items which are inserted '''

##from collections import *
##
##d=[("a",1),("b",2),("c",3),("a",4),("a",5)]
##
##c=Counter(name for name,marks in d)
##print(c)


''' 4. Named Tuple
As we already know, Python Tuples are immutable lists. This means that a value cannot be given
to a key which aready exists in the tuple. '''



##import collections
##
##User = collections.namedtuple('User', 'name age gender')
##a = User(name='Shubham', age=23, gender='M')
##print(a)
##
##print('Name of User: {0}'.format(a.name))
##print(a.age)



##from collections import *
##t=namedtuple("user","name age gender")
##a=t(name="alex",age=25,gender="M")
##print(t)
##print(a.name)
##print(a.age)
##print(a.gender)

'''5. Deque
A Deque is a double-ended queue which allows us to add and remove elements from both the ends.
This enhances the capabilities of a stack or a queue. '''



##import collections
##
##name = collections.deque('Shubham')
##print('Deque       :', name)
##
##name.extendleft('...')
##name.append('-')
##print('Deque       :', name)













