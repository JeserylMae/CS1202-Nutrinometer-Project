
"""
    LOG-IN PAGE
"""

import os # for clearing screen.
from tabulate import tabulate # this is not a built-in module, it is used to create a tabular presentation of datas.
from design import * # in order to use the defined functions from design.py, it is necessary to import it.
from calc import * # in order to use the defined functions from calc.py, it is necessary to import it.

# create a text file named user_list2.txt, this will store all the username and password of all user's 
# who will sign-in to the program.
file = open("user_list2.txt", "a") # as soon as the program was run, a txt file named user_list2 will be created.
file.close() # closing the file.


# creating list of active usernames.
user_list = []
# opening the file in read mode, since we're only going to read its content and not write to it.
with open("user_list2.txt", "r") as file: 
    user_list = file.read().split() # puttting the contents of the txt file into the list user_list.
    # .read() function will read through the txt file's contents.
    # .split will separate the contents of the txt file whenever it encounters white spaces.
    
# this is the main class.
class User():
    # Declaring variables inside class User.
    def __init__(self, un, pw):
        self.un = un
        self.pw = pw

    # open/create txt file w/ user's name as filename.
    def user_account(self): # defining a function user_account() with self as its parameter.
        account = open(f"{self.un}.txt", "a") # once the user signed-in or logged-in 
        # this txt file will be automatically opened, whether it exist or not.
        account.close()

# Creating class for new users.
class New_user(User): # this inherits all the attributes and methods the class User have.
    
    # inheriting class User's attributes.
    def __init__(self, un, pw): 
        super().__init__(un, pw)

    # this function will create a text file for the New User.
    def user_info(self):
        # append the new user to the list of users in a txt file. 
        with open("user_list2.txt", "a") as file: # open a file called user_list.txt to append infos in it.
            file.write(f"{self.un} {self.pw}\n") # saving self.un and self.pw inside user_list.txt.
    
# Creating class for the home page.
class Homepage(User): # this inherits all the attributes and methods the class User have.
    
    # inheriting class User's attributes.
    def __init__(self, un, pw=None): # since we don't need the user's password in this class, 
        # we set it to None, so it wouldn't ask for value of pw once it's called.
         super().__init__(un, pw) 

    # this function creates the table presented in the homepage and view record page.
    def table_r(self, n=int): 
        print(homepage_h) # printing homepage header, this is from design.py.

        with open(f"{self.un}.txt", "r") as file: # opening txt.file with User's username as filename.
            lines = file.readlines() # lines is a list which will store all the contents of the txt file.
            lines = sorted(lines) # arranging all the conents chrnologically.

        # Defining list line and list y.
        # list line will store the values stored in lines separated by '|'
        line =  [['DATE', 'TYPE OF MEAL', 'FOOD', 'AMOUNT OF CALORIES', 'STATUS']] 
        # list y will stored tabulated values of line.
        y = [] 

        # n is a code here which says whether it is the homepage or view record page.
        if n == 1: # if n = 1 then it is the homepage.
            print(homepage_m) # printing homepage header from designs.py
            # Since the targeted number of rows to be presented in Recent Records is 
            # a max of 4 rows we need to set range of rows.
            if len(lines) <= 3: # here if length of lines is below 3, the range will be equal to the length of lines.
                m = -(len(lines)) # m is negative because we want to read the contents of the list from the end.
            else: 
                m = -4 # however if length of lines is greater than 3, the range = 4.
        else: # this is for the View all Record page.
            print(view_page) # this is the header for view page, from design.py
            m = -(len(lines)) # since we want to view all records, then m should be equal to the number of lines of the list.

        # adding values to list line.
        if len(lines) != 0: # the is for the old users.
            for i in range(m, 0):
                line.append(lines[i].rstrip('\n').split(" | ")) # adding contents of the txt file to list line.
                # .rstrip() removes all '\n' character in the file.
                # .split() will separate the values whenever it encounters a '|' character.
            # creating table of records using tabulate function/module.
            t = tabulate(line, headers="firstrow", tablefmt="fancy_grid", stralign="center", numalign="center", missingval=" ", maxcolwidths=15)
        # if the txt file is empty or there's no record yet. 
        else: # this is for New users, since their txt file has no record yet.
            line.append([' ', ' ', 'No Record Yet', ' ', ' ']) # this will be the contents of the table for new users.
            # creating table of records using tabulate function/module.
            t = (tabulate(line, headers="firstrow", tablefmt="fancy_grid", stralign="center", missingval=" "))

        # adding tables to list y.
        y.append(t)
        q = [] # this will store the contents of the txt file with the table design.
        q.extend(y[0].split("\n")) # this will store the tabulated values separated line by line.

        # to print tabulated datas.
        for i in range (0, len(q)):
            print(f"{Colors().cyan}\t\t{q[i]}") # Colors().cyan changes the color of text to cyan.

        # printing user choices in red/pink color.
        if n == 1: # printing footer for the homepage
            print(f"{Colors().red} \n\t\t[1] Add Record\t\t\t[2] View All Records\t\t\t[0] Exit") # Colors().red changes the text color to red.
        else: # printing footer for the view all record page.
            print(f"{Colors().red} \n\t\t[1] Add Record {tab} [0] Exit") # Colors().red changes the text color to red.

        print(f"{Colors().cyan} \n{115*'▀'} \n") # printing a color cyan line. 

        # Directing the program to Record_ch.menu()
        Record_ch.menu_c(self.un)

