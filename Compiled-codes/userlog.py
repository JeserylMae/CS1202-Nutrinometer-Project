
"""
LOG-IN 
"""

import os
from tabulate import tabulate

# title 
header = (f"""\033[0;96m
{115*'▀'}\n \033[0;31m

        ███╗░░██╗██╗░░░██╗████████╗██████╗░██╗███╗░░██╗░█████╗░███╗░░░███╗███████╗████████╗███████╗██████╗░ 
        ████╗░██║██║░░░██║╚══██╔══╝██╔══██╗██║████╗░██║██╔══██╗████╗░████║██╔════╝╚══██╔══╝██╔════╝██╔══██╗ 
        ██╔██╗██║██║░░░██║░░░██║░░░██████╔╝██║██╔██╗██║██║░░██║██╔████╔██║█████╗░░░░░██║░░░█████╗░░██████╔╝ 
        ██║╚████║██║░░░██║░░░██║░░░██╔══██╗██║██║╚████║██║░░██║██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗ 
        ██║░╚███║╚██████╔╝░░░██║░░░██║░░██║██║██║░╚███║╚█████╔╝██║░╚═╝░██║███████╗░░░██║░░░███████╗██║░░██║ 
        ╚═╝░░╚══╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝ 
        
\033[0;96m\n{115*'▀'} """)

# create a text file named user_list2.txt
file = open("user_list2.txt", "a")
file.close()

# creating list of active usernames.
user_list = []
with open("user_list2.txt", "r") as file:
    user_list = file.read().split()

class User:
    def __init__(self, un, pw):
        self.un = un
        self.pw = pw

    # open/create txt file w/ user's name as filename.
    def user_account(self):
        account = open(f"{self.un}.txt", "a") 
        account.close()

    def home(self):
        print(header)
        print("\n\033[0;31m")
        print(f"\t\tWelcome {self.un}!!\n".upper())
        print("\t\tRecent Records...")

        with open(f"{self.un}.txt", "r") as file:
            lines = file.readlines() # lines is a list
           
        line = [['DATE', 'TYPE OF MEAL', 'FOOD', 'AMOUNT OF CALORIES', 'STATUS']] # declaring a list named line.
        
        y = []

        if len(lines) <= 7:
            n = -(len(lines))
        else:
            n = -7

        #adding values to list line.
        if len(lines) != 0:
            for i in range(n, 0):
                line.append(lines[i].rstrip('\n').split(" | "))
            t = tabulate(line, headers="firstrow", tablefmt="fancy_grid", stralign="center", numalign="center", missingval=" ", maxcolwidths=15)
        
        # if the txt file is empty.
        else:
            line.append([' ', ' ', 'No Record Yet', ' ', ' '])
            t = (tabulate(line, headers="firstrow", tablefmt="fancy_grid", stralign="center", missingval=" "))

        y.append(t)
        q = []
        q.extend(y[0].split("\n"))

        for i in range (0, len(q)):
            print(f"\033[0;96m\t\t{q[i]}")
        print("\033[0;31m\n\t\t[1] Add Record\t\t\t[2] View All Records\t\t\t[0] Exit")
        print(f"\033[0;96m\n{115*'▀'} \n")

        Functions.menu_c(self.un)

class New_user(User):
    def __init__(self, un, pw):
        super().__init__(un, pw)

    def user_account(self):
        super().user_account()
    
    def user_info(self):
        # append the new user to the list of users in a txt file. 
        with open("user_list2.txt", "a") as file: # open a file called user_list.txt to append infos in it.
            file.write(f"{self.un} {self.pw}\n") # saving self.un and self.pw inside user_list.txt.

    def user_personal_info(self):
        print(header)

        u_weight = float(input("\n\t\t\033[0;96mWeight [kg]:\033[0;31m\t"))
        u_height = float(input("\t\t\033[0;96mHeight [cm]:\033[0;31m\t"))
        u_age = int(input("\t\t\033[0;96mAge:\033[0;31m\t"))
        u_sex = int(input("\t\t\033[0;96mSex [0-Male 1-Female]:\033[0;31m\t"))

        print("\n\t\t\033[0;96m[1-Sendentary, 2-Lightly Active, 3-Moderately Active, 4-Very Active]")
        u_actLevel = str(input("\t\t\033[0;96mActivity Level:\033[0;31m\t"))
        # create txt file which will store persinal infos of user.
        with open(f"{self.un}-personal-info.txt", "a") as file:
            file.write(f"Weight:\t{u_weight}\nHeight:\t{u_height}\nAge:\t{u_age}\nSex:\t{u_sex}\nActivity Level:\t{u_actLevel}\n")

        # determining BMR
        if u_sex == 0:
            bmr = 66.5 + (13.8 * u_weight) + (5 * u_height) - (6.75 * u_age)
        else:
            bmr = 655 + (9.6 * u_weight) + (1.9 * u_height) - (4.7 * u_age)
        print(bmr)

        # Calculating Calaries
        if u_actLevel == "sedentary":
            calories = bmr * 1.2
        elif u_actLevel == "lightly active":
            calories = bmr * 1.375
        elif u_actLevel == "moderately active":
            calories = bmr * 1.55
        else:
            calories = bmr * 1.725

