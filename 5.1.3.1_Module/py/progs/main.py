from module import suml, prodl

# print(module.counter)
'''
As you can see, the main file tries to access the module's counter variable. Is this legal? Yes, it is. Is it usable? 
It may be very usable. Is it safe? That depends - if you trust your module's users, there's no problem; however, 
you may not want the rest of the world to see your personal/private variable.

Unlike many other programming languages, Python has no means of allowing you to hide such variables from 
the eyes of the module's users. You can only inform your users that this is your variable, that they may 
read it, but that they should not modify it under any circumstances.

This is done by preceding the variable's name with _ (one underscore) or __ (two underscores), but remember, 
it's only a convention. Your module's users may obey it or they may not.
'''

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))


# Directory
'''
It's time to make this example more complicated - we've assumed here that the main Python file is located in the same folder/directory as the module to be imported.

Let's give up this assumption and conduct the following thought experiment:

    we are using Windows ® OS (this assumption is important, as the file name's shape depends on it)
    the main Python script lies in C:\Users\user\py\progs and is named main.py
    the module to import is located in C:\Users\user\py\modules 

How to deal with it?

To answer this question, we have to talk about how Python searches for modules. There's a special variable (actually a list) storing all locations 
(folders/directories) that are searched in order to find a module which has been requested by the import instruction.

Python browses these folders in the order in which they are listed in the list - if the module cannot be found in any of these directories, the import fails.

Otherwise, the first folder containing a module with the desired name will be taken into consideration (if any of the remaining folders contains a module of that name, it will be ignored).

The variable is named path, and it's accessible through the module named sys. This is how you can check its regular value:

We've launched the code inside the C:\User\user folder, and we've got:
C:\Users\user
C:\Users\user\AppData\Local\Programs\Python\Python36-32\python36.zip
C:\Users\user\AppData\Local\Programs\Python\Python36-32\DLLs
C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib
C:\Users\user\AppData\Local\Programs\Python\Python36-32
C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages



Note: the folder in which the execution starts is listed in the first path's element.

Note once again: there is a zip file listed as one of the path's elements - it's not an error. Python is able to treat zip files as ordinary folders - this can save lots of storage.

Can you figure out how we can solve the problem?

You can solve it by adding a folder containing the module to the path variable (it's fully modifiable).
'''

from sys import path

path.append("..\\modules")

import module 

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

'''
Note:

    we've doubled the \ inside folder name - do you know why?
        Because a backslash is used to escape other characters - if you want to get just a backslash, you have to escape it.


we've used the relative name of the folder - this will work if you start the main.py file directly from its home folder, and won't work if the current directory doesn't fit the relative path; you can always use an absolute path, like this:

path.append('C:\\Users\\user\\py\\modules')

we've used the append() method - in effect, the new path will occupy the last element in the path list; if you don't like the idea, you can use insert() instead.
'''