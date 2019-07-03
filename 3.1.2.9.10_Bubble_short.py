'''
We solve this issue in the following way: we introduce another variable; its task is to observe if any swap 
has been done during the pass or not; if there is no swap, then the list is already sorted, and nothing more 
has to be done. We create a variable named swapped, and we assign a value of False to it, to indicate that 
there are no swaps. Otherwise, it will be assigned True.
'''

myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)