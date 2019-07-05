'''
The break and continue statements
So far, we've treated the body of the loop as an indivisible and inseparable sequence of instructions that are performed completely at every turn of the loop. However, as developer, you could be faced with the following choices:

it appears that it's unnecessary to continue the loop as a whole; you should refrain from further execution of the loop's body and go further;
it appears that you need to start the next turn of the loop without completing the execution of the current turn.
Python provides two special instructions for the implementation of both these tasks. Let's say for the sake of accuracy that their existence in the language is not necessary - an experienced programmer is able to code any algorithm without these instructions. Such additions, which don't improve the language's expressive power, but only simplify the developer's work, are sometimes called syntactic candy, or syntactic sugar.

These two instructions are:

break - exits the loop immediately, and unconditionally ends the loop's operation; the program begins to execute the nearest instruction after the loop's body;
continue - behaves as if the program has suddenly reached the end of the body; the next turn is started and the condition expression is tested immediately.
'''

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")