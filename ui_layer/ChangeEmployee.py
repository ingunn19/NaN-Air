from UI_API import UI_Api
SPACER = "_____________________________________________"
class ChangeEmployee:
    def __init__(self):
        self.__UI_API = UI_Api()
        self.employee_ID = ""
        self.employee = []
    def change_employee_info(self):
        print("Change employee info:")
        self.employee_ID = input("Employee ID: ")
        self.employee = self.__UI_API.get_personal_info(self.employee_ID)
        orgenallist = self.employee.copy()
        print("tis is orginal list", orgenallist)
        SSN = self.employee[0]
        NAME = self.employee[1]
        ROLE = self.employee[2]
        LICENCE = self.employee[3]
        ADDRESS = self.employee[4]
        GSM = self.employee[5]
        print(f"{SSN} {NAME} {ROLE} {LICENCE} {ADDRESS} {GSM}")
        self.employee[2] = input("New role: ")
        if self.employee[2] == "":
            self.employee[2] = orgenallist[2]
        self.employee[3] = input("New Licence: ")
        if self.employee[3] == "":
            self.employee[3] = orgenallist[3]
        self.employee[4] = input("New address: ")
        if self.employee[4] == "":
            self.employee[4] = orgenallist[4]
        self.employee[5] = input("New GSM: ")
        if self.employee[5] == "":
            self.employee[5] = orgenallist[5]
        print(self.employee)
        self.__UI_API.set_changes_for_existing_employee(self.employee)