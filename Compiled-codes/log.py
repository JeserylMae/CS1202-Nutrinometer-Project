
import os
from tabulate import tabulate
from design import *
from calc import *

# create a text file named user_list2.txt
file = open("user_list2.txt", "a")
file.close()

user_list = [] 
# creating list of active usernames.
user_list = []
with open("user_list2.txt", "r") as file:
    user_list = file.read().split()

class User():
    # Declaring variables inside class User.
    def __init__(self, un, pw):
        self.un = un
        self.pw = pw

    # open/create txt file w/ user's name as filename.
    def user_account(self):
        account = open(f"{self.un}.txt", "a") 
        account.close()

    def user_kcal(self):
        with open(f"{self.un}.txt", "r") as file:
            pass

class New_user(User):
    # inheriting class User's variables
    def __init__(self, un, pw): 
        super().__init__(un, pw)

    # this function will create a text file for the New User.
    def user_info(self):
        # append the new user to the list of users in a txt file. 
        with open("user_list2.txt", "a") as file: # open a file called user_list.txt to append infos in it.
            file.write(f"{self.un} {self.pw}\n") # saving self.un and self.pw inside user_list.txt.
    

class Homepage(User):
    def __init__(self, un, pw=None):
         super().__init__(un, pw)

    def table_r(self, n=int):
        print(homepage_h)

        with open(f"{self.un}.txt", "r") as file:
            lines = file.readlines() # lines is a list
            lines = sorted(lines)

        # Defining list line and list y.
        # list line will store the values stored in lines separated by '|'
        line =  [['DATE', 'TYPE OF MEAL', 'FOOD', 'AMOUNT OF CALORIES', 'STATUS']] 
        # list y will stored tabulated values of line.
        y = [] 

        if n == 1:
            print(homepage_m)
            # Since the targeted number of rows to be presented in Recent Records is 
            # a max of 7 rows we need to set range of rows.
            if len(lines) <= 3: # here if length of lines is below 7, the range will up to the length of lines.
                m = -(len(lines))
            else:
                m = -4 # however if length of lines is greater than 7, the range = 7.
        else:
            print(view_page)
            m = -(len(lines))

        #adding values to list line.
        if len(lines) != 0:
            for i in range(m, 0):
                line.append(lines[i].rstrip('\n').split(" | "))
            t = tabulate(line, headers="firstrow", tablefmt="fancy_grid", stralign="center", numalign="center", missingval=" ", maxcolwidths=15)
        # if the txt file is empty or there's no record yet. 
        else:
            line.append([' ', ' ', 'No Record Yet', ' ', ' '])
            t = (tabulate(line, headers="firstrow", tablefmt="fancy_grid", stralign="center", missingval=" "))

        y.append(t)
        q = []
        q.extend(y[0].split("\n")) # this will store the tabulated values separated line by line.

        # to print tabulated datas.
        for i in range (0, len(q)):
            print(f"{Colors().cyan}\t\t{q[i]}")


        # printing user choices in red/pink color.
        if n == 1:
            print(f"{Colors().red} \n\t\t[1] Add Record\t\t\t[2] View All Records\t\t\t[0] Exit")
        else:
            print(f"{Colors().red} \n\t\t[1] Add Record {tab} [0] Exit")

        print(f"{Colors().cyan} \n{115*'▀'} \n")

        # Directing the program to Record_ch.menu()
        Record_ch.menu_c(self.un)


class NewUser_data(New_user):
    def __init__(self, un, pw):
        super().__init__(un, pw)

    def user_personal_info(self):
        print(homepage_h)

        weight = float(input(f"\n\t\t{Colors().cyan}Weight [kg]:{Colors().red}\t"))
        height = float(input(f"\t\t{Colors().cyan}Height [cm]:{Colors().red}\t"))
        age = int(input(f"\t\t{Colors().cyan}Age:\t {Colors().red}"))
        sex = int(input(f"\t\t{Colors().cyan}Sex [0-Male 1-Female]:\t {Colors().red}"))

        print(f"\n\t\t{Colors().cyan}[1-Sendentary, 2-Lightly Active, 3-Moderately Active, 4-Very Active]")
        actLevel = str(input(f"\t\t{Colors().cyan}Activity Level:\t {Colors().red}"))
        
        # calculating bmr based on user's sex.
        bmr = calc_bmr(weight, height, sex, age)
        calories = calc_daily_calories(actLevel, bmr)
        
        # create txt file which will store persinal infos of user.
        with open(f"{self.un}-personal-info.txt", "a") as file:
            file.write(f"""Weight:\t{weight}
            \rHeight:\t{height}
            \rAge:\t{age}
            \rSex:\t{sex}
            \rActivity Level:\t{actLevel}
            \rBmr:\t{bmr}
            \rRequired Calorie:\t{calories}""")


# commands for user's choices wheter to add record, view, or exit.
class Record_ch(User):
    def __init__(self, un, pw=None):
        super().__init__(un, pw)

    def home(self):
        super().home()

    # for menu choices   
    def menu_c(self):
        ch = int(input(f"{Colors().cyan}\t\tChoice:\t"))
        print("\n")

        # menu choices:
        if ch == 1:
            os.system("cls")
            Add(self).add_record()
        elif ch == 2:
            os.system("cls")
            View(self).view_record()
        else:
            os.system("cls")
            exit(0)

class Add(NewUser_data):
    def __init__(self, un, pw=None):
        super().__init__(un, pw)
    
    def user_personal_info(self):
        return super().user_personal_info()

    def add_record(self):
        os.system("cls")
        print(homepage_h)

        print("\n\t\t[Month Day, Year]")
        i_date = str(input("\t\tDate:\t"))

        print("\n\t\t[Breakfast, Brunch, Lunch, Snack, Dinner]")
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

        total_cal = food_input(self.un, rice, meat, veggies, seafood, i_date, i_mealType)

        # Getting Required Calories.
        with open(f"{self.un}-personal-info.txt", "r") as file:
            for lines in file:
                lines = lines.split()
        req_cal = float(lines[2])

        # Comparing Consumed calories (total_cal) and required calories (req_kcal).
        analyze_kcal(self.un, total_cal, req_cal)

        print(f"\n\n{divider_line}\n")

        # Asking if user wants to add another record or not.
        ch = int(input("\t\t[0] Back\t\t[1] Add Record\t\tChoice: "))
        record_choices(ch, self.un)
 

class View(Record_ch):
    def __init__(self, un, pw=None):
        super().__init__(un, pw)
    
    def view_record(self):
        os.system("cls")
        Homepage(self.un).table_r(n=0)

def record_choices(ch, user):
    if ch == 1:
        os.system("cls")
        Add(un=user).add_record()
    else: 
        os.system("cls")
        Homepage(un=user).table_r(n=1)

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
    User(un, pw).user_account()

    # directing user to home page.
    os.system("cls")
    NewUser_data(un, pw).user_personal_info()
    os.system("cls")
    Homepage(un, pw).table_r(n=1)


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
    Homepage(un, pw).table_r(n=1)
