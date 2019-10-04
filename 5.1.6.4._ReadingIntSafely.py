'''
Scenario

Your task is to write a function able to input integer values and to check if they are within a specified range.

The function should:

    accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
    if the user enters a string that is not an integer value, the function should emit the message Error: wrong input, and ask the user to input the value again;
    if the user enters a number which falls outside the specified range, the function should emit the message Error: the value is not within permitted range (min..max) and ask the user to input the value again;
    if the input value is valid, return it as a result.
'''

def readint(prompt, min, max):
    try:
        n = int(input(prompt))
        assert n >= min and n <= max
        return n
    except AssertionError:
        print("Error: the value is not within permitted range (-10..10)")
    except:
        print("Error: wrong input")

des = True

while des:
    v = readint("Enter a number from -10 to 10: ", -10, 10)
    if type(v) == int:
        des = False

print("The number is:", v)