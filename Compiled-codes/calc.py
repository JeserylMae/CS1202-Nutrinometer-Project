
"""
CALCULATOR
"""

# This function calculates the bmr of the user.
def calc_bmr(weight, height, sex, age): # the values of these parameters are gotten in log.py
    if sex == 0: # if male
        bmr = 66.5 + (13.8 * weight) + (5 * height) - (6.75 * age)
    else: # if female
        bmr = 655 + (9.6 * weight) + (1.9 * height) - (4.7 * age)

    bmr = round(bmr, 2) # rounding bmr's decimal places into two.
    
    # returning bmr to variable bmr in class NewUser_data, def user_personal_info    
    return bmr 

# thi function computes the required calories of the user.
def calc_daily_calories(actLevel, bmr): # the values of these parameters are gotten in log.py
    if actLevel == 1: # 1 = sedentary
        calories = (bmr * 1.2)/3
    elif actLevel == 2: # 2 = Lightly Active
        calories = (bmr * 1.375)/3
    elif actLevel == 3: # 3 = Moderately Active
        calories = (bmr * 1.55)/3
    else: # 4 = Very Active
        calories = (bmr * 1.725)/3
    
    calories = round(calories, 2) # rounding decimal places into two.
    
    # returning calories to a variable in class NewUser_data, def user_personal_info
    return calories 

# this function calculates the total calories found in consumed foods of the user.
def food_input(un, rice, meat, veggies, seafood, i_date, i_mealType): # the values of these parameters are gotten in log.py
    
    # computing the total calories.
    total_cal = (rice*200) + (meat*150) + (veggies*75) + (seafood*150)
    
    # defining i_food.
    i_food = ""
    
    # If the user entered a value for portion that is not zero, i_food will concatenate corresponding string.
    if rice != 0:
        i_food += "Rice + "
    if meat != 0:
        i_food += "Meat + "
    if veggies != 0:
        i_food += "Vegetables + "
    if seafood != 0:
        i_food += "Seafood"

    # adding date, meal type, food, and total cal to the txt file with user' name as filename.
    with open(f"{un}.txt", "a") as file:
        file.write(f"{i_date} | {i_mealType} | {i_food} | {total_cal} | ")

    # returning the total cal to class Add, def add_record 
    return total_cal 

# this function will analyze if the luser has met the required calories.
def analyze_kcal(un, total_cal, req_cal):
    if total_cal > req_cal:
        status = "Higher Than Required Calories."
    elif total_cal < req_cal:
        status = "Lower Than Required Calories."
    else:
        status = "Met Required Calories."
    
    # status will be added to the txt file with user's name as file name.
    with open(f"{un}.txt", "a") as file:
        file.write(status + '\n')
