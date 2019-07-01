income = float(input("Enter the annual income: "))

if(income<85528):
    tax = (income*0.18)-556.02
else:
    tax = 14839.02*1.32

tax = round(tax, 0)
if(tax<0): tax = 0

print("The tax is:", tax, "thalers")