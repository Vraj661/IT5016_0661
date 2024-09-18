'''
PROGRAM WHICH IS  USED TO GENERATE A RANDOM NUMBER BETWEEN 1 AND 100
NAME VRAJ PRAJAPATI
'''

import random
def user_number_guess(computer_num):
    prompt = "Enter Your Guess ( 1-99 ) : "
    num_guesses = 0
    number = 0
    
    while number!= computer_num:
        number = int(input(prompt))
        num_guesses += 1
        
        if number < computer_num:
            print("Too Low!")
        elif number > computer_num:
            print("Too High!")
        else:
            print(f"Correct ! number of guess: {num_guesses}")
    
def main():
    user_number_guess(random.randrange(1,100))
    
main()