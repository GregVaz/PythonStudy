import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)
for i in range(1,5):
    print('Mississippi')
    time.sleep(1)

# More examples

pow = 1
for exp in range(16):
    print("2 to the power of", exp, "is", pow)
    pow *= 2

for i in range(3):
    print(i, end=" ") # outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ") # outputs: 6, 4, 2