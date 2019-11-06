# Let's start from the absolute beginning - this is how the objective stack begins:
class Stack(): 
    def __init__(self):
        print("Hi")

stackObj = Stack()

'''
Now, we expect two things from it:

    we want the class to have one property as the stack's storage - we have to "install" a list inside each object of the class (note: each object has to have its own list - the list mustn't be shared among different stacks)
    then, we want the list to be hidden from the class users' sight.

How is this done?

In contrast to other programming languages, Python has no means of allowing you to declare such a property just like that.

Instead, you need to add a specific statement or instruction. The properties have to be added to the class manually.

How do you guarantee that such an activity takes place every time the new stack is created?

There is a simple way to do it - you have to equip the class with a specific function - its specificity is dual:

    it has to be named in a strict way;
    it is invoked implicitly, when the new object is created.

Such a function is called a constructor, as its general purpose is to construct a new object. The constructor should know everything about the object's structure, and must perform all the needed initializations.

And now:

    the constructor's name is always __init__;
    it has to have at least one parameter (we'll discuss this later); the parameter is used to represent the newly created object - you can use the parameter to manipulate the object, and to enrich it with the needed properties; you'll make use of this soon;
    note: the obligatory parameter is usually named self - it's only a convention, but you should follow it - it simplifies the process of reading and understanding your code.

'''


class Stack:
    def __init__(self):
        self.stackList = []

stackObject = Stack()
print(len(stackObject.stackList))

'''
Any change you make inside the constructor that modifies the state of the self parameter will reflect the newly created object.

This means you can add any property to the object and the property will remain there until the object finishes its life or the property is explicitly removed.

Now let's add just one property to the new object - a list for a stack. We'll name it stackList.
'''


class Stack:
    def __init__(self):
        self.__stackList = []

stackObject = Stack()
print(len(stackObject.__stackList))

'''
The change invalidates the program.

Why?

When any class component has a name starting with two underscores (__), it becomes private - this means that it can be accessed only from within the class.

You cannot see it from the outside world. This is how Python implements the encapsulation concept.

Run the program to test our assumptions - an AttributeError exception should be raised.
'''

#complete
class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


stackObject = Stack()

stackObject.push(3)
stackObject.push(2)
stackObject.push(1)

print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())

'''
However, there's something really strange in the code. The functions look familiar, but they have more parameters than their procedural counterparts.

Here, both functions have a parameter named self at the first position of the parameters list.

Is it needed? Yes, it is.

All methods have to have this parameter. It plays the same role as the first constructor parameter.

It allows the method to access entities (properties and activities/methods) carried out by the actual object. You cannot omit it. Every time Python invokes a method, it implicitly sends the current object as the first argument.

This means that a method is obligated to have at least one parameter, which is used by Python itself - you don't have any influence on it.

If your method needs no parameters at all, this one must be specified anyway. If it's designed to process just one parameter, you have to specify two, and the first one's role is still the same.

There is one more thing that requires explanation - the way in which methods are invoked from within the __stackList variable.
'''


# call a superclass
class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

'''
The new class should be able to evaluate the sum of all the elements currently stored on the stack.

The first step is easy: just define a new subclass pointing to the class which will be used as the superclass.
It gets all the components defined by its superclass - the name of the superclass is written after the colon directly after the new class name.

Firstly, let's add a new variable to the class. It'll be a private variable, like the stack list. We don't want anybody to manipulate the sum value.

As you already know, adding a new property to the class is done by the constructor. 
But the line before it looks different. What does it do? Is it really necessary? Yes, it is.

Contrary to many other languages, Python forces you to explicitly invoke a superclass's constructor. Omitting this point will have harmful effects - the object will be deprived of the __stackList list. Such a stack will not function properly.

This is the only time you can invoke any of the available constructors explicitly - it can be done inside the superclass's constructor.

Note the syntax:

    you specify the superclass's name (this is the class whose constructor you want to run)
    you put a dot (.)after it;
    you specify the name of the constructor;
    you have to point to the object (the class's instance) which has to be initialized by the constructor - this is why you have to specify the argument and use the self variable here; note: invoking any method (including constructors) from outside the class never requires you to put the self argument at the argument's list - invoking a method from within the class demands explicit usage of the self argument, and it has to be put first on the list.
'''



class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    
    def push(self, val):
        self.__sum += val
        Stack.push(self,val)
    
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        
    def getSum(self):
        val = self.__sum
        return val

stack = AddingStack()
stack.push(5)
stack.push(10)
stack.pop()
print(stack.getSum())

