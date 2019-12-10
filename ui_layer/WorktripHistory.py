from ui_layer.uiAPI import UI_API

SPACER = "_____________________________________________"

class WorktripHistory:
    def __init__(self):
        self.__UI_API = UI_API()

    def workTrip_history_menu(self):
        action = ""
        while (action != "b"):
            print("Overview: ")
            print("1. Worktrip history")
            print("2. Worktrip week overview")
            print("3. Worktrip day overview")
            print("B. Back to main menu")
            print("Q. Quit")

            action = input("Choose an option: ").lower()
            if action == "b":
                print(SPACER)

            if action == "1":
                print("display worktrip history")
                self.__UI_API.get_all_worktrips()
                input()
                print(SPACER)

            elif action == "2":
                print("Week worktrip overview ")
                print("Choose a week: 1 - 52:")
                year = input("Year: ")
                week = input("Week: ")
                self.__UI_API.get_week_worktrip(year, week)
                input()
                print(SPACER)

            elif action == "3":
                print("Day worktrip overview ")
                print("Choose your day: yyyy-mm-dd")
                display_workday = input()
                self.__UI_API.get_day_worktrip(display_workday)
                input()
                print(SPACER)


            elif action == "q":
                quit()

        print(SPACER)