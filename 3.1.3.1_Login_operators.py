'''
Computer logic
Have you noticed that the conditions we've used so far have been very simple, not to say, quite primitive? 
The conditions we use in real life are much more complex. Let's look at this sentence:

If we have some free time, and the weather is good, we will go for a walk.


We've used the conjunction and, which means that going for a walk depends on the simultaneous fulfilment 
of these two conditions. In the language of logic, such a connection of conditions is called a conjunction. 
And now another example:

If you are in the mall or I am in the mall, one of us will buy a gift for Mom.


The appearance of the word or means that the purchase depends on at least one of these conditions. 
In logic, such a compound is called a disjunction.

It's clear that Python must have operators to build conjunctions and disjunctions. Without them, 
the expressive power of the language would be substantially weakened. They're called logical operators.

*********
*  and  *
*********

One logical conjunction operator in Python is the word and. It's a binary operator with a priority 
that is lower than the one expressed by the comparison operators. It allows us to code complex conditions without the use of parentheses like this one:
'''
counter = 1
value  = 10

counter > 0 and value == 100

'''
The result provided by the and operator can be determined on the basis of the truth table.

If we consider the conjunction of A and B, the set of possible values of arguments and corresponding values of the conjunction looks as follows:

Argument A	Argument B	A and B
False	    False	    False
False	    True	    False
True	    False	    False
True	    True	    True
'''

'''
********
*  or  *
********
A disjunction operator is the word or. It's a binary operator with a lower priority than and (just like + compared to *). Its truth table is as follows:
'''

counter > 0 or value == 100

'''
Argument A	Argument B	A or B
False	False	False
False	True	True
True	False	True
True	True	True
'''

'''
not
In addition, there's another operator that can be applied for constructing conditions. It's a unary operator performing a logical negation. Its operation is simple: it turns truth into falsehood and falsehood into truth.

This operator is written as the word not, and its priority is very high: the same as the unary + and -. Its truth table is simple:
'''

not counter > 0

'''
Argument	not Argument
False	True
True	False
'''

