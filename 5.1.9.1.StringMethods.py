#The capitalize() method

'''
Let's go through some standard Python string methods. We're going to go through them in alphabetical order - to be honest, any order has as many disadvantages as advantages, so the choice may as well be random.

The capitalize() method does exactly what it says - it creates a new string filled with characters taken from the source string, but it tries to modify them in the following way:

    if the first character inside the string is a letter (note: the first character is an element with an index equal to 0, not just the first visible character), it will be converted to upper-case;
    all remaining letters from the string will be converted to lower-case.

Don't forget that:

    the original string (from which the method is invoked) is not changed in any way (a string's immutability must be obeyed without reservation)
    the modified (capitalized in this case) string is returned as a result - if you don't use it in any way (assign it to a variable, or pass it to a function/method) it will disappear without a trace.
'''

print("Alpha".capitalize()) # result: Alpha
print('ALPHA'.capitalize()) # result: Alpha
print(' Alpha'.capitalize()) # result: alpha
print('123'.capitalize()) # result: 123
print("αβγδ".capitalize()) # result: αβγδ


#The center() method

'''
The one-parameter variant of the center() method makes a copy of the original string, trying to center it inside a field of a specified width.

The centering is actually done by adding some spaces before and after the string.

Don't expect this method to demonstrate any sophisticated skills. It's rather simple.

The example in the editor uses brackets to clearly show you where the centered string actually begins and terminates.
'''

print('[' + 'alpha'.center(10) + ']') #Result: [  alpha   ]

print('[' + 'Beta'.center(2) + ']') #Result: [Beta]
print('[' + 'Beta'.center(4) + ']') #Result: [Beta]
print('[' + 'Beta'.center(6) + ']') #Result: [ Beta ]

print('[' + 'gamma'.center(20, '*') + ']') #Result: [*******gamma********]



# The endswith() method
'''
The endswith() method checks if the given string ends with the specified argument and returns True or False, depending on the check result.

Note: the substring must adhere to the string's last character - it cannot just be located somewhere near the end of the string.
'''
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

t = "zeta"
print(t.endswith("a")) #result: True
print(t.endswith("A")) #result: False
print(t.endswith("et")) #result: False
print(t.endswith("eta")) #result: True


# The find method()
'''
The find() method is similar to index(), which you already know - it looks for a substring and returns the index of first occurrence of this substring, but:

    it's safer - it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
    it works with strings only - don't try to apply it to any other sequence.
'''
print("Eta".find("ta")) #Return: 1 (position)
print("Eta".find("mma")) #Return: -1 (position)

    #Note: don't use find() if you only want to check if a single character occurs within a string - the in

txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)

'''
Return:
15
80
198
221
238
'''

#The isalnum() method
'''
The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (letters), and returns True or False according to the result.

Look at the example in the editor and run it.

Note: any string element that is not a digit or a letter causes the method to return False. An empty string does, too.
'''
print('lambda30'.isalnum()) # True
print('lambda'.isalnum()) # True
print('30'.isalnum()) # True 
print('@'.isalnum()) # False
print('lambda_30'.isalnum()) # False
print(''.isalnum()) # False

t = 'Six lambdas'
print(t.isalnum()) # False

t = 'ΑβΓδ'
print(t.isalnum()) # True

t = '20E1'
print(t.isalnum()) # True


# The isalpha() method
'''
The isalpha() method is more specialized - it's interested in letters only.
'''
print("Moooo".isalpha()) # True
print('Mu40'.isalpha()) # False

# The isdigit() method
'''
In turn, the isdigit() method looks at digits only - anything else produces False as the result.
'''
print('2018'.isdigit()) # True
print("Year2019".isdigit()) # False


# The islower() method
'''
The islower() method is a fussy variant of isalpha() - it accepts lower-case letters only.
'''
print("Moooo".islower()) # False
print('moooo'.islower()) # True

# The isspace() method
'''
The isspace() method identifies whitespaces only - it disregards any other character (the result is False then).
'''
print(' \n '.isspace()) # True
print(" ".isspace()) # True
print("mooo mooo mooo".isspace()) # False


# The isupper() method
'''
The isupper() method is the upper-case version of islower() - it concentrates on upper-case letters only.
'''
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())


# The join() method
'''
The join() method is rather complicated, so let us guide you step by step thorough it:

    as its name suggests, the method performs a join - it expects one argument as a list; it must be assured that all the list's elements are strings - the method will raise a TypeError exception otherwise;
    all the list's elements will be joined into one string but...
    ...the string from which the method has been invoked is used as a separator, put among the strings;
    the newly created string is returned as a result.
'''

print(",".join(["omicron", "pi", "rho"])) # omicron,pi,rho


#The lower() method
'''
The lower() method makes a copy of a source string, replaces all upper-case letters with their lower-case counterparts, and returns the string as the result. Again, the source string remains untouched.

If the string doesn't contain any upper-case characters, the method returns the original string.

Note: The lower() method doesn't take any parameters.
'''

print("SiGmA=60".lower()) # sigma=60


# The lstrip() method
'''
The parameterless lstrip() method returns a newly created string formed from the original one by removing all leading whitespaces.

The one-parameter lstrip() method does the same as its parameterless version, but removes all characters enlisted in its argument (a string), not just whitespaces:
print("www.cisco.com".lstrip("w."))

Brackets aren't needed here, as the output looks as follows:
cisco.com
'''

print("[" + " tau ".lstrip() + "]") # [tau ]


#The replace() method
'''
The two-parameter replace() method returns a copy of the original string in which all occurrences of the first argument have been replaced by the second argument.

The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.
'''

print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) # www.pyhoninstitute.org
print("This is it!".replace("is", "are")) # Thare are it!
print("Apple juice".replace("juice", "")) # Apple

print("This is it!".replace("is", "are", 1)) # Thare is it!


# The rfind() method
'''
The one-, two-, and three-parameter methods named rfind() do nearly the same things as their counterparts (the ones devoid of the r prefix), but start their searches from the end of the string, not the beginning (hence the prefix r, for right).
'''

print("tau tau tau".rfind("ta")) # 8
print("tau tau tau".rfind("taz", 9)) # -1
print("tau tau tau".rfind("ta", 3, 9)) # 4



# The rstrip() method
'''
Two variants of the rstrip() method do nearly the same as lstrips, but affect the opposite side of the string.
'''

print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))



# The split() method
'''
The split() method does what it says - it splits the string and builds a list of all detected substrings.

The method assumes that the substrings are delimited by whitespaces - the spaces don't take part in the operation, and aren't copied into the resulting list.
'''

print("phi       chi\npsi".split()) # ['phi', 'chi', 'psi']
print("phi,chi,psi".split(",")) # ['phi', 'chi', 'psi']


# The startswith() method
'''
The startswith() method is a mirror reflection of endswith() - it checks if a given string starts with the specified substring.
'''

print("omega".startswith("meg")) # False
print("omega".startswith("om")) # True


# The strip() method
'''
The trip() method combines the effects caused by rstrip() and lstrip() - it makes a new string lacking all the leading and trailing whitespaces.
'''

print("[" + "   aleph   ".strip() + "]") # [aleph]



# The swapcase() method
'''print('lambda'.isalnum()) # Trueprint('laprint('lambda'.isalnum()) # True
print('lambda'.isalnum()) # True
print('lambda'.isalnum()) # True
mbda'.isalnum()) # True


The swapcase() method makes a new string by swapping the case of all letters within the source string: lower-case characters become upper-case, and vice versa.
'''
print("I know that I know nothing.".swapcase()) # i KNOW THAT i KNOW NOTHING.


#The title() method
'''
The title() method performs a somewhat similar function - it changes every word's first letter to upper-case, turning all other ones to lower-case.

'''
print("I know that I know nothing. Part 1.".title()) # I Know That I Know Nothing. Part 1.
print('lambda'.isalnum()) # Trueprint('lambda'.isalnum()) # True



#The upper() method
'''
Last but not least, the upper() method makes a copy of the source string, replaces all lower-case letters with their upper-case counterparts, and returns the string as the result.
'''
print("I know that I know nothing. Part 2.".upper()) # I KNOW THAT I KNOW NOTHING. PART 2.
