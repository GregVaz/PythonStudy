'''
Anything that can go wrong, will go wrong.

This is Murphy's law, and it works everywhere and always. Your code's execution can go wrong, too. If it can, it will.

Look the code in the editor. There are at least two possible ways it can "go wrong". Can you see them?

    As a user is able to enter a completely arbitrary string of characters, there is no guarantee that the string can be converted into a float value - this is the first vulnerability of the code;
    the second is that the sqrt() function fails if it gets a negative argument.
'''

import math

x = float(input("Enter x: "))
y = math.sqrt(x)

print("The square root of", x, "equals to", y)


'''
You may get one of the following error messages.

Something like this:
Enter x: Abracadabra

Traceback (most recent call last):

  File "sqrt.py", line 3, in 

    x = float(input("Enter x: "))

ValueError: could not convert string to float: 'Abracadabra'

Or something like this:
Enter x: -1

Traceback (most recent call last):

  File "sqrt.py", line 4, in 

    y = math.sqrt(x)

ValueError: math domain error

Can you protect yourself from such surprises? Of course you can. Moreover, you have to do it in order to be considered a good programmer.

'''

# Exceptions

'''
Each time your code tries to do something wrong/foolish/irresponsible/crazy/unenforceable, Python does two things:

    it stops your program;
    it creates a special kind of data, called an exception.

Both of these activities are called raising an exception. We can say that Python always raises an exception (or that an exception has been raised) when it has no idea what do to with your code.

What happens next?

    the raised exception expects somebody or something to notice it and take care of it;
    if nothing happens to take care of the raised exception, the program will be forcibly terminated, and you will see an error message sent to the console by Python;
    otherwise, if the exception is taken care of and handled properly, the suspended program can be resumed and its execution can continue.
'''

# How do you handle exceptions? The word try is key to the solution.

'''
    the try keyword begins a block of the code which may or may not be performing correctly;
    next, Python tries to perform the risky action; if it fails, an exception is raised and Python starts to look for a solution;
    the except keyword starts a piece of code which will be executed if anything inside the try block goes wrong - if an exception is raised inside a previous try block, it will fail here, so the code located after the except keyword should provide an adequate reaction to the raised exception;
    returning to the previous nesting level ends the try-except section.
'''

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")

'''

    the except branches are searched in the same order in which they appear in the code;
    you must not use more than one except branch with a certain exception name;
    the number of different except branches is arbitrary - the only condition is that if you use try, you must put at least one except (named or not) after it;
    the except keyword must not be used without a preceding try;
    if any of the except branches is executed, no other branches will be visited;
    if none of the specified except branches matches the raised exception, the exception remains unhandled (we'll discuss it soon)
    if an unnamed except branch exists (one without an exception name), it has to be specified as the last.

'''

