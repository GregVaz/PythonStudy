'''
The while loop and the else branch
Both loops, while and for, have one interesting (and rarely used) feature.

We'll show you how it works - try to judge for yourself if it's usable and whether you can live without it or not.

In other words, try to convince yourself if the feature is valuable and useful, or is just syntactic sugar.

Take a look at the snippet in the editor. There's something strange at the end - the else keyword.

As you may have suspected, loops may have the else branch too, like ifs.

The loop's else branch is always executed once, regardless of whether the loop has entered its body or not.

Can you guess the output? Run the program to check if you were right.

Modify the snippet a bit so that the loop has no chance to execute its body even once:

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

The while's condition is False at the beginning - can you see it?

Run and test the program, and check whether the else branch has been executed or not.
'''
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)