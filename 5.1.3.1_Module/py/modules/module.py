#!/urs/bin/env Python3

''' module.py - an example of Python module '''

__counter = 0

def suml(list):
    global __counter
    __counter += 1
    sum = 0
    for el in list:
        sum += el
    return sum

def prodl(list):
    global __counter
    __counter += 1
    prod = 1
    for el in list:
        prod *= el
    return prod

if __name__ == "__main__":
    print("I prefer to be a module, but I can do some test for you")
    l = [i+1 for i in range(5)]
    print(suml(l) == 15)
    print(prodl(l) == 120)
else:
    print("I like to be a module")


#  NOTES
'''
We can say that:

    when you run a file directly, its __name__ variable is set to __main__;
    when a file is imported as a module, its __name__ variable is set to the file's name (excluding .py)

A few elements need some explanation, we think:

    the line starting with #! has many names - it may be called shabang, shebang, hashbang, poundbang or even hashpling (don't ask us why). The name itself means nothing here - its role is more important. From Python's point of view, it's just a comment as it starts with #. For Unix and Unix-like OSs (including MacOS) such a line instructs the OS how to execute the contents of the file (in other words, what program needs to be launched to interpret the text). In some environments (especially those connected with web servers) the absence of that line will cause trouble;
    a string (maybe a multiline) placed before any module instructions (including imports) is called the doc-string, and should briefly explain the purpose and contents of the module;
    the functions defined inside the module (suml() and prodl()) are available for import;
    we've used the __name__ variable to detect when the file is run stand-alone, and seized this opportunity to perform some simple tests.

'''