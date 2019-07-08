# Recursion

# fibonacci
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(1,11):
    print(i, fib(i))

# factorial
def fac(n):
    if n < 0:
        return None
    if n < 2:
        return 1
        
    return n * fac(n - 1)

for i in range(1,11):
    print(i, fac(i))