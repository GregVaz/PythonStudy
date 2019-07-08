'''
 Body Mass Index (BMI).

    BMI = weight/height

As you can see, the formula gets two values:

weight (originally in kilograms)
height (originally in meters)
'''

''' # process
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

print(bmi(175, 1.65))

# We can write two simple functions to convert imperial units to metric ones
def lbtokg(lb):
    return lb * 0.45359237

print(lbtokg(1))

def ftintom(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

print(ftintom(6))
'''

#  what is the BMI of a person 5'7" tall and weighing 176 lbs?
# Result 
def ftintom(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lbstokg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2


print(bmi(weight = lbstokg(176), height = ftintom(5, 7)))