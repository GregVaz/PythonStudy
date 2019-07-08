'''
It will return True if the sides can build a triangle, and False otherwise. In this case, isItATriangle is a good name for such a function.

def isItATriangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))

# More compact

def isItATriangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))
'''

# Can we compact it even more?

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))


# we'll try to ensure that a certain triangle is a right-angle triangle.

a = float(input("Enter the first side's length: "))
b = float(input("Enter the second side's length: "))
c = float(input("Enter the third side's length: "))

def isItRightTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(isItRightTriangle(a,b,c))


'''
Evaluating a triangle's field
We can also evaluate a triangle's field. Heron's formula will be handy here:
'''


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def fieldOfTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return None
    return heron(a, b, c)

print(fieldOfTriangle(a,b,c))