'''
Logical values vs. single bits
Logical operators take their arguments as a whole regardless of how many bits they contain. The operators are aware only of the value: zero (when all the bits are reset) means False; not zero (when at least one bit is set) means True.

The result of their operations is one of these values: False or True. This means that this snippet will assign the value True to the j variable if i is not zero; otherwise, it will be False.

i = 1
j = not not i
'''
'''
Bitwise operators
However, there are four operators that allow you to manipulate single bits of data. They are called bitwise operators.

They cover all the operations we mentioned before in the logical context, and one additional operator. This is the xor (as in exclusive or) operator, and is denoted as ^ (caret).

Here are all of them:

& (ampersand) - bitwise conjunction;
| (bar) - bitwise disjunction;
~ (tilde) - bitwise negation;
^ (caret) - bitwise exclusive or (xor).


Bitwise operations (&, |, and ^)
Arg A	Arg B	Arg B & Arg B	Arg A | Arg B	Arg A ^ Arg B
0	    0	        0	                0	            0
0	    1	        0	                1	            1
1	    0	        0	                1	            1
1	    1	        1	                1	            0

Bitwise operations (~)
Arg	    ~Arg
0	      1
1	      0

Let's make it easier:

& requires exactly two 1s to provide 1 as the result;
| requires at least one 1 to provide 1 as the result;
^ requires exactly one 1 to provide 1 as the result.


Let us add an important remark: the arguments of these operators must be integers; we must not use floats here.

The difference in the operation of the logical and bit operators is important: the logical operators do not 
penetrate into the bit level of its argument. They're only interested in the final integer value.

Bitwise operators are stricter: they deal with every bit separately. If we assume that the integer variable 
occupies 64 bits (which is common in modern computer systems), you can imagine the bitwise operation as a 64-fold 
evaluation of the logical operator for each pair of bits of the arguments. This analogy is obviously imperfect, 
as in the real world all these 64 operations are performed at the same time (simultaneously).
'''


i = 15
j = 22

# If we assume that the integers are stored with 32 bits, the bitwise image of the two variables will be as follows:
# i: 00000000000000000000000000001111
# j: 00000000000000000000000000010110

# The assignment is given:
log = i and j

# We are dealing with a logical conjunction here. Let's trace the course of the calculations. 
# Both variables i and j are not zeros, so will be deemed to represent True. 
# Consulting the truth table for the and operator, we can see that the result will be True. No other operations are performed.

# log: True


# Now the bitwise operation - here it is:
bit = i & j

# The & operator will operate with each pair of corresponding bits separately, 
# producing the values of the relevant bits of the result. Therefore, the result will be as follows:

# i	00000000000000000000000000001111
# j	00000000000000000000000000010110
# bit = i & j	00000000000000000000000000000110

#
# These bits correspond to the integer value of six.
# 
print(bit)

#-----------------------------------------------------------------------------------------------
# The bitwise negation goes like this:

# bitneg = ~i

# It may be a bit surprising: the bitneg variable value is -16. This may seem strange, but isn't at all. If you wish to learn more, you should check out the binary numeral system and the rules governing two's complement numbers.

# i	00000000000000000000000000001111
# bitneg = ~i	11111111111111111111111111110000