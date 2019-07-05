'''
The same kind of operation is performed by the computer, but with one difference: as two is the base for binary numbers (not 10), shifting a value one bit to the left thus corresponds to multiplying it by two; respectively, shifting one bit to the right is like dividing by two (notice that the rightmost bit is lost).

The shift operators in Python are a pair of digraphs: << and >>, clearly suggesting in which direction the shift will act.

value << bits
value >> bits

The left argument of these operators is an integer value whose bits are shifted. The right argument determines the size of the shift.

It shows that this operation is certainly not commutative.

The priority of these operators is very high. You'll see them in the updated table of priorities, which we'll show you at the end of this section.

Take a look at the shifts in the editor window.

The final print() invocation produces the following output:

17 68 8

Note:

17 // 2 → 8 (shifting to the right by one bit is the same as integer division by two)
17 * 4 → 68 (shifting to the left by two bits is the same as integer multiplication by four)

And here is the updated priority table, containing all the operators introduced so far:

Priority	                       Operator	
1	~, +, -	                        unary
2	**	
3	*, /, //, %	
4	+, -	                        binary
5	<<, >>	
6	<, <=, >, >=	
7	==, !=	
8	&	
9	|	
10	=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=
'''

var = 17
varRight = var >> 1
varLeft = var << 2
print(var, varLeft, varRight)