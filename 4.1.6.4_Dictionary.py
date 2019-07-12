'''
What is a dictionary?
The dictionary is another Python data structure. It's not a sequence type (but can be easily adapted to sequence processing) and it is mutable.

In Python's world, the word you look for is named a key. The word you get from the dictionary is called a value.

This means that a dictionary is a set of key-value pairs. Note:

each key must be unique - it's not possible to have more than one key of the same value;
a key may be data of any type: it may be a number (integer or float), or even a string;
a dictionary is not a list - a list contains a set of numbered values, while a dictionary holds pairs of values;
the len() function works for dictionaries, too - it returns the numbers of key-value elements in the dictionary;
a dictionary is a one-way tool - if you have an English-French dictionary, you can look for French equivalents of English terms, but not vice versa.

How to make a dictionary?
If you want to assign some initial pairs to a dictionary, you should use the following syntax:
'''

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
emptyDictionary = {}

print(dict)
print(phoneNumbers)
print(emptyDictionary)

'''
In the first example, the dictionary uses keys and values which are both strings. In the second one, the keys are strings, but the values are integers. The reverse layout (keys → numbers, values → strings) is also possible, as well as number-number combination.

The list of pairs is surrounded by curly braces, while the pairs themselves are separated by commas, and the keys and values by colons.

The first of our dictionaries is a very simple English-French dictionary. The second - a very tiny telephone directory.

The empty dictionaries are constructed by an empty pair of curly braces - nothing unusual.
'''

#(*) In Python 3.6x dictionaries have become ordered collections by default. Your results may vary depending on what Python version you're using.

key = "boss"
if key in phoneNumbers:
    print(key," -> ", phoneNumbers['boss'])
else:
    print(key, " no se encuentra en la lista de numeros")

'''
Can dictionaries be browsed using the for loop, like lists or tuples?

No and yes.

No, because a dictionary is not a sequence type - the for loop is useless with it.

Yes, because there are simple and very effective tools that can adapt any dictionary to the for 
loop requirements (in other words, building an intermediate link between the dictionary and a temporary sequence entity).

The first of them is a method named keys(), possessed by each dictionary. The method returns a 
list built of all the keys gathered within the dictionary. Having a list of keys enables you to access the whole dictionary in an easy and handy way.
'''

for key in dict.keys():
    print(key, "->", dict[key]


# Do you want it sorted? Just enrich the for loop to get such a form:
for key in sorted(dict.keys()):
    print(key, "->", dict[key])


'''
How to use a dictionary: The item() and values() methods
Another way is based on using a dictionary's method named items(). The method returns a list of tuples (this is the first example where tuples are something more than just an example of themselves) where each tuple is a key-value pair.

This is how it works:
'''

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

for english, french in dict.items():
    print(english, "->", french)

# Note the way in which the tuple has been used as a for loop variable.



# There is also a method named values(), which works similarly to keys(), but returns a list of values.

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

for french in dict.values():
    print(french)

# As the dictionary is not able to automatically find a key for a given value, the role of this method is rather limited.


'''
How to use a dictionary: modifying and adding values
Assigning a new value to an existing key is simple - as dictionaries are fully mutable, there are no obstacles to modifying them.

We're going to replace the value "chat" with "minou", which is not very accurate, but it will work well with our example.
'''

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

dict['cat'] = 'minou'
print(dict)

# The output is:

# {'dog': 'chien', 'horse': 'cheval', 'cat': 'minou'}

'''
Adding a new key
Adding a new key-value pair to a dictionary is as simple as changing a value - you only have to assign a value to a new, previously non-existent key.

Note: this is very different behavior compared to lists, which don't allow you to assign values to non-existing indices.

Let's add a new pair of words to the dictionary - a bit weird, but still valid:
'''

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

dict['swan'] = 'cygne'
print(dict)

# The example outputs:

# {'swan': 'cygne', 'horse': 'cheval', 'dog': 'chien', 'cat': 'chat'}


# You can also insert an item to a dictionary by using the update() method, e.g.:

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

dict.update({"duck" : "canard"})
print(dict)

# Removing a key
# Can you guess how to remove a key from a dictionary?

# Note: removing a key will always cause the removal of the associated value. Values cannot exist without their keys.

# This is done with the del instruction.

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

del dict['dog']
print(dict)

# Note: removing a non-existing key causes an error.


# To remove the last item in a dictionary, you can use the popitem() method:

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

dict.popitem()
print(dict)    # outputs: {'cat' : 'chat', 'dog' : 'chien'}

# In the older versions of Python, i.e., before 3.6.7, the popitem() method removes a random item from a dictionary.


'''
Tuples and dictionaries can work together
We've prepared a simple example, showing how tuples and dictionaries can work together.

Let's imagine the following problem:

you need a program to evaluate the students' average scores;
the program should ask for the student's name, followed by her/his single score;
the names may be entered in any order;
entering an empty name finishes the inputting of the data;
a list of all names, together with the evaluated average score, should be then emitted.
'''

schoolClass = {}

while True:
    name = input("Enter the student's name (or type exit to stop): ")
    if name == 'exit':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    
    if name in schoolClass:
        schoolClass[name] += (score,)
    else:
        schoolClass[name] = (score,)

print(schoolClass)
        
for name in sorted(schoolClass.keys()):
    sum = 0
    counter = 0
    for score in schoolClass[name]:
        sum += score
        counter += 1
    print(name, ":", sum / counter)


'''
1. Dictionaries are unordered*, changeable (mutable), and indexed collections of data. (*In Python 3.6x dictionaries have become ordered by default.

Each dictionary is a set of key : value pairs. You can create it by using the following syntax:
'''

myDictionary = {
    key1 : value1,
    key2 : value2,
    key3 : value3,
    }

'''
2. If you want to access a dictionary item, you can do so by making a reference to its key inside a pair of square brackets (ex. 1) or by using the get() method (ex. 2):
'''

polEngDict = {
    "kwiat" : "flower",
    "woda"  : "water",
    "gleba" : "soil"
    }

item1 = polEngDict["gleba"]    # ex. 1
print(item1)    # outputs: soil

item2 = polEngDict.get("woda")
print(item2)    # outputs: water

'''
3. If you want to change the value associated with a specific key, you can do so by referring to the item's key name in the following way:
'''

polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

polEngDict["zamek"] = "lock"
item = polEngDict["zamek"]    # outputs: lock

'''
4. To add or remove a key (and the associated value), use the following syntax:
'''

myPhonebook = {}    # an empty dictionary

myPhonebook["Adam"] = 3456783958    # create/add a key-value pair
print(myPhonebook)    # outputs: {'Adam': 3456783958}

del myPhonebook["Adam"]
print(myPhonebook)    # outputs: {}

# You can also insert an item to a dictionary by using the update() method, and remove the last element by using the popitem() method, e.g.:

polEngDict = {"kwiat" : "flower"}

polEngDict = update("gleba" : "soil")
print(polEngDict)    # outputs: {'kwiat' : 'flower', 'gleba' : 'soil'}

polEngDict.popitem()
print(polEngDict)    # outputs: {'kwiat' : 'flower'}

'''
5. You can use the for loop to loop through a dictionary, e.g.:
'''

polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

for item in polEngDict:
    print(item)    # outputs: zamek
                   #          woda
                   #          gleba



'''
6. If you want to loop through a dictionary's keys and values, you can use the items() method, e.g.:
'''

polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

for key, value in polEngDict.items():
    print("Pol/Eng ->", key, ":", value)

'''
7. To check if a given key exists in a dictionary, you can use the in keyword:
'''

polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

if "zamek" in polEngDict:
    print("Yes")
else:
    print("No")

'''
8. You can use the del keyword to remove a specific item, or delete a dictionary. To remove all the dictionary's items, you need to use the clear() method:
'''

polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

print(len(polEngDict))    # outputs: 3
del polEngDict["zamek"]    # remove an item
print(len(polEngDict))    # outputs: 2

polEngDict.clear()   # removes all the items
print(len(polEngDict))    # outputs: 0

del polEngDict    # removes the dictionary

'''
9. To copy a dictionary, use the copy() method:
'''

polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

copyDict = polEngDict.copy()