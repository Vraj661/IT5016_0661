"""
Program which get cost
Author = Vraj Prajapati
"""

def get_price(a, b):
    child = 20
    adult = 25
    group = 21
    group_rate =0.7

    cost = (a * child + b * adult)

    if a + b > group:
        cost = cost * group_rate
    return cost

def main():
    Num_a = int(input("Enter the number of a:-"))
    Num_b = int(input("Enter the number of b:-"))
    cost = get_price(Num_a,Num_b)
    print("The cost of your tickets is  : $" + str(cost))
main()