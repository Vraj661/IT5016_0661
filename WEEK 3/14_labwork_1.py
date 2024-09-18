"""
Program which calculate BMI
Author = Vraj Prajapati
"""


def display_BMI(weight , height):
    BMI = weight / (height/100)**2 
    return BMI 

weight = int(input("Enter weight:-"))
height = int(input("Enter height:-"))
print(display_BMI(weight , height))
