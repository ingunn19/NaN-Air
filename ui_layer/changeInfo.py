from ui_layer.changeEmployee import ChangeEmployee
from ui_layer.changeWorkTrip import ChangeWorkTrip
from ui_layer.changeDestination import ChangeDestination
from ui_layer.changeAircraft import ChangeAircraft
#from UI_API import UI_Api
SPACER = "_____________________________________________"
class Change_Info:
    def __init__(self):
        #self.__UI_API = UI_Api()
        self.__Change_Employee = ChangeEmployee()
        self.__Change_WorkTrip = ChangeWorkTrip()
        self.__Change_Destination = ChangeDestination()
        self.__Change_Aircraft = ChangeAircraft()

    def Change_info_Menu(self):
        action = ""
        while (action != "b"):
            print("Change info:")
            print("1. Employee info")
            print("2. Aircraft info")
            print("3. WorkTrip info")
            print("4. Destination info")
            print("B. Back to main menu")
            print("Q. Quit")

            action = input("Choose an option: ").lower()
            if action == "b":
                print(SPACER)

            if action == "1":
                print(SPACER)
                self.__Change_Employee.change_employee_info()

            elif action == "2":
                print(SPACER)
                self.__Change_Aircraft.change_aircraft()

            elif action == "3":
                print(SPACER)
                self.__Change_WorkTrip.change_workTrip()

            elif action == "4":
                print(SPACER)
                self.__Change_Destination.change_destination()

            elif action == "q":
                quit()