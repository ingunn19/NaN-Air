from ui_layer.uiAPI import UI_API
from ui_layer.withTask import WithTask
from ui_layer.noTask import NoTask
from ui_layer.licence import Licence
from ui_layer.detailedSearch import DetailedSearch

SPACER = "_____________________________________________"

class EmployeeOverview:
    def __init__(self):
        self.__UI_API = UI_API()
 
        self.__detailed_search = DetailedSearch()
        self.__with_task = WithTask()
        self.__no_task = NoTask()
        self.__licence = Licence()

    def overview_menu(self):
        __classObject = EmployeeOverview()
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
                __classObject.view_employees()

            elif action == "2":
                print(SPACER)
                __classObject.all_pilots()

            elif action == "3":
                print(SPACER)
                __classObject.all_cabin_crew()

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

    def view_employees(self):
        print("All employees")
        self.__UI_API.get_all_employees()
        input()
        print(SPACER)

    def all_pilots(self):
        print("Here we list all pilots!")
        self.__UI_API.get_all_pilots()
        input()
        print(SPACER)

    def all_cabin_crew(self):
        print("Here we list all attendants!")
        self.__UI_API.get_all_cabin_crew()
        input()
        print(SPACER)