class Functions(User):
    def __init__(self, un, pw=None):
        super().__init__(un, pw)

    def home(self):
        super().home()

    # for menu choices   
    def menu_c(self):
        ch = int(input("\033[0;31m\t\tChoice:\t"))
        print("\n")

        # menu choices:
        if ch == 1:
            os.system("cls")
            Functions(self).add_record()
        elif ch == 2:
            os.system("cls")
            Functions(self).view_record()
        else:
            os.system("cls")
            exit(0)
        
    def add_record(self):
        os.system("cls")
        print(header)

        print("\n\t\t[Month Day, Year]")
        i_date = str(input("\t\tDate:\t"))

        print("\n\t\t[Breakfast, Bruch, Lunch, Snack, Dinner]")
        i_mealType = str(input("\t\tType of Meal:\t"))

        print("\n\t\tFood Portion [if none input 0]")

        food_portion: list = ['rice', 'meat', 'veggies', 'seafood']
        i_portion: list = []
        for i in range (4):
            i_portion = input(f"\t\tPortion of {food_portion[i]}:\t")
            i += 1
            food_portion.extend(i_portion)

        rice = float(food_portion[4])
        meat = float(food_portion[5])
        veggies = float(food_portion[6])
        seafood = float(food_portion[7])

        total_cal = (rice + meat + veggies + seafood)*280
        total_cal = total_cal / 4
        i_food = ""

        if rice != 0:
            i_food += "Rice + "
        if meat != 0:
            i_food += "Meat + "
        if veggies != 0:
            i_food += "Vegetables + "
        if seafood != 0:
            i_food += "Seafood"

        with open(f"{self.un}.txt", "a") as file:
            file.write(f"{i_date} | {i_mealType} | {i_food} | calories | status\n")
        
    def view_record(self):
        os.system("cls")
        print("view")

def sign_in():
    # Promt user to enter username.
    while True:
        un = str(input("\tUsername:\t"))  # putting username to class User().
        
        # verifying username
        if un in user_list: # if user has already been made the program will promt again.
            print("\tUsername Already Exist.")
            print()
        else:
            break

    # Prompt user to enter password
    while True:
        pw = str(input("\tPassword:\t")) # putting password into class User().
        v_password = str(input("\tRe-enter Password:\t")) # promt user to re-enter password.

        # Verifying Password
        try:
            if v_password != pw: # checking if re-entered password is the same to the first one.
                raise ValueError # if not the program will be directed to the except Funtion.
            break
        except:
            print("\tPassword do not match!") # error message.
            print() # will prompt the user again to enter password.

    # Directing user's input to class New_user
    New_user(un, pw).user_info()
    New_user(un, pw).user_account()

    # directing user to home page.
    os.system("cls")
    New_user(un, pw).user_personal_info()
    os.system("cls")
    User(un, pw).home()


def log_in():
    # Promt user to enter username.
    while True:
        un = str(input("\tUsername:\t")) 
        
        # verifying username
        if un in user_list: # checking if the username exits.
            break # if it does the program will continue.
        else:
            print("\tUsername Doesn't Exist.") # if the username doesn't exist the program will prompt again.
            print()
    
    # Prompt user to enter password
    while True:
        pw = str(input("\tPassword:\t")) # putting password into class User().

        # Verifying Password
        try:
            if pw not in user_list: # checking if password is correct.
                raise ValueError
            break
        except:
            print("\tIncorrect Password!!") # error message.
            print() # will prompt the user again to enter password.

    # directing User's input to class User
    User(un, pw).user_account()

    # directing user to home page.
    os.system("cls")
    User(un, pw).home()

