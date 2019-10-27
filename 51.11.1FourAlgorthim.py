# Caesar cipher
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)


'''
This cipher was (probably) invented and used by Gaius Julius Caesar and his troops during the Gallic Wars. The idea is rather simple - every letter of the message is replaced by its nearest consequent (A becomes B, B becomes C, and so on). The only exception is Z, which becomes A.

The program in the editor is a very simple (but working) implementation of the algorithm.
'''


# Caesar cipher - decrypting a message
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)


# Numbers Processor
try:
    line = input("Enter a line of numbers - separate them with spaces: ")
    strings = line.split()
    total = 0
except:
    print("Write almost one number")
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")



The IBAN Validator
'''
The fourth program implements (in a slightly simplified form) an algorithm used by European banks to specify account numbers. The standard named IBAN (International Bank Account Number) provides a simple and fairly reliable method of validating the account numbers against simple typos that can occur during rewriting of the number e.g., from paper documents, like invoices or bills, into computers.

An IBAN-compliant account number consists of:

    a two-letter country code taken from the ISO 3166-1 standard (e.g., FR for France, GB for Great Britain, DE for Germany, and so on)
    two check digits used to perform the validity checks - fast and simple, but not fully reliable, tests, showing whether a number is invalid (distorted by a typo) or seems to be good;
    the actual account number (up to 30 alphanumeric characters - the length of that part depends on the country)
'''

# IBAN Validator

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")


'''
The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

    asks the user for one line of text to encrypt;
    asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
    prints out the encoded text. 
'''
def cipher(code):
    cipher = code
    num = int(input("Number: "))
    text = ''
    for char in cipher:
        if not char.isalpha():
            text += char
            continue
        code = ord(char) + num
        if code > ord('z'):
            code = ord('a') + (code-ord('z')-1)
        if code > ord('Z') and code < ord('A'):
            code = ord('A')+ (code-ord('Z'))
        text += chr(code)
    
    print(text)
    
cipher("abcxyzABCxyz 123")


