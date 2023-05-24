"""
NOTE: 
    -   install tabulate to run this program.
"""

import os # for clear screen
from design import *
from log import *


def input_CH():
    ch = int(input("\tChoice: "))

    while 2 < ch or 0 > ch: 
        print("INVALID! Enter a Number From 0-2.")
        input_CH()
        break
    return ch

def CH(ch):
    if ch == 1:
        os.system("cls")
        print(f"\n{menu_h}\n")
        sign_in()
    elif ch == 2:
        os.system("cls")
        print(f"\n{menu_h}\n")
        log_in()
    else:
        exit(0)

def menu():
    # printing header
    print(menu_h)

    # Print options
    print(menu_options)

    # choice = input(ch)
    ch = input_CH()

    #directing user's to their chosen page.
    CH(ch)



menu()
