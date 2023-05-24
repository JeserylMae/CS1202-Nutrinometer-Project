"""
NOTE: 
    -   install tabulate to run this program.
    -   run the program in this main file
"""

import os # for clear screen
from design import * # this from design.py
from log import * # from log.py


# Asking user's input with input validation.
def input_CH(): 
    ch = int(input("\tChoice: ")) # prompting user to enter his/her choice.

    while 2 < ch or 0 > ch: # checking if ch is in the range zero-two.
        print("INVALID! Enter a Number From 0-2.") # if not this warning will be printed out.
        input_CH() # this will prompt user again to enter his/her choice.
        break # once the user entered a number between zero-two, with BREAK function the loop will end.
    return ch # returning ch 

# this is the possible locations that the user will be directed at, after he/she entered his/her choice.
def CH(ch): # defining a function.
    if ch == 1: # if user's input is 1.
        os.system("cls") # this will clear the console screen.
        print(f"\n{menu_h}\n") # printing menu_h from design.py
        sign_in() # for new user, this will direct user to the sign-in page. (the code for this is in log.py)
    elif ch == 2: # if user's input is 2.
        os.system("cls") # this will clear the console screen.
        print(f"\n{menu_h}\n")  # printing menu_h from design.py
        log_in() # this will direct user to the log-in page. (the code for this is in log.py)
    else: # if user's input is zero then the program will be terminated.
        exit(0) 

# This part prints the structured menu options. 
# this is the first part to be displayed once the program was run.
def menu(): # defining function menu().
    
    # printing header
    print(menu_h) # from design.py

    # Print options
    print(menu_options) # from design.py

    # Getting user's choice.
    ch = input_CH() # the returned value of ch from input_CH will be stored in ch variable.

    #directing user's to their chosen page.
    CH(ch) # calling the function CH with the value for ch.

menu() # printing function menu.