# Class for the data of new users.
class NewUser_data(New_user): # inheriting the attributes and methods of class New_user.
    
    # explicitly inheriting the attributes of New user.
    def __init__(self, un, pw):
        super().__init__(un, pw)

    # this function will ask the user about their personal datas.
    def user_personal_info(self):
        print(homepage_h) # printing header, this is from design.py

        # prompting user to enter ther corresponding datas.
        weight = float(input(f"\n\t\t{Colors().cyan}Weight [kg]:{Colors().red}\t"))
        height = float(input(f"\t\t{Colors().cyan}Height [cm]:{Colors().red}\t"))
        age = int(input(f"\t\t{Colors().cyan}Age:\t {Colors().red}"))
        sex = int(input(f"\t\t{Colors().cyan}Sex [0-Male 1-Female]:\t {Colors().red}"))

        print(f"\n\t\t{Colors().cyan}[1-Sendentary, 2-Lightly Active, 3-Moderately Active, 4-Very Active]")
        actLevel = str(input(f"\t\t{Colors().cyan}Activity Level:\t {Colors().red}"))
        
        # calculating bmr based on user's sex.
        # Directing user entered value of weight, height, sex, age to function calc_bmr(). 
        bmr = calc_bmr(weight, height, sex, age) # calc_bmr is in the calc.py. the returned value from this function will be stored in bmr variable.
        # calculating the calories using the function calc_daily_calories().
        calories = calc_daily_calories(actLevel, bmr) # the returned value from this function will be stored in the variable calories.
        
        # adding user's personal datas inside the user's txt file.
        with open(f"{self.un}-personal-info.txt", "a") as file: # it is in append mode since we want to add/write data into the txt file.
             # adding weight, height, age, sex, activity level, Bmr, and required calories inside the txt file.
            file.write(f"""Weight:\t{weight}
            \rHeight:\t{height}
            \rAge:\t{age}
            \rSex:\t{sex}
            \rActivity Level:\t{actLevel}
            \rBmr:\t{bmr}
            \rRequired Calorie:\t{calories}""")


# commands for user's choices wheter to add record, view, or exit.
class Record_ch(User): # inheriting attributes and methods of class User.
    
    # explicitly inheriting attributes of User.
    def __init__(self, un, pw=None): # setting pw to None, so it won't ask for a value once it's called.
        super().__init__(un, pw) 

    # explicitly inheriting method home() from class User.
    def home(self):
        super().home()

    # for menu choices.
    def menu_c(self):
        ch = int(input(f"{Colors().cyan}\t\tChoice:\t")) # prompting user to enter his/her choice.
        print("\n")

        # menu choices:
        if ch == 1: # if choice = 1, the program will be directed to add record page.
            os.system("cls") # clearing screen.
            Add(self).add_record() # calling add_record funtion to print out the add record page.
        elif ch == 2: # if choice = 2, the program will be directed to View All Records Page.
            os.system("cls") # clearing screen.
            View(self).view_record() # calling view_record function to print out View Record Page.
        else: # if choice = 0, the program will be terminated.
            os.system("cls") # for clearing screen.
            exit(0) # this function terminates the program, with exit code zero.

