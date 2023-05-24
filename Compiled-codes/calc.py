
def calc_bmr(weight, height, sex, age):    
    if sex == 0: # if male
        bmr = 66.5 + (13.8 * weight) + (5 * height) - (6.75 * age)
    else: # if female
        bmr = 655 + (9.6 * weight) + (1.9 * height) - (4.7 * age)

    # class NewUser_data, def user_personal_info    
    bmr = round(bmr, 2)
    return bmr

def calc_daily_calories(actLevel, bmr):
    if actLevel == 1: # 1 = sedentary
        calories = (bmr * 1.2)/3
    elif actLevel == 2: # 2 = Lightly Active
        calories = (bmr * 1.375)/3
    elif actLevel == 3: # 3 = Moderately Active
        calories = (bmr * 1.55)/3
    else:
        calories = (bmr * 1.725)/3
    
    calories = round(calories, 2)
    # class NewUser_data, def user_personal_info
    return calories 


def food_input(un, rice, meat, veggies, seafood, i_date, i_mealType):
    total_cal = (rice*200) + (meat*150) + (veggies*75) + (seafood*150)
    i_food = ""

    if rice != 0:
        i_food += "Rice + "
    if meat != 0:
        i_food += "Meat + "
    if veggies != 0:
        i_food += "Vegetables + "
    if seafood != 0:
        i_food += "Seafood"

    with open(f"{un}.txt", "a") as file:
        file.write(f"{i_date} | {i_mealType} | {i_food} | {total_cal} | ")

    # class Add, def add_record 
    return total_cal 

def analyze_kcal(un, total_cal, req_cal):
    if total_cal > req_cal:
        status = "Higher Than Required Calories."
    elif total_cal < req_cal:
        status = "Lower Than Required Calories."
    else:
        status = "Met Required Calories."
    
    with open(f"{un}.txt", "a") as file:
        file.write(status + '\n')
