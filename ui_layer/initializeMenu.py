from ui_layer.newEmployee import New_Employee
from ui_layer.newAirplane import New_Airplane
from ui_layer.newWorkTrip import New_WorkTrip
from ui_layer.newDestination import New_Destination
SPACER = "_______________________________________________________________________________________________________________________________________"

class Initialize:
    def __init__(self):
        self.__Initialize_Employee = New_Employee()
        self.__Initialize_Aircraft = New_Airplane()
        self.__Initialize_WorkTrip = New_WorkTrip()
        self.__Initialize_Destination = New_Destination()

    def Initialize_Menu(self):
        action = ""
        while (action != "b"):
            print("Initialize: ")
            print("1. Employee")
            print("2. Aircraft")
            print("3. WorkTrip")
            print("4. Destination")
            print("B. Back to main menu")
            print("Q. Quit")

            action = input("Choose an option: ").lower()
            if action == "b":
                print(SPACER)
            if action == "1":
                print(SPACER)
                self.__Initialize_Employee.New_Employee_Menu()

            elif action == "2":
                print(SPACER)
                self.__Initialize_Aircraft.New_Airplane()

            elif action == "3":
                print(SPACER)
                self.__Initialize_WorkTrip.Initialize_WorkTrip()

            elif action == "4":
                print(SPACER)
                self.__Initialize_Destination.Initialize_Destination()

            elif action == "q":
                quit()