'''
PROGRAM WHICH IS FOR LOOP
NAME VRAJ PRAJAPATI
'''
def Show_Output():
    total = 0
    for number in range(9, 20):
        if number % 2 == 0 or number % 3 == 0:
            total += number
            print(total)
        
def main():
    Show_Output()
main()