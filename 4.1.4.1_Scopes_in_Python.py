'''
The scope of a name (e.g., a variable name) is the part of a code where the name is properly recognizable.

For example, the scope of a function's parameter is the function itself. The parameter is inaccessible outside the function.
'''

def scopeTest():
    x = 123

scopeTest()
print(x)

'''
Let's start by checking whether or not a variable created outside any function is visible inside the functions. 
In other words, does a variable's name propagate into a function's body?
'''

def myFunction():
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)

# The answer is: a variable existing outside a function has a scope inside the functions' bodies.

# A variable existing outside a function has a scope inside the functions' bodies, excluding those of them which define a variable of the same name.
# It also means that the scope of a variable existing outside a function is supported only when getting its value (reading). Assigning a value forces the creation of the function's own variable.

'''
Using this keyword inside a function with the name (or names separated with commas) of a variable(s), 
forces Python to refrain from creating a new variable inside the function - the one accessible from outside will be used instead.
'''
def myFunction():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)

'''
he code in the editor should teach you something. As you can see, the function changes the value of its parameter. Does the change affect the argument?
'''

def myFunction(n):
    print("I got", n)
    n += 1
    print("I have", n)

var = 1
myFunction(var)
print(var)

# The conclusion is obvious - changing the parameter's value doesn't propagate outside the function (in any case, not when the variable is a scalar)
# This also means that a function receives the argument's value, not the argument itself. This is true for scalars.

def myFunction(myList1):
    print(myList1)
    myList1 = [0, 1]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)

# It seems that the former rule still works.

## Finally, can you see the difference in the example below:

def myFunction(myList1):
    print(myList1)
    del myList1[0]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)

# We don't change the value of the parameter myList1 (we already know it will not affect the argument), but instead modify the list identified by it.