# Sequece types and mutability 
'''
A sequence type is a type of data in Python which is able to store more than one value (or less than one, as a sequence may be empty), 
and these values can be sequentially (hence the name) browsed, element by element.
The list is a classic example of a Python sequence, although there are some other sequences worth mentioning

The second notion - mutability - is a property of any of Python's data that describes its readiness to be freely changed during program execution. 
There are two kinds of Python data: mutable and immutable.

Mutable data can be freely updated at any time - we call such an operation in situ.
In situ is a Latin phrase that translates as literally in position. For example, the following instruction modifies the data in situ:

list.append(1)


Immutable data cannot be modified in this way.

Imagine that a list can only be assigned and read over. You would be able neither to append an element to it, nor remove any element from it. 
This means that appending an element to the end of the list would require the recreation of the list from scratch.

You would have to build a completely new list, consisting of the all elements of the already existing list, plus the new element.

The data type we want to tell you about now is a tuple. A tuple is an immutable sequence type. It can behave like a list, 
but it mustn't be modified in situ.
'''

'''
What is a tuple?
The first and the clearest distinction between lists and tuples is the syntax used to create them - tuples prefer to use parenthesis, 
whereas lists like to see brackets, although it's also possible to create a tuple just from a set of values separated by commas.
'''

tuple1 = (1, 2, 4, 8)
tuple2 = 1., .5, .25, .125

print(tuple1)
print(tuple2)

# Note: each tuple element may be of a different type (floating-point, integer, or any other not-as-yet-introduced kind of data).


# If you want to create a one-element tuple, you have to take into consideration the fact that, due to syntax reasons (a tuple has to be distinguishable from an ordinary, single value), you must end the value with a comma:

oneElementTuple1 = (1, )
oneElementTuple2 = 1., 

'''
How to use a tuple: continued
What else can tuples do for you?

the len() function accepts tuples, and returns the number of elements contained inside;
the + operator can join tuples together (we've shown you this already)
the * operator can multiply tuples, just like lists;
the in and not in operators work in the same way as in lists.
'''


'''
1. Tuples are ordered and unchangeable (immutable) collections of data. They can be thought of as immutable lists. They are written in round brackets:
'''

myTuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(myTuple)

myList = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(myList)

# Each tuple element may be of a different type (i.e., integers, strings, booleans, etc.). What is more, tuples can contain other tuples or lists (and the other way round).

'''
2. You can create an empty tuple like this:
'''

emptyTuple = ()
print(type(emptyTuple))    # outputs: <class 'tuple'>

'''
3. A one-element tuple may be created as follows:
'''

oneElemTup1 = ("one", )    # brackets and a comma
oneElemTup2 = "one",     # no brackets, just a comma

# If you remove the comma, you will tell Python to create a variable, not a tuple:

myTup1 = 1, 
print(type(myTup1))    # outputs: <class 'tuple'>

myTup2 = 1
print(type(myTup2))    # outputs: <class 'int'>

'''
4. You can access tuple elements by indexing them:
'''

myTuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(myTuple[3])    # outputs: [3, 4]

'''
5. Tuples are immutable, which means you cannot change their elements (you cannot append tuples, or modify, or remove tuple elements). The following snippet will cause an exception:
'''

myTuple = (1, 2.0, "string", [3, 4], (5, ), True)
myTuple[2] = "guitar"    # a TypeError exception will be raised

# However, you can delete a tuple as a whole:

myTuple = 1, 2, 3, 
del myTuple
print(myTuple)    # NameError: name 'myTuple' is not defined


'''
6. You can loop through a tuple elements (Example 1), check if a specific element is (not)present in a tuple (Example 2), use the len() function to check how many elements there are in a tuple (Example 3), or even join/multiply tuples (Example 4):
'''

# Example 1
t1 = (1, 2, 3)
for elem in t1:
    print(elem)

# Example 2
t2 = (1, 2, 3, 4)
print(5 in t2)
print(5 not in t2)

# Example 3
t3 = (1, 2, 3, 5)
print(len(t3))

# Example 4
t4 = t1 + t2
t5 = t3 * 2

print(t4)
print(t5)

'''
You can also create a tuple using a Python built-in function called tuple(). This is particularly useful when you want to convert a certain iterable (e.g., a list, range, string, etc.) to a tuple:
'''

myTup = tuple((1, 2, "string"))
print(myTup)

lst = [2, 4, 6]
print(lst)    # outputs: [2, 4, 6]
print(type(lst))    # outputs: <class 'list'>
tup = tuple(lst)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>

# By the same fashion, when you want to convert an iterable to a list, you can use a Python built-in function called list():

tup = 1, 2, 3, 
lst = list(tup)
print(type(lst))    # outputs: <class 'list'>

'''