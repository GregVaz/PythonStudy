
#Stack 
'''
A stack is a structure developed to store data in a very specific way. Imagine a stack of coins. You aren't able to put a coin anywhere else but on the top of the stack. Similarly, you can't get a coin off the stack from any place other than the top of the stack. If you want to get the coin that lies on the bottom, you have to remove all the coins from the higher levels.

The alternative name for a stack (but only in IT terminology) is LIFO. It's an abbreviation for a very clear description of the stack's behavior: Last In - First Out. The coin that came last onto the stack will leave first.

A stack is an object with two elementary operations, conventionally named push (when a new element is put on the top) and pop (when an existing element is taken away from the top).
'''

#First, you have to decide how to store the values which will arrive onto the stack. We suggest using the simplest of methods, and employing a list for this job

stack = []

def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

'''

The stack - the procedural approach vs. the object-oriented approach

The procedural stack is ready. Of course, there are some weaknesses, and the implementation could be improved in many ways (harnessing exceptions to work is a good idea), but in general the stack is fully implemented, and you can use it if you need to.

But the more often you use it, the more disadvantages you'll encounter. Here are some of them:

    the essential variable (the stack list) is highly vulnerable; anyone can modify it in an uncontrollable way, destroying the stack, in effect; this doesn't mean that it's been done maliciously - on the contrary, it may happen as a result of carelessness, e.g., when somebody confuses variable names; imagine that you have accidentally written something like this:

    stack[0] = 0

    The functioning of the stack will be completely disorganized;

    it may also happen that one day you need more than one stack; you'll have to create another list for the stack's storage, and probably other push and pop functions too;

    it may also happen that you need not only push and pop functions, but also some other conveniences; you could certainly implement them, but try to imagine what would happen if you had dozens of separately implemented stacks.



The objective approach delivers solutions for each of the above problems. Let's name them first:

    the ability to hide (protect) selected values against unauthorized access is called encapsulation; the encapsulated values can be neither accessed nor modified if you want to use them exclusively;

    when you have a class implementing all the needed stack behaviors, you can produce as many stacks as you want; you needn't copy or replicate any part of the code;

    the ability to enrich the stack with new functions comes from inheritance; you can create a new class (a subclass) which inherits all the existing traits from the superclass, and adds some new ones.

'''

