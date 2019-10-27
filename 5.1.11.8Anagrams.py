'''
Scenario

An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

    asks the user for two separate texts;
    checks whether, the entered texts are anagrams and prints the result.

Note:

    assume that two empty strings are not anagrams;
    treat upper- and lower-case letters as equal;
    spaces are not taken into account during the check - treat them as non-existent

Test your code using the data we've provided.
Test data

Sample input:
Listen
Silent

Anagrams

Sample input:
modern
norman

Not anagrams 
'''

def isAnagram(text):
    anagram = False
    anag = text.lower().replace(" ","")
    dictW = ["silent","norman","best","informative","encapsulation","dictionary"]
    st2 = [i for i in anag]
    st2.sort()
    for w in dictW:
        st1 = [i for i in w]
        st1.sort()
        if(st1 == st2):
            anagram = True
            anag = w
            break
    print(anag.capitalize() if anagram else text + " not anagrams")
    
isAnagram("tesb")