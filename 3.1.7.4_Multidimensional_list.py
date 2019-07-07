# Multidimensional nature of lists: advanced applications
# Let's go deeper into the multidimensional nature of lists. To find any element of a two-dimensional list, you have to use two coordinates:

# a vertical one (row number)
# and a horizontal one (column number).

'''
Imagine that you develop a piece of software for an automatic weather station. 
The device records the air temperature on an hourly basis and does it throughout the month. 
This gives you a total of 24 × 31 = 744 values. Let's try to design a list capable of storing all these results.
'''

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)


# Now find the highest temperature during the whole month

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

# Now count the days when the temperature at noon was at least 20 ℃:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, "days were hot.")


#Three-dimensional arrays

# Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor. 
# For this, you need an array which can collect and process information on the occupied/free rooms.

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# Check if there are any vacancies on the 15th floor of the third building:

vacancy = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1
