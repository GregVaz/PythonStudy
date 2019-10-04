'''
Writing your own modules doesn't differ much from writing ordinary scripts.

There are some specific aspects you must be aware of, but it definitely isn't rocket science. You'll see this soon enough.
The Package-Module-Function concept


Let's summarize some important issues:

a module is a kind of container filled with functions - you can pack as many functions as you want into one module and distribute it across the world;
of course, it's generally a good idea not to mix functions with different application areas within one module (just like in a library - nobody expects scientific works to be put among comic books), so group your functions carefully and name the module containing them in a clear and intuitive way (e.g., don't give the name arcade_games to a module containing functions intended to partition and format hard disks)
making many modules may cause a little mess - sooner or later you'll want to group your modules exactly in the same way as you've previously grouped functions - is there a more general container than a module?
yes, there is - it's a package; in the world of modules, a package plays a similar role to a folder/directory in the world of files.
'''

# Your fist module

'''
We've named the file module.py. Not very creative, but simple and clear.

The second file contains the code using the new module. Its name is main.py.

Inside the main.py file write: 
    import module


Run the main.py file. What do you see?

You should see nothing. This means that Python has successfully imported the contents of the module.py file. It doesn't matter that the module is empty for now. The very first step has been done, but before you take the next step, we want you to take a look into the folder in which both files exist.

Do you notice something interesting?

A new subfolder has appeared - can you see it? Its name is __pycache__. Take a look inside. What do you see?

There is a file named (more or less) module.cpython-xy.pyc where x and y are digits derived from your version of Python (e.g., they will be 3 and 4 if you use Python 3.4).

The name of the file is the same as your module's name (module here). The part after the first dot says which Python implementation has created the file (CPython here) and its version number. The last part (pyc) comes from the words Python and compiled.

You can look inside the file - the content is completely unreadable to humans. It has to be like that, as the file is intended for Python's use only.

When Python imports a module for the first time, it translates its contents into a somewhat compiled shape. The file doesn't contain machine code - it's internal Python semi-compiled code, ready to be executed by Python's interpreter. As such a file doesn't require lots of the checks needed for a pure source file, the execution starts faster, and runs faster, too.

Thanks to that, every subsequent import will go quicker than interpreting the source text from scratch.

Python is able to check if the module's source file has been modified (in this case, the pyc file will be rebuilt) or not (when the pyc file may be run at once). As this process is fully automatic and transparent, you don't have to keep it in mind.

'''


