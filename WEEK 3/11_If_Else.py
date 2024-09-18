"""
Program which if else condition
Author = Vraj Prajapati
"""

def what_to_wear(temperature):
    if temperature > 25:
        print("Wear shorts.")
    else:
        print("Not hot today!")
        print("Enjoy yourself.")
    print("Wear long pants.")
def main():
    what_to_wear(10)
    print()
    what_to_wear(40)
main()

