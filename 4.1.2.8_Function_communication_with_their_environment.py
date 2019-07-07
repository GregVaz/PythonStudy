# You can pass information to functions by using parameters. Your functions can have as many parameters as you need.

def hi(name):
    print("Hi,", name)

hi("Greg")

# three-parameter function: 

def address(street, city, postalCode):
    print("Your address is:", street, "St.,", city, postalCode)

s = input("Street: ")
pC = input("Postal Code: ")
c = input("City: ")

address(s, c, pC)

# You can pass arguments to a function using the following techniques:

# positional argument passing in which the order of arguments passed matters,
# keyword (named) argument passing in which the order of arguments passed doesn't matter,
# a mix of positional and keyword argument passing.

def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


def subtra1(a, b):
    print(a - b)

subtra1(a=5, b=2)    # outputs: 3
subtra1(b=2, a=5)    # outputs: 3

def subtra2(a, b):
    print(a - b)

subtra2(5, b=2)    # outputs: 3
subtra2(5, 2)    # outputs: 3

