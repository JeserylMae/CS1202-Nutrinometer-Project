"""
LOG-IN PAGE CODE

"""

import os

def log_main():
    print(45*("=") + "\n\t\tNUTRINOMETER\n" + 45*("=")) # header
    print(f"""
    \t[1] Sign-up
    \t[2] Log-in
    \t[0] Exit\n\n{45*("=")}""") # log-in choices
    
    while True:
        ch = int(input("Choice: ")) # getting user's choice
        
        # input validation
        try:
            if 2 < ch or 0 > ch: # if ch is not in [0,1,2] it will direct the program to except funtion.
                raise ValueError
            break # this will break the loop once user entered number from 0-2.
        except:
            print("INVALID! Enter a Number From 0-2.")
            print() # this will print Choice: prompt again.
    
    if ch == 1: # if ch is equal to 1 the user will be directed to the sign-up page.
        sign_up()
    elif ch == 2: # if ch is equal to 2 the user will be directed to the log-in page.
        log_in()
    else:
        exit(0) # if ch is equal to 0, the program will automatically be terminated.

# class User
class User:
    
    # Creating txt files for each new user.
    def user_info(self):
        with open("user_list.txt", "a") as file: # open a file called user_list.txt to append infos in it.
            file.write(f"{self.un} {self.pw}\n") # putting self.un and self.pw inside user_list.txt.
        file.close() # to close the file.

        # Create txt file with user's name as file name.
        record = open(f"{self.un}.txt", "a") 
        record.close()
 
    # main function
    def main(self):
        os.system('cls')
        print(60*("=") + "\n\n\t\t N U T R I N O M E T E R\n\n" + 60*("=")) # header
        print(f"\n\tWelcome {self.un}!\n")

        print(f"""\t
        W E E K L Y  R E C O R D S 
        {43*("-")}""")


# function sign-up
def sign_up():
    os.system('cls') # clear screen
    print(45*("=") + "\n\t\tNUTRINOMETER\n" + 45*("=")) # header
    
    # putting datas inside user_list.txt into list
    file = open("user_list.txt", "r")
    user_list = file.read().split() 
    file.close()

    user = User() # Directing user to User's attributes.

    while True:
        # Promt user to enter username.
        user.un = str(input("\tUsername: "))  # putting username to class User().
        
        # verifying username
        if user.un in user_list: # if user has already been made the program will promt again.
            print("\tUsername Already Exist.")
            print()
        else:
            break

    # Prompt user to enter password
    while True:
        user.pw = str(input("\tPassword: ")) # putting password into class User().
        v_password = str(input("\tRe-enter Password: ")) # promt user to re-enter password.

        # Verifying Password
        try:
            if v_password != user.pw: # checking if re-entered password is the same to the first one.
                raise ValueError # if not the program will be directed to the except Funtion.
            break
        except:
            print("\tPassword do not match!") # error message.
            print() # will prompt the user again to enter password.

    print(45*("="))
    user.user_info() # to put user.un and user.pw inside user_list.txt
    user.main() # the user will be directed to the Nutrinometer page.


# Function log-in
def log_in():
    os.system('cls')
    print(45*("=") + "\n\t\tNUTRINOMETER\n" + 45*("=")) # header

    # putting datas inside user_list.txt into list
    file = open("user_list.txt", "r")
    user_list = file.read().split() 
    file.close()

    user = User() # Directing user to User's attributes.

    while True:
        # Promt user to enter username.
        user.un = str(input("\tUsername: "))  # putting username to class User().
        
        # verifying username
        if user.un in user_list: # checking if the username exits.
            break # if it does the program will continue.
        else:
            print("\tUsername Doesn't Exist.") # if the username doesn't exist the program will prompt again.
            print()
    
    # Prompt user to enter password
    while True:
        user.pw = str(input("\tPassword: ")) # putting password into class User().

        # Verifying Password
        try:
            if user.pw not in user_list: # checking if password is correct.
                raise ValueError
            break
        except:
            print("\tIncorrect Password!!") # error message.
            print() # will prompt the user again to enter password.

    print(45*("="))
    user.main()

log_main()

