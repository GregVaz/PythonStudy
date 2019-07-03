secretNumber = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
num = int(input("Ingresa tu numero "))
while secretNumber!=num:
    print("Estas equivocado no es el numero muggle")
    num = int(input("Ingresa otro numero"))
print("Correcto el numero es ",num)    