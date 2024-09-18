"""
Program which convert temp.
Author = Vraj Prajapati
"""

def celsius_to_f(celsius):
    fahrenheit = celsius* 9/5 + 32
    return fahrenheit

celsius = 15
print(1,"celsius",celsius,"= fahrenheit",celsius_to_f(celsius))

celsius = 35
print(2,"celsius",celsius,"= fahrenheit",celsius_to_f(celsius))

celsius = 65
print(3,"celsius",celsius,"= fahrenheit",celsius_to_f(celsius))