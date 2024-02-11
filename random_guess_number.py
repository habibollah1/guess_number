import random 
import string
import os

os.system('cls')

ai_random = random.randrange(1,10)
def game_again():    
        
    while True:            
        user_input = input('are you game again? (y/n): ')
        if user_input in ['y', 'n']:
            if user_input == 'y':
                random_number_guess()
            else:
                break    
        else:
            print('invalid input. you should enter (y or n): ')
    print('thank you for playing')


def random_number_guess():
    
    while True:
        user_input = (input('guess your choice of number (1 until 10):  '))
        
        if user_input.isdigit():
            a = int(user_input)
            if not 0 < a <= 10:
                print('invalid input. you should select of number (1 until 10) ')
            elif a == ai_random:
                print('your guess is correct')
                break
            else:
                print('your guess is wrong')
        
        else:
            print('you should enter number (1 until 10)')
                 
    game_again()    
            
            
random_number_guess()