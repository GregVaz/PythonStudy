# A function is a block of code that performs a specific task when the function is called (invoked). 
# You can use functions to make your code reusable, better organized, and more readable. Functions can have parameters and return values.

# There are at least four basic types of functions in Python:
#   built-in functions which are an integral part of Python (such as the print() function).
#   the ones that come from pre-installed modules
#   user-defined functions which are written by users for users - you can write your own functions and use them freely in your code,
#   the lambda functions

def hello(name):    # defining a function
    print("Hello,", name)    # body of the function


name = input("Enter your name: ")

hello(name)    # calling the function

