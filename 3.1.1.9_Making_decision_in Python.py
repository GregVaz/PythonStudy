# Making decisions in Python

#Example 1
# read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# choose the larger number
if number1 > number2:
    largerNumber = number1
else:
    largerNumber = number2

# print the result
print("The larger number is:", largerNumber)


# My version

# Enter the quantity for numbers
quantity = int(input("Cantidad de numeros a ingresar? : "))
list = []

for i in range(quantity):
    list.append(int(input("Ingresa un numero: ")))

print("El numero mayor es: ",max(list))