# This program will prompt the user to add the details for their daily food intake.
class Add(NewUser_data): # inheriting the class NewUser_data.
    # explicitly inheriting all attributes in NewUser_data.
    def __init__(self, un, pw=None): # setting pw to none, since we only need to get the un(username).
        super().__init__(un, pw)
    
    # explicitly inheriting the method user_personal_info().
    def user_personal_info(self):
        return super().user_personal_info()

    # this function is for the add_record page.
    def add_record(self):
        os.system("cls") # clearing screen.
        print(homepage_h) # printing header, this is from design.py

        print("\n\t\t[Month Day, Year]") # Guiding the user of the date format.
        i_date = str(input("\t\tDate:\t")) # prompting user to enter Date.

        print("\n\t\t[Breakfast, Brunch, Lunch, Snack, Dinner]") # Printing choices fo the type of meal.
        i_mealType = str(input("\t\tType of Meal:\t")) # promting user to enter the type of meal.

        print("\n\t\tFood Portion [if none input 0]")

        food_portion: list = ['rice', 'meat', 'veggies', 'seafood']
        i_portion: list = [] # this will store user's input.
        for i in range (4): # this will loop through the list food_portion.
            i_portion = input(f"\t\tPortion of {food_portion[i]}:\t") # this will prompt user to enter food portion they had taken.
            i += 1
            food_portion.extend(i_portion) # adding user input to food_portion list.

        # assigning the values of food_portion to their respective variable while converting their type to float.
        rice = float(food_portion[4]) 
        meat = float(food_portion[5])
        veggies = float(food_portion[6])
        seafood = float(food_portion[7])

        # calculating the total_cal using function food_input from calc.py.
        # the return value of function food_input will be stored inside total_cal variable.
        total_cal = food_input(self.un, rice, meat, veggies, seafood, i_date, i_mealType)

        # Getting Required Calories.
        with open(f"{self.un}-personal-info.txt", "r") as file: # opening txt file in read mode.
            for lines in file:
                lines = lines.split() # adding contents of the txt file to list lines, 
                # the contents will be separated by dot split() word-by-word before storing it to list lines.
        req_cal = float(lines[2]) # storing value of lines[2] to req_cal.

        # Comparing Consumed calories (total_cal) and required calories (req_kcal).
        analyze_kcal(self.un, total_cal, req_cal) # this function is from calc.py

        print(f"\n\n{divider_line}\n") # printing divider line from design.py

        # Asking if user wants to add another record or not.
        ch = int(input("\t\t[0] Back\t\t[1] Add Record\t\tChoice: ")) # prompting user to enter his/her choice.
        record_choices(ch, self.un) # directing user's choice to function record_choices().
 
# this class contains methods which will print the View All Record Page. 
class View(Record_ch): # inheriting class Record_ch.
    # explicitly inheriting attributes of Record_ch.
    def __init__(self, un, pw=None): # setting pw to None, since we don't need a value for this.
        super().__init__(un, pw)
    
    # View record function.
    def view_record(self):
        os.system("cls") # clearing screen.
        Homepage(self.un).table_r(n=0) # calling table_r() function to print the tabulated records of the user.

# this function will direct user to their chosen option. 
def record_choices(ch, user):
    if ch == 1: # if user entered 1 then he will be directed to add record page.
        os.system("cls") # clearing screen.
        Add(un=user).add_record() # calling add record () function in order to print out add record page.
    else: # if the user entered 2, then he will be directed to the Homepage.
        os.system("cls") # clearing screen.
        Homepage(un=user).table_r(n=1) # calling function table_r which is inside class Homepage.

# This function is where the user will be directed to, if he enters 1 in the menu.
def sign_in():
    # Promt user to enter username.
    while True: # this loop is for input validation.
        un = str(input("\tUsername:\t"))  # putting username to class User().
        
        # verifying username
        if un in user_list: # if the username the user has entered was already used by another user, the program will prompt again foe him to enter another username.
            print("\tUsername Already Exist.")
            print()
        else: # but if the username hasn't been used then the user will be directed to the next prompt.
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
    New_user(un, pw).user_info() # in order to create a txt file with user's username as file name.
    User(un, pw).user_account() # in order to add user's name to the userlist.

    # directing user to home page.
    os.system("cls")
    NewUser_data(un, pw).user_personal_info() # this will print the page where the user needs to enter his/her weight, height, etc.
    os.system("cls") # for clearing screen.
    Homepage(un, pw).table_r(n=1) # printing the Homepage...

# This function is where the user will be directed to, if he enters 2 in the menu.
def log_in():
    # Promt user to enter username.
    while True: # thi loop will check if the username exists.
        un = str(input("\tUsername:\t")) # prompt user to enter his username.
        
        # verifying username
        if un in user_list: # checking if the username exits in userlist.
            break # if it does the program will continue.
        else: 
            print("\tUsername Doesn't Exist.") # if the username doesn't exist the program will prompt again.
            print()
    
    # Prompt user to enter password
    while True: # this loop checks if the password is correct.
        pw = str(input("\tPassword:\t")) # prompting user to enter his password.

        # Verifying Password
        try:
            if pw not in user_list: # checking if password is correct.
                raise ValueError # valueerror pertains to the error message in except function.
            break # if the password is correct the program will break out of the loop and continue to the next program.
        except:
            print("\tIncorrect Password!!") # error message.
            print() # will prompt the user again to enter password.

    # directing User's input to class User
    User(un, pw).user_account()

    # directing user to home page.
    os.system("cls")
    Homepage(un, pw).table_r(n=1) # pring the homepage.

