# program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd
# program terminates when zero is entered

oddNumbers = 0
evenNumbers = 0

# read the first number
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution
while number != 0:
    # check if the number is odd
    if number % 2 == 1:
        # increase the oddNumbers counter
        oddNumbers += 1
    else:
        # increase the evenNumbers counter
        evenNumbers += 1
    # read the next number
    number = int(input("Enter a number or type 0 to stop: "))

# print results
print("Odd numbers count:", oddNumbers)
print("Even numbers count:", evenNumbers)