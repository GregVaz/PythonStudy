'''
It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:

    asks the user for some text;
    checks whether the entered text is a palindrome, and prints result.

Note:

    assume that an empty string isn't a palindrome;
    treat upper- and lower-case letters as equal;
    spaces are not taken into account during the check - treat them as non-existent;
    there are more than a few correct solutions - try to find more than one.

Test your code using the data we've provided.
Test data

Sample input:
Ten animals I slam in a net

It's a palindrome

Sample input:
Eleven animals I slam in a net

It's not a palindrome 
'''


def isPalindrome(text):
    palindromo = True
    compar = text.lower().replace(" ","")
    for i in range(len(compar)):
        if(compar[i] != compar[len(compar)-i-1]):
            palindromo = False
            break
    print(text + " es un palindromo" if palindromo else text + " no es un palindromo")

def isPalindromeList(text):
    palindromo = True
    compar = text.lower().replace(" ","")
    list1 = [char for char in compar]
    list2 = list1.copy()
    list2.reverse()
    if list1!=list2:
        palindromo = False
    print(text + " es un palindromo" if palindromo else text + " no es un palindromo")

isPalindromeList("Ten animals I slam in a net")