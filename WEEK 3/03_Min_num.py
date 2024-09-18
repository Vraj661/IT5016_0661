"""
Program which find minimum number
Author = Vraj Prajapati
"""

def function1(n1,n2,n3):
    sum = n1+n2+n3
    Minimum = min(n1,n2,n3)
    return  sum-Minimum

n1 = int(input("Enter n1:-"))
n2 = int(input("Enter n2:-"))
n3 = int(input("Enter n3:-"))
print(function1(n1,n2,n3))
