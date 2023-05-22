import os
import pickle


def getCalories(question):
    calories = input(question)
    if calories.isdigit():
        calories = int(calories)
        if 0 <= calories <= 50000:
            return calories
        else:
            print("Invalid amount")
            return getCalories(question)
    else:
        print("Numbers only please")
        return getCalories(question)


def getAweek():
    os.system("cls" if os.name == "nt" else "clear")
    print("Please enter your calories for the last 7 days")
    week = []
    for i in range(7):
        day = getCalories(question="Day " + str(i + 1) + ":")
        week.append(day)

    total = sum(week)
    average = int(total / 7)

    print("\n\nYour total calorie intake for the week:", total)
    print("Your average calorie intake for the week:", average)

    if total > 21000:
        print("\nYou are eating too many calories.")
    elif total < 9000:
        print("\nYou are eating far too few calories.")
    input("Press enter to continue")
    return week


def create_new_account():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confPassword = input("Confirm password: ")
    if password == confPassword:
        print("User accepted!")
        user_data = {
            'name': name,
            'email': email,
            'password': password,
            'month': [[], [], [], []]
        }
        with open(f"{email}.p", "wb") as file:
            pickle.dump(user_data, file)

        print("User information saved successfully!")
        main(user_data)
    else:
        print("Invalid password combination")


def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    try:
        with open(f"{email}.p", "rb") as file:
            user_data = pickle.load(file)
            if user_data['password'] == password:
                print(f"Welcome back, {user_data['name']}!")
                return user_data
            else:
                print("Invalid email or password. Please try again.")
    except FileNotFoundError:
        print("Invalid email or password. Please try again.")

    return None


def main(user_data):
    os.system("cls" if os.name == "nt" else "clear")
    print("\t\t **********   Welcome to Nutrinometer   **********\n")
    print("Num\tMon \tTue \tWed \tThur \tFri \tSat \tSun \tAvg \tTotal")
    count = 1
    for week in user_data['month']:
        if len(week) == 7:
            print(count, end="\t")
            for day in week:
                print(day, end="\t")
            print(int(sum(week) / 7), end="\t")
            print(sum(week), end="\n")
        else:
            print("")
        count += 1

    try:
        weeknum = int(input("\n\nWhich week would you like to edit the values for? (1,2,3,4)"))
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        return

    if 1 <= weeknum <= 4:
        user_data['month'][weeknum - 1] = getAweek()
        with open(f"{user_data['email']}.p", "wb") as file:
            pickle.dump(user_data, file)
        main(user_data)
    else:
        print("Invalid week number. Please try again.")


def run_program():
    choice = input("Enter 1 to create a new account or 2 to log in: ")

    if choice == "1":
        create_new_account()
    elif choice == "2":
        user_data = login()
        if user_data:
            main(user_data)


run_program()
