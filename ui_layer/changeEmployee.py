from ui_layer.uiAPI import UI_API
SPACER = "_____________________________________________"
class ChangeEmployee:
    def __init__(self):
        self.__UI_API = UI_API()
        self.__employee_ID = ""
        self.__employee = []

    def change_employee_info(self):
        print("Change employee info:")
        self.__employee_ID = input("Employee ID: ")
        self.__employee = self.__UI_API.get_personal_info(self.__employee_ID)
        orgenallist = self.__employee.copy()
        print("tis is orginal list", orgenallist)
        self.__employee[2] = input("New role: ")
        if self.__employee[2] == "":
            self.__employee[2] = orgenallist[2]
        self.__employee[3] = input("New Licence: ")
        if self.__employee[3] == "":
            self.__employee[3] = orgenallist[3]
        self.__employee[4] = input("New address: ")
        if self.__employee[4] == "":
            self.__employee[4] = orgenallist[4]
        self.__employee[5] = input("New GSM: ")
        if self.__employee[5] == "":
            self.__employee[5] = orgenallist[5]
        print(self.__employee)
        self.__UI_API.set_changes_for_existing_employee(self.__employee)