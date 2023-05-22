choice = input("Enter 1 to create a new account or 2 to log in: ")

if choice == "1":
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confPassword = input("Confirm password: ")

    if password == confPassword:
        print("User accepted!")
        with open("user_info.txt", "a") as file:
            file.write(f"{name},{email},{password}\n")

        print("User information saved successfully!")
    else:
        print("Invalid password combination")

elif choice == "2":
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    with open("user_info.txt", "r") as file:
        found_user = False
        for line in file:
            user_info = line.strip().split(",")
            if len(user_info) >= 3 and user_info[1] == email and user_info[2] == password:
                found_user = True
                print(f"Welcome back, {user_info[0]}!")
                break

        if not found_user:
            print("Invalid email or password. Please try again.")
import os
import pickle


def getCalories(question):
    calories = input(question)
    if calories.isdigit():
        calories = int(calories)
        if calories > -1 and calories < 50000:
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
    print("\nYour average calorie intake for the week:", average)

    if total > 21000:
        print("\nYou are eating too many calories.")
    elif total < 9000:
        print("\nYou are eating far too few calories.")
    input("Press enter to continue")
    return week


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("\t\t **********   Welcome to Nutrinometer   **********\n")
    print("Num\tMon \tTue \tWed \tThur \tFri \tSat \tSun \tAvg \tTotal")
    count = 1
    for week in month:
        if len(week) == 7:
            print(count, end="\t")
            for day in week:
                print(day, end="\t")
            print(int(sum(week) / 7), end="\t")
            print(sum(week), end="\n")
        else:
            print("")
        # print(str(count) +"\t" + "\t".join([str(x) for x in week]) + ""\n"
        count = count + 1

    weeknum = int(input("\n\nWhich week would you like to edit the values for? (1,2,3,4)"))
    month[weeknum - 1] = getAweek()
    pickle.dump(month, open("save.p", "wb"))

    main()


try:
    month = pickle.load(open("save.p", "rb"))
except:
    month = [[], [], [], []]

main()
