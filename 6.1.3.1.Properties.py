
# Instance variables

'''
In general, a class can be equipped with two different kinds of data to form a class's properties. You already saw one of them when we were looking at stacks.

This kind of class property exists when and only when it is explicitly created and added to an object. As you already know, this can be done during the object's initialization, performed by the constructor.

Moreover, it can be done in any moment of the object's life. Furthermore, any existing property can be removed at any time.

Such an approach has some important consequences:

    different objects of the same class may possess different sets of properties;
    there must be a way to safely check if a specific object owns the property you want to utilize (unless you want to provoke an exception - it's always worth considering)
    each object carries its own set of properties - they don't interfere with one another in any way.

Such variables (properties) are called instance variables.

The word instance suggests that they are closely connected to the objects (which are class instances), not to the classes themselves.
'''

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def setSecond(self, val):
        self.second = val


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(3)

exampleObject3 = ExampleClass(4)
exampleObject3.third = 5


print(exampleObject1.__dict__) # property it's  a Dictionary  # {'first': 1}
print(exampleObject2.__dict__) # {'second': 3, 'first': 2}
print(exampleObject3.__dict__) # {'third': 5, 'first': 4}

# There is one additional conclusion that should be stated here: modifying an instance variable of any object has no impact on all the remaining objects



# It's nearly the same as the previous one. The only difference is in the property names. We've added two underscores (__) in front of them.
# As you know, such an addition makes the instance variable private - it becomes inaccessible from the outer world.

class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def setSecond(self, val = 2):
        self.__second = val


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(3)

exampleObject3 = ExampleClass(4)
exampleObject3.__third = 5


print(exampleObject1.__dict__) # {'_ExampleClass__first': 1}
print(exampleObject2.__dict__) # {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
print(exampleObject3.__dict__) # {'_ExampleClass__first': 4, '__third': 5}

'''
When Python sees that you want to add an instance variable to an object and you're going to do it inside any of the object's methods, it mangles the operation in the following way:

    it puts a class name before your name;
    it puts an additional underscore at the beginning.

This is why the __first becomes _ExampleClass__first.
'''

# The name is now fully accessible from outside the class. You can run a code like this:
print(exampleObject1._ExampleClass__first)
# and you'll get a valid result with no errors or exceptions.




#Class variables
'''
A class variable is a property which exists in just one copy and is stored outside any object.

Note: no instance variable exists if there is no object in the class; a class variable exists in one copy even if there are no objects in the class.

Class variables are created differently to their instance siblings. 
'''

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)

print(exampleObject1.__dict__, exampleObject1.counter)
print(exampleObject2.__dict__, exampleObject2.counter)
print(exampleObject3.__dict__, exampleObject3.counter)

#Result
'''
{'_ExampleClass__first': 1} 3
{'_ExampleClass__first': 2} 3
{'_ExampleClass__first': 4} 3

Two important conclusions come from the example:

    class variables aren't shown in an object's __dict__ (this is natural as class variables aren't parts of an object) but you can always try to look into the variable of the same name, but at the class level - we'll show you this very soon;
    a class variable always presents the same value in all class instances (objects)
'''



'''
We told you before that class variables exist even when no class instance (object) had been created.

Now we're going to take the opportunity to show you the difference between these two __dict__ variables, the one from the class and the one from the object.

Look at the code in the editor. The proof is there.

Let's take a closer look at it:

    we define one class named ExampleClass;
    the class defines one class variable named varia;
    the class constructor sets the variable with the parameter's value;
    naming the variable is the most important aspect of the example because:
        changing the assignment to self.varia = val would create an instance variable of the same name as the class's one;
        changing the assignment to varia = val would operate on a method's local variable; (we strongly encourage you to test both of the above cases - this will make it easier for you to remember the difference)
    the first line of the off-class code prints the value of the ExampleClass.varia attribute; note - we use the value before the very first object of the class is instantiated.
'''

class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val

print(ExampleClass.__dict__)    #{'__module__': '__main__', 'varia': 1, '__init__': <function ExampleClass.__init__ at 0x7fa972f230d0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}

exampleObject = ExampleClass(2)

print(ExampleClass.__dict__)    #{'__module__': '__main__', 'varia': 2, '__init__': <function ExampleClass.__init__ at 0x7fa972f230d0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}

print(exampleObject.__dict__)   #{}




#Checking an attribute's existence
'''
Python's attitude to object instantiation raises one important issue - in contrast to other programming languages, you may not expect that all objects of the same class have the same sets of properties.

Just like in the example in the editor. Look at it carefully.

The object created by the constructor can have only one of two possible attributes: a or b.
'''

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1)

print(exampleObject.a)
print(exampleObject.b)




#Checking an attribute's existence: continued
'''
The try-except instruction gives you the chance to avoid issues with non-existent properties.

It's easy - look at the code in the editor.

As you can see, this action isn't very sophisticated. Essentially, we've just swept the issue under the carpet.

Fortunately, there is one more way to cope with the issue.
'''

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1)
print(exampleObject.a)

try:
    print(exampleObject.b)
except AttributeError:
    pass


'''
Python provides a function which is able to safely check if any object/class contains a specified property. The function is named hasattr, and expects two arguments to be passed to it:

    the class or the object being checked;
    the name of the property whose existence has to be reported (note: it has to be a string containing the attribute name, not the name alone)

The function returns True or False.
'''

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1)
print(exampleObject.a)

if hasattr(exampleObject, 'b'):
    print(exampleObject.b)



#Checking an attribute's existence: continued
'''
Don't forget that the hasattr() function can operate on classes, too. You can use it to find out if a class variable is available, just like here in the example in the editor.

The function returns True if the specified class contains a given attribute, and False otherwise.

Can you guess the code's output? Run it to check your guesses.
'''

class ExampleClass:
    attr = 1

print(hasattr(ExampleClass, 'attr')) # True
print(hasattr(ExampleClass, 'prop')) # False




class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2

exampleObject = ExampleClass()

print(hasattr(exampleObject, 'b')) #True
print(hasattr(exampleObject, 'a')) #True
print(hasattr(ExampleClass, 'b'))  #False
print(hasattr(ExampleClass, 'a'))  #True