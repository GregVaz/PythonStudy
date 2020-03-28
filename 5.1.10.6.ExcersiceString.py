def display(num):
    text = []
    if(num.isdigit()):
        print("Ingresa unicamente numeros")
    for i in num:
        # print(printNumbers(i))
        dis = printNumbers(i).split("\n")
        for e in range(len(dis)):
            if(len(text)<5):
                text.append(dis[e])
            else:
                text[e] = text[e] + " " + dis[e]
    for i in text:
        print(i)

def printNumbers(arg):
    dictionary = {
        "1": "#\n#\n#\n#\n#",
        "2": "###\n  #\n###\n#  \n###",
        "3": "###\n  #\n###\n  #\n###",
        "4": "# #\n# #\n###\n  #\n  #",
        "5": "###\n#  \n###\n  #\n###",
        "6": "###\n#  \n###\n# #\n###",
        "7": "###\n  #\n  #\n  #\n  #",
        "8": "###\n# #\n###\n# #\n###",
        "9": "###\n# #\n###\n  #\n###",
        "0": "###\n# #\n# #\n# #\n###"
    }
    return dictionary[arg]

try:
    display(input("Ingresa un numero: "))
except:
    print("Error: ingresa unicamente numeros") 