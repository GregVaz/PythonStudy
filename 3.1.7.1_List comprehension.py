# A list comprehension is actually a list, but created on-the-fly during program execution, and is not described statically.

# Take a look at the snippet:
WHITE_PAWN = "white_pan"

row = [WHITE_PAWN for i in range(8)]
print(row)

# The part of the code placed inside the brackets specifies:

# the data to be used to fill the list (WHITE_PAWN)
# the clause specifying how many times the data occurs inside the list (for i in range(8))


# Example #1:

squares = [x ** 2 for x in range(10)]

# Example #2:

twos = [2 ** i for i in range(8)]

# Example #3:

odds = [x for x in squares if x % 2 != 0 ]

