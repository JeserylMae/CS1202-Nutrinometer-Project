#calories calculator

weight = float(input("Enter your weight in kilos: "))
height = float(input("Enter your height in centimeters: "))
age = int(input("Enter you age: "))
sex = input("Enter your sex [male or female]: ")
activity_level = input("Enter your activity level (sedentary,lightly active,moderately active,very active): ")

import os
os.system('cls')

print("Input food portion a day[if none input 0]")
num1 = float(input("Portion of meat: "))
num2 = float(input("Portion of rice: "))
num3 = float(input("Portion of veggies: "))
num4 = float(input("Portion of seafood: "))

totalcal = (num1 + num2 + num3 + num4)*280
answer = totalcal / 4


def calculate_bmr(weight, height, age, sex):
    if sex == "male":
        bmr = 66.5 + (13.8 * weight) + (5 * height) - (6.75 * age)
    else:
        bmr = 655 + (9.6 * weight) + (1.9 * height) - (4.7 * age)
    return bmr
def calculate_daily_calories(bmr, activity_level):
    if activity_level == "sedentary":
        calories = bmr * 1.2
    elif activity_level == "lightly active":
        calories = bmr * 1.375
    elif activity_level == "moderately active":
        calories = bmr * 1.55
    else:
        calories = bmr * 1.725
    return calories

bmr = calculate_bmr(weight, height, age, sex)
calories = calculate_daily_calories(bmr, activity_level)

print("Your amount of calories is: ", answer)
print("Your daily calorie needs are: ", calories)

def Get_NormRequired():
    if answer > calories:
        print("\nYou are eating too many calories.")
    elif answer == calories:
        print("\nYou're at the right amount of calories. ")
    else:
        print("\nYou need to eat more with calories. ")












