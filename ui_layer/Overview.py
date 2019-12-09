from EmployeeOverview import EmployeeOverview
from WorktripHistory import WorktripHistory
from DestinationOverview import DestinationOverview
from AircraftOverview import AircraftOverview
SPACER = "_____________________________________________"
class Overview:
    def __init__(self):
        self.__Employee_Overview = EmployeeOverview()  # Employee
        self.__WorkTrip_Overview = WorktripHistory()
        self.__Destination_Overview = DestinationOverview()
        self.__Aircraft_Overview = AircraftOverview()

    def Overview_Menu(self):
        action = ""
        while (action != "b"):
            print("Overview: ")
            print("1. Employee overview")
            print("2. WorkTrip overview")
            print("3. Destination overview")
            print("4. Aircraft overview")
            print("B. Back to main menu")
            print("Q. Quit")

            action = input("Choose an option: ").lower()
            if action == "b":
                print(SPACER)

            if action == "1":
                print(SPACER)
                self.__Employee_Overview.Overview_menu()

            elif action == "2":
                print(SPACER)
                self.__WorkTrip_Overview.workTrip_history_menu()

            elif action == "3":
                print(SPACER)
                self.__Destination_Overview.destination_overview_menu()

            elif action == "4":
                print(SPACER)
                self.__Aircraft_Overview.Aircraft_Overview_Menu()

            elif action == "q":
                quit()