"""
NOTE:
    - install tabulate to run this program.
"""

import os # for clear screen
from userlog import * # to use functions of userlog file


def menu():
    print(menu_h)
    print(f"""\033[1;96m
            [1] Sign-in
            [2] Log-in
            [0] Exit\n\n\033[0;96m{55*("=")}""")

    # getting user's choice
    while True:
        ch = int(input("\tChoice: ")) 
        
        # input validation
        try:
            if 2 < ch or 0 > ch: # if ch is not in [0,1,2] it will direct the program to except funtion.
                raise ValueError
            break # this will break the loop once user entered number from 0-2.
        except:
            print("INVALID! Enter a Number From 0-2.")
            print() # this will print Choice: prompt again.

    ###
    if ch == 1: # if ch is equal to 1 the user will be directed to the sign-up page.
        os.system("cls")
        print(f"\n{menu_h}\n")
        sign_in()
        
    elif ch == 2: # if ch is equal to 2 the user will be directed to the log-in page.
        os.system("cls")
        print(f"\n{menu_h}\n")
        log_in()

    else:
        exit(0) # if ch is equal to 0, the program will automatically be terminated.


menu_h = (f"""\033[0;96m{55*'='}\n\033[0;31m
        ╔═╦╗───╔╗────╔╗──────────────╔╗─────── 
        ║║║║╔╦╗║╚╗╔╦╗╠╣╔═╦╗╔═╗╔══╗╔═╗║╚╗╔═╗╔╦╗ 
        ║║║║║║║║╔╣║╔╝║║║║║║║║║║║║║║╩╣║╔╣║╩╣║╔╝ 
        ╚╩═╝╚═╝╚═╝╚╝─╚╝╚╩═╝╚═╝╚╩╩╝╚═╝╚═╝╚═╝╚╝─    
\n\033[0;96m{55*'='}""") # log-in choices

menu()
