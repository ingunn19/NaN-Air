from ui_layer.initializeMenu import Initialize
from ui_layer.overview import Overview
from ui_layer.changeInfo import Change_Info

SPACER = "____________________________________________________________________________________________________________________________________________________________________________"

class MainMenu:
    def __init__(self):
        self.__initialize = Initialize()
        self.__overview = Overview()
        self.__change_info = Change_Info()

    def main_menu(self):
        action = ""
        while(action != "q"):
            print("You can do the following: ")
            print("1. Initialize")
            print("2. Overview")
            print("3. Change information")
            print("Q. Quit")

            action = input("Choose an option: ").lower()
            if action == "b":
                print(SPACER)

            if action == "1":
                print(SPACER)
                self.__initialize.Initialize_Menu()

            elif action == "2":
                print(SPACER)
                self.__overview.Overview_Menu()

            elif action == "3":
                print(SPACER)
                self.__change_info.Change_info_Menu()