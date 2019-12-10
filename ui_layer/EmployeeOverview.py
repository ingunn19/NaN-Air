from UI_API import UI_Api
from WithTask import WithTask
from NoTask import NoTask
from Licence import Licence
SPACER = "_____________________________________________"
class EmployeeOverview:
    def __init__(self):
        self.__UI_API = UI_Api()
        self.__all_employees = AllEmployees()
        self.__all_pilots = AllPilots()
        self.__all_cabin_crew = AllCabinCrew()
        self.__detailed_search = DetailedSearch()

        self.__with_task = WithTask()
        self.__no_task = NoTask()
        self.__licence = Licence()

    def Overview_menu(self):
        action = ""
        while(action != "b"):
            print("Overview menu: ")
            print("1. View all employees")
            print("2. View all pilots")
            print("3. View all cabincrew")
            print("4. Detailed search")
            print("5. Employees with a task")
            print("6. Employees without a task")
            print("7. Licence")
            print("B. Back")
            print("Q. Quit")

            action = input("Choose an option: ").lower()
            if action == "b":
                print(SPACER)

            if action == "1":
                print(SPACER)
                self.__all_employees.view_employees()

            elif action == "2":
                print(SPACER)
                self.__all_pilots.all_pilots()

            elif action == "3":
                print(SPACER)
                self.__all_cabin_crew.all_cabin_crew()

            elif action == "4":
                print(SPACER)
                self.__detailed_search.detailed_search()

            elif action == "5":
                print(SPACER)
                self.__with_task.with_task()

            elif action == "6":
                print(SPACER)
                self.__no_task.no_task()

            elif action == "7":
                print(SPACER)
                self.__licence.licence_menu()

            elif action == "q":
                quit()

class AllEmployees:
    def __init__(self):
        self.__UI_API = UI_Api()
    def view_employees(self):
        print("All employees")
        self.__UI_API.get_all_employees()
        input()
        print(SPACER)
class AllPilots:
    def __init__(self):
        self.__UI_API = UI_Api()
    def all_pilots(self):
        print("Here we list all pilots!")
        self.__UI_API.get_all_pilots()
        input()
        print(SPACER)
class AllCabinCrew:
    def __init__(self):
        self.__UI_API = UI_Api()
    def all_cabin_crew(self):
        print("Here we list all attendants!")
        self.__UI_API.get_all_cabin_crew()
        input()
        print(SPACER)
class DetailedSearch:
    def __init__(self):
        self.__UI_API = UI_Api()
        self.employee_id = ""
    def detailed_search(self):
        self.__UI_API.get_all_employees() #Sýna alla starfsmenn
        print("Choose an employee:")
        self.employee_id = input("Employee ID: ")
        print(SPACER)
        print(f"{self.__UI_API.get_name(self.employee_id)}:")
        action = ""
        while (action != "b"):
            print("1. Personal info")
            print("2. Work schedule")
            print("B. Back")
            print("Q. Quit")

            action = input("Choose an option: ").lower()
            if action == "b":
                print(SPACER)

            if action == "1":
                print(SPACER)
                self.__UI_API.get_personal_info(self.employee_id)
                input()

            elif action == "2":
                print(SPACER)
                year = input("Year: ")
                week = input("week: ")
                self.__UI_API.get_work_schedule(self.employee_id, year, week)
                input()

            elif action == "q":
                quit()