from ui_layer.employeeOverview import EmployeeOverview
from ui_layer.worktripHistory import WorktripHistory
from ui_layer.destinationOverview import DestinationOverview
from ui_layer.aircraftOverview import AircraftOverview

SPACER = "_____________________________________________"

class Overview:
    def __init__(self):
        self.__employee_Overview = EmployeeOverview()  # Employee
        self.__workTrip_Overview = WorktripHistory()
        self.__destination_Overview = DestinationOverview()
        self.__aircraft_Overview = AircraftOverview()

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
                self.__employee_Overview.overview_menu()

            elif action == "2":
                print(SPACER)
                self.__workTrip_Overview.workTrip_history_menu()

            elif action == "3":
                print(SPACER)
                self.__destination_Overview.destination_overview_menu()

            elif action == "4":
                print(SPACER)
                self.__aircraft_Overview.Aircraft_Overview_Menu()

            elif action == "q":
                quit()