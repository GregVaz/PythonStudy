'''
Computers store characters as numbers. Every character used by a computer corresponds to a unique number, and vice versa. This assignment must include more characters than you might expect. Many of them are invisible to humans, but essential to computers.

Some of these characters are called whitespaces, while others are named control characters, because their purpose is to control input/output devices.

An example of a whitespace that is completely invisible to the naked eye is a special code, or a pair of codes (different operating systems may treat this issue differently), which are used to mark the ends of the lines inside text files.

People do not see this sign (or these signs), but are able to observe the effect of their application where the lines are broken.

We can create virtually any number of character-number assignments, but life in a world in which every type of computer uses a different character encoding would not be very convenient. This system has led to a need to introduce a universal and widely accepted standard implemented by (almost) all computers and operating systems all over the world.


The one named ASCII (short for American Standard Code for Information Interchange) is the most widely used, and you can assume that nearly all modern devices (like computers, printers, mobile phones, tablets, etc.) use that code.

The code provides space for 256 different characters, but we are interested only in the first 128. If you want to see how the code is constructed, look at the table below. Click the table to enlarge it. Look at it carefully - there are some interesting facts. Look at the code of the most common character - the space. This is 32.
'''

'''

I18N

Of course, the Latin alphabet is not sufficient for the whole of mankind. Users of that alphabet are in the minority. It was necessary to come up with something more flexible and capacious than ASCII, something able to make all the software in the world amenable to internationalization, because different languages use completely different alphabets, and sometimes these alphabets are not as simple as the Latin one.

The word internationalization is commonly shortened to I18N.
I18N Internationalization

Why? Look carefully - there is an I at the front of the word, next there are 18 different letters, and an N at the end.

Despite the slightly humorous origin, the term is officially used in many documents and standards.

The software I18N is a standard in present times. Each program has to be written in a way that enables it to be used all around the world, among different cultures, languages and alphabets.

A classic form of ASCII code uses eight bits for each sign. Eight bits mean 256 different characters. The first 128 are used for the standard Latin alphabet (both upper-case and lower-case characters). Is it possible to push all the other national characters used around the world into the remaining 128 locations?

No. It isn't.


Code points and code pages

We need a new term now: a code point.

A code point is a number which makes a character. For example, 32 is a code point which makes a space in ASCII encoding. We can say that standard ASCII code consists of 128 code points.

As standard ASCII occupies 128 out of 256 possible code points, you can only make use of the remaining 128.

It's not enough for all possible languages, but it may be sufficient for one language, or for a small group of similar languages.

Can you set the higher half of the code points differently for different languages? Yes, you can. Such a concept is called a code page.

A code page is a standard for using the upper 128 code points to store specific national characters. For example, there are different code pages for Western Europe and Eastern Europe, Cyrillic and Greek alphabets, Arabic and Hebrew languages, and so on.

This means that the one and same code point can make different characters when used in different code pages.

For example, the code point 200 makes Č (a letter used by some Slavic languages) when utilized by the ISO/IEC 8859-2 code page, and makes Ш (a Cyrillic letter) when used by the ISO/IEC 8859-5 code page.

In consequence, to determine the meaning of a specific code point, you have to know the target code page.

In other words, the code points derived from code the page concept are ambiguous.
'''

'''

Unicode

Code pages helped the computer industry to solve I18N issues for some time, but it soon turned out that they would not be a permanent solution.

The concept that solved the problem in the long term was Unicode.
UNICODE

Unicode assigns unique (unambiguous) characters (letters, hyphens, ideograms, etc.) to more than a million code points. The first 128 Unicode code points are identical to ASCII, and the first 256 Unicode code points are identical to the ISO/IEC 8859-1 code page (a code page designed for western European languages).
UCS-4

The Unicode standard says nothing about how to code and store the characters in the memory and files. It only names all available characters and assigns them to planes (a group of characters of similar origin, application, or nature).
UCS-4

There is more than one standard describing the techniques used to implement Unicode in actual computers and computer storage systems. The most general of them is UCS-4.

The name comes from Universal Character Set.

UCS-4 uses 32 bits (four bytes) to store each character, and the code is just the Unicode code points' unique number. A file containing UCS-4 encoded text may start with a BOM (byte order mark), an unprintable combination of bits announcing the nature of the file's contents. Some utilities may require it.



As you can see, UCS-4 is a rather wasteful standard - it increases a text's size by four times compared to standard ASCII. Fortunately, there are smarter forms of encoding Unicode texts.
UTF-8

One of the most commonly used is UTF-8.

The name is derived from Unicode Transformation Format.

The concept is very smart. UTF-8 uses as many bits for each of the code points as it really needs to represent them.
UTF-8 - humorous graphics

For example:

    all Latin characters (and all standard ASCII characters) occupy eight bits;
    non-Latin characters occupy 16 bits;
    CJK (China-Japan-Korea) ideographs occupy 24 bits.

Due to features of the method used by UTF-8 to store the code points, there is no need to use the BOM, but some of the tools look for it when reading the file, and many editors set it up during the save.

Python 3 fully supports Unicode and UTF-8:

    you can use Unicode/UTF-8 encoded characters to name variables and other entities;
    you can use them during all input and output.

This means that Python3 is completely I18Ned.
'''

#Operation on strings

'''
In general, strings can be:

    concatenated (joined)
    replicated.
'''

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)


# function ord()

'''
If you want to know a specific character's ASCII/UNICODE code point value, you can use a function named ord() (as in ordinal).

The function needs a >strong>one-character string as its argument - breaching this requirement causes a TypeError exception, and returns a number representing the argument's code point.
'''

ch1 = 'a' 
ch2 = ' ' # space

print(ord(ch1))
print(ord(ch2))

# function chr()

'''
If you know the code point (number) and want to get the corresponding character, you can use a function named chr().

The function takes a code point and returns its character.
'''

print(chr(97)) # Result: a
print(chr(945))


# Strings as sequences: indexing

'''


We told you before that Python's strings are sequences. It's time to show you what that actually means.

Strings aren't lists, but you can treat them like lists in many particular cases.

For example, if you want to access any of a string's characters, you can do it using indexing
'''

exampleString = 'Hello world'

for ix in range(len(exampleString)):
    print(exampleString[ix], end=' ')


# Slices

'''
Slices

Moreover, everything you know about slices is still usable.

We've gathered some examples showing how slices work in the string world.
'''

alpha = "interno"

print(alpha[1:3])
print(alpha[3:])


#The in and not in operators

'''
The in operator shouldn't surprise you when applied to strings - it simply checks if its left argument (a string) can be found anywhere within the right argument (another string).

The result of the check is simply True or False.
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)


#Python strings are immutable

'''
We've also told you that Python's strings are immutable. This is a very important feature. What does it mean?

This primarily means that the similarity of strings and lists is limited. Not everything you can do with a list may be done with a string.

The first important difference doesn't allow you to use the del instruction to remove anything from a string.
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"

del alphabet[1]

'''
Traceback (most recent call last):

  File "main.py", line 4, in <module>

    del alphabet[1]

TypeError: 'str' object doesn't support item deletion
'''


#Operations on strings: min()

'''
Now that you understand that strings are sequences, we can show you some less obvious sequence capabilities. We'll present them using strings, but don't forget that lists can adopt the same tricks, too.

Let's start with a function named min().

The function finds the minimum element of the sequence passed as an argument. There is one condition - the sequence (string, list, it doesn't matter) cannot be empty, or else you'll get a ValueError exception.
'''

print(min("aAbByYzZ")) # Result: A

t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']') # Result: [ ]

t = [0, 1, 2]
print(min(t)) #Result: 0


#Operations on strings: max()
'''
Similarly, a function named max() finds the maximum element of the sequence.
'''

print(max("aAbByYzZ")) # Result: z

t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']') #Result: [y]

t = [0, 1, 2]
print(max(t)) #Result: 2


#Operations on strings: the index() method

'''
The index() method (it's a method, not a function) searches the sequence from the beginning, in order to find the first element of the value specified in its argument.

Note: the element searched for must occur in the sequence - its absence will cause a ValueError exception.

The method returns the index of the first occurrence of the argument (which means that the lowest possible result is 0, while the highest is the length of argument decremented by 1). 
'''

print("aAbByYzZaA".index("b")) #result:2
print("aAbByYzZaA".index("Z")) #result:7
print("aAbByYzZaA".index("A")) #result:1


# Operations on strings: the list() function

'''
The list() function takes its argument (a string) and creates a new list containing all the string's characters, one per list element.

Note: it's not strictly a string function - list() is able to create a new list from many other entities (e.g., from tuples and dictionaries).
'''

print(list("abcabc")) # ['a', 'b', 'c', 'a', 'b', 'c']


#Operations on strings: the count() method

'''
The count() method counts all occurrences of the element inside the sequence. The absence of such elements doesn't cause any problems.
'''

print("abcabc".count("b")) #result: 2
print('abcabc'.count("d")) #result: 0

