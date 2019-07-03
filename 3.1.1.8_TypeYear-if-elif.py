year = int(input("Enter a year: "))
val = ""

if(year%4!=0):
    val ="It's a common year"
elif year%100!=0:
    val = "It's a leap year"
elif year%400!=0:
    val = "It's a common year"
else:
    val = "It's a leap year"
print(val)