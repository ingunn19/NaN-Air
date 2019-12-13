from ui_layer.uiAPI import UI_API
SPACER = "____________________________________________________________________________________________________________________________________________________________________________"
class DestinationOverview:
    def __init__(self):
        self.__UI_API = UI_API()
    def destination_overview_menu(self):
        action = ""
        while (action != "b"):
            print("Destination overview menu: ")
            print("1. List all destinations")
            print("2. Specific destination")
            print("B. Back")
            print("Q. Quit")

            action = input("Choose an option: ").lower()
            if action == "b":
                print(SPACER)

            if action == "1":
                print(SPACER)
                self.__UI_API.get_all_destinations()
                print(SPACER)
                input()

            elif action == "2":
                print(SPACER)
                self.__UI_API.get_all_destinations()
                print("Choose a Destination:")
                a_destination = input()
                print(a_destination)
                self.__UI_API.get_specific_destination(a_destination)
                print(SPACER)
                input()

            elif action == "q":
                quit()
