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

# ang normal calorie intake daw ata ay nasa 2000+ per day sabi ni google kaya pag irrun nyo yung code gawin nyong nasa 4digits ang input
# magugulo kasi ang table pag nilagyan nyo ng 1 or 2 digits yan HAHAHAHAH

# tinry ko nga pala ako gawin yung user registration feature natin parang keri naman sya. idagdag ko nalang dito pag goods na

# bale itong code pala natin ay meron ng 3 features(?) pero aayusin padin natin HAHAHA tas pang apat na feature na natin yung sa user registration
# kulang pa tayo ng dietary needs
# mag meet na din siguro talaga tayo habang nagawa dito sa pycharm para makapag usap ng ayos HAHAHAHA
