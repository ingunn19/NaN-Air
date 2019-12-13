from ui_layer.newPilot import New_Pilot
from ui_layer.newCabinCrew import New_CabinCrew
SPACER = "____________________________________________________________________________________________________________________________________________________________________________"
class New_Employee:
    def __init__(self):
        self.__New_Pilot = New_Pilot()
        self.__Cabin_crew = New_CabinCrew()
        #self.__Main_Menu = MainMenu()

    def New_Employee_Menu(self):
        action = ""
        while (action != "b"):
            print("Initialize: ")
            print("1. Pilot")
            print("2. Cabin crew")
            print("B. Back")
            print("Q. Quit")

            action = (input("Choose an option: ")).lower()
            if action == "b":
                print(SPACER)

            if action == "1":
                print(SPACER)
                self.__New_Pilot.create_pilot()

            elif action == "2":
                print(SPACER)
                self.__Cabin_crew.create_Cabin_crew()

            elif action == "q":
                quit()