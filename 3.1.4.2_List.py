# Indexing lists

numbers = [10, 5, 7, 2, 1]
print("List content:", numbers) # printing original list content

numbers[0] = 111
print("New list content: ", numbers) # current list content

numbers[1] = numbers[4] # copying value of the fifth element to the second
print("New list content:", numbers) # printing current list content

# If you want to check the list's current length, you can use a function named len() (its name comes from length).

# The function takes the list's name as an argument, and returns the number of elements currently stored inside the list (in other words - the list's length).
print("\nList length:", len(numbers)) # printing the list's length

'''
Removing elements from a list
Any of the list's elements may be removed at any time - this is done with an instruction named del (delete). Note: it's an instruction, not a function.

You have to point to the element to be removed - it'll vanish from the list, and the list's length will be reduced by one.
'''
del numbers[1]
print(len(numbers))
print(numbers)

'''
Negative indices are legal
It may look strange, but negative indices are legal, and can be very useful.

An element with an index equal to -1 is the last one in the list.
'''

print(numbers[-1])


'''
Swap the list's elements to reverse their order
'''
myList = [10, 1, 8, 3, 5]
length = len(myList)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)