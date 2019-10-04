# The simplest way to import a particular module is to use the import instruction as follows:
import math

# The clause contains:
#     the import keyword;
#     the name of the module which is subject to import.
# The instruction may be located anywhere in your code, but it must be placed before the first use of any of the module's entities. 

# If the module of a specified name exists and is accessible (a module is in fact a Python source file), Python imports its contents, i.e., all the names defined in the module become known, but they don't enter your code's namespace.

# This means that you can have your own entities named sin or pi and they won't be affected by the import in any way.
# The namespace concept: math and pi

print(math.sin(math.pi/2))

# Now we're going to show you how the two namespaces (yours and the module's one) can coexist.

import math

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

'''
In the second method, the import's syntax precisely points out which module's entity (or entities) are acceptable in the code:
from math import pi

The instruction consists of the following elements:

    the from keyword;
    the name of the module to be (selectively) imported;
    the import keyword;
    the name or list of names of the entity/entities which are being imported into the namespace.

The instruction has this effect:

    the listed entities (and only those ones) are imported from the indicated module;
    the names of the imported entities are accessible without qualification.
'''

from math import e

print(e)


# They supersede the original (imported) definitions within the code's namespace;
from math import sin, pi

print(sin(pi/2))

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))



'''
In the third method, the import's syntax is a more aggressive form of the previously presented one:

from module import *


As you can see, the name of an entity (or the list of entities' names) is replaced with a single asterisk (*).

Such an instruction imports all entities from the indicated module.

Is it convenient? Yes, it is, as it relieves you of the duty of enumerating all the names you need.

Is it unsafe? Yes, it is - unless you know all the names provided by the module, you may not be able 
to avoid name conflicts. Treat this as a temporary solution, and try not to use it in regular code.
'''
from time import *


'''
If you use the import module variant and you don't like a particular module's name (e.g., it's the same as one of your already defined entities, so qualification becomes troublesome) you can give it any name you like - this is called aliasing.

Aliasing causes the module to be identified under a different name than the original. This may shorten the qualified names, too.

Creating an alias is done together with importing the module, and demands the following form of the import instruction:
import module as alias

The "module" identifies the original module's name while the "alias" is the name you wish to use instead of the original.

This is how it can be done:
from module import name as alias

The phrase name as alias can be repeated - use commas to separate the multiplied phrases, like this:
from module import n as a, m as b, o as c
'''

import itertools as tools