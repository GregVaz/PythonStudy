'''
The inner life of lists
Now we want to show you one important, and very surprising, feature of lists, which strongly distinguishes them from ordinary variables.

We want you to memorize it - it may affect your future programs, and cause severe problems if forgotten or overlooked.

Take a look at the snippet in the editor.

The program:

creates a one-element list named list1;
assigns it to a new list named list2;
changes the only element of list1;
prints out list2.
The surprising part is the fact that the program will output: [2], not [1], which seems to be the obvious solution.


Lists (and many other complex Python entities) are stored in different ways than ordinary (scalar) variables.

You could say that:

the name of an ordinary variable is the name of its content;
the name of a list is the name of a memory location where the list is stored.
Read these two lines once more - the difference is essential for understanding what we are going to talk about next.

The assignment: list2 = list1 copies the name of the array, not its contents. In effect, the two names (list1 and list2) identify the same location in the computer memory. Modifying one of them affects the other, and vice versa.

How do you cope with that?
'''

list1 = [1]
list2 = list1
list1[0] = 2
print(list2)

# Result: [2]


'''
Powerful slices
Fortunately, the solution is at your fingertips - its name is the slice.

A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.

It actually copies the list's contents, not the list's name.

This is exactly what you need. Take a look at the snippet below:
'''

list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

# Its output is [1].
# This inconspicuous part of the code described as [:] is able to produce a brand new list.

# Copying the whole list
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

# Copying part of the list
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)

'''
Slices - negative indices
Look at the snippet below:

myList[start:end]

To repeat:

start is the index of the first element included in the slice;
end is the index of the first element not included in the slice.

This is how negative indices work with the slice:
'''

myList = [10, 8, 6, 4, 2]
newList = myList[1:-1]
print(newList)

# The snippet's output is: [8, 6, 4].


# If the start specifies an element lying further than the one described by the end (from the list's beginning point of view), the slice will be empty:

myList = [10, 8, 6, 4, 2]
newList = myList[-1:1]
print(newList)

# The snippet's output is: [].


# As we've said before, omitting both start and end makes a copy of the whole list:

myList = [10, 8, 6, 4, 2]
newList = myList[:]
print(newList)

# The previously described del instruction is able to delete more than just a list's element at once - it can delete slices too:

del myList[1:3]
print(myList)

# Output: [10, 4, 2] 

# Deleting all the elements at once is possible too:

myList = [10, 8, 6, 4, 2]
del myList[:]
print(myList)


'''
Python offers two very powerful operators, able to look through the list in order to check whether a specific value is stored inside the list or not.
These operators are:

elem in myList
elem not in myList

The first of them (in) checks if a given element (its left argument) is currently stored somewhere inside the list (the right argument) - the operator returns True in this case.

The second (not in) checks if a given element (its left argument) is absent in a list - the operator returns True in this case.
'''

myList = [0, 3, 12, 8, 2]

print(5 in myList) # Output: False
print(5 not in myList) # Output: True
print(12 in myList) # Output: True