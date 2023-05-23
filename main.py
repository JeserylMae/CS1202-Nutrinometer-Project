import os
import pickle


class Nutrinometer:
    def __init__(self):
        self.user_data = None

    def getCalories(self, question):
        calories = input(question)
        if calories.isdigit():
            calories = int(calories)
            if 0 <= calories <= 50000:
                return calories
            else:
                print("Invalid amount")
                return self.getCalories(question)
        else:
            print("Numbers only please")
            return self.getCalories(question)

    def getFoodIntake(self):
        food_intake = {}
        print("Please enter your food intake for the day")
        while True:
            food = input("Food (enter 'done' to finish): ")
            if food.lower() == "done" or not food:
                break
            portion_size = self.getCalories("Portion size (calories): ")
            food_intake[food] = portion_size
        return food_intake

    def getAweek(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Please enter your calories for the last 7 days")
        week = []
        for i in range(7):
            day = self.getFoodIntake()
            total_calories = sum(day.values())
            week.append(total_calories)
        return week

    def create_new_account(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        confPassword = input("Confirm password: ")
        if password == confPassword:
            print("User accepted!")
            self.user_data = {
                'name': name,
                'email': email,
                'password': password,
                'month': [[], [], [], []]
            }
            with open(f"{email}.p", "wb") as file:
                pickle.dump(self.user_data, file)

            print("User information saved successfully!")
            self.main()
        else:
            print("Invalid password combination")

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        try:
            with open(f"{email}.p", "rb") as file:
                self.user_data = pickle.load(file)
                if self.user_data['password'] == password:
                    print(f"Welcome back, {self.user_data['name']}!")
                    return True
                else:
                    print("Invalid email or password. Please try again.")
        except FileNotFoundError:
            print("Invalid email or password. Please try again.")

        return False

    def main(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\t\t **********   Welcome to Nutrinometer   **********\n")
        print("Num\tMon \tTue \tWed \tThur \tFri \tSat \tSun \tAvg \tTotal")
        count = 1
        for week in self.user_data['month']:
            if len(week) == 7:
                print(count, end="\t")
                for day in week:
                    print(day, end="\t")
                print(int(sum(week) / 7), end="\t")
                print(sum(week), end="\n")
            else:
                print("")
            count += 1

        while True:
            try:
                weeknum = int(input("\n\nWhich week would you like to edit the values for? (1,2,3,4)"))
                if 1 <= weeknum <= 4:
                    self.user_data['month'][weeknum - 1] = self.getAweek()
                    with open(f"{self.user_data['email']}.p", "wb") as file:
                        pickle.dump(self.user_data, file)
                    break
                else:
                    print("Invalid week number. Please try again.")
            except KeyboardInterrupt:
                print("\nProgram interrupted. Exiting...")
                return

        self.main()

    def run_program(self):
        choice = input("Enter 1 to create a new account or 2 to log in: ")

        if choice == "1":
            self.create_new_account()
        elif choice == "2":
            if self.login():
                self.main()


nutrinometer = Nutrinometer()
nutrinometer.run_program()
