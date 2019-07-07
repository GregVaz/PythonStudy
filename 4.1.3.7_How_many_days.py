'''
Scenario
Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days
 for the given month/year pair (while only February is sensitive to the year value, your function should be universal).
'''

def isYearLeap(year):
    if year%4!=0:
        return False # return False if the year is a leap year 
    elif year%100!=0:
        return True # return True if the year is a common year
    elif year%400!=0:
        return False
    else:
        return True

def daysInMonth(year, month):
    if isYearLeap(year):
        if month == 2:
            return 29
        else:
            return days(month)
    else:
        if month == 2:
            return 28
        else:
            return days(month)
        
def days(month):
    if month < 7:
        if month%2 != 0:
            return 31
        else:
            return 30
    elif month < 13:
        if month%2 != 0:
            return 30
        else:
            return 31


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")