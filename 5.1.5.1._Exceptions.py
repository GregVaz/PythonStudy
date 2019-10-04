# Python 3 defines 63 built-in exceptions, and all of them form a tree-shaped hierarchy, although the tree is a bit weird as its root is located on top.

'''

BaseException
    SystemExit
    KeyboardInterrupt
    ->Exception
        ->ValueError
        ->LookupError
            ->IndexError
            ->KeyError
        ->ArithmeticError
            ->ZeroDivisionError

'''

try:
    y = 1/0
    print(y)
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

'''
Resultado:
    Zero division!
    THE END.
'''

#Will it change anything if we swap the two except branches around? Just like here below:

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")

'''
Result:
    Arithmetic problem!
    THE END.

The exception is the same, but the more general exception is now listed first - it will catch all zero divisions too. 
It also means that there's no chance that any exception hits the ZeroDivisionError branch. 
This branch is now completely unreachable.
'''

# if you want to handle two or more exceptions in the same way, you can use the following sintax:

'''

try:
    :
except (exc1, exc2):
    :

'''


'''

The raise instruction raises the specified exception named exc as if it was raised in a normal (natural) way:
raise exc

Note: raise is a keyword.

The instruction enables you to:

    simulate raising actual exceptions (e.g., to test your handling strategy)
    partially handle an exception and make another part of the code responsible for completing the handling (separation of concerns).

'''

def RaiseExc(n):
    raise ZeroDivisionError

try:
    RaiseExc(0)
except ArithmeticError:
    print("Calling the Exception")

print("The End")

'''
The raise instruction may also be utilized in the following way (note the absence of the exception's name):
raise

There is one serious restriction: this kind of raise instruction may be used inside the except branch only; using it in any other context causes an error.

The instruction will immediately re-raise the same exception as currently handled.
'''

'''

Now is a good moment to show you another Python instruction, named assert. This is a keyword.
assert expression

How does it work?

    It evaluates the expression;
    if the expression evaluates to True, or a non-zero numerical value, or a non-empty string, or any other value different than None, it won't do anything else;
    otherwise, it automatically and immediately raises an exception named AssertionError (in this case, we say that the assertion has failed)

How it can be used?

    you may want to put it into your code where you want to be absolutely safe from evidently wrong data, and where you aren't absolutely sure that the data has been carefully examined before (e.g., inside a function used by someone else)
    raising an AssertionError exception secures your code from producing invalid results, and clearly shows the nature of the failure;
    assertions don't supersede exceptions or validate the data - they are their supplements.

If exceptions and data validation are like careful driving, assertion can play the role of an airbag.

'''

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

# More information https://docs.python.org/3.6/library/exceptions.html
