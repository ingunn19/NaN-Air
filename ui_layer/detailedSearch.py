from ui_layer.uiAPI import UI_API

SPACER = "_____________________________________________"

class DetailedSearch:
    def __init__(self):
        self.__UI_API = UI_API()
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