from ui_layer.uiAPI import UI_API
SPACER = "____________________________________________________________________________________________________________________________________________________________________________"
class AircraftOverview:
    def __init__(self):
        self.__UI_API = UI_API()
    def Aircraft_Overview_Menu(self):
        action = ""
        while action != "b":
            print("Overview: ")
            print("1. List all planes")
            print("2. List state of all planes")
            print("B. Back")
            print("Q. Quit")

            action = input("Choose an option: ").lower()
            if action == "b":
                print(SPACER)

            if action == "1":
                print(SPACER)
                self.__UI_API.get_all_planes()
                print(SPACER)
                input()

            elif action == "2":
                print(SPACER)
                self.__UI_API.get_plane_state()
                input()

            elif action == "q":
                quit()
