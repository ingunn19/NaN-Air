from ui_layer.uiAPI import UI_API

SPACER = "______________________________________________"

class Licence:
    def __init__(self):
        self.__UI_API = UI_API()
    def licence_menu(self):
        action = ""
        while action != "b":
            print("Licence menu:")
            print("1. Airplanes")
            print("2. Pilot")
            print("B. Back")
            print("Q. Quit")
            action = input("Choose an option: ").lower()
            if action == "b":
                print(SPACER)

            if action == "1":
                print(SPACER)
                plane_model = input("Plane model: ")
                # Villuchekka
                self.__UI_API.get_airplane_licence(plane_model)
                input()
            elif action == "2":
                print(SPACER)
                self.__UI_API.get_pilot_licence()
                input()
            elif action == "q":
                quit()
