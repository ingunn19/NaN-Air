from ui_layer.uiAPI import UI_API
from ui_layer.validation import licence_validation, email_vaidation, address_validation, phone_validation
SPACER = "_____________________________________________"
class ChangeEmployee:
    def __init__(self):
        self.__UI_API = UI_API()
        self.__employee_ID = ""
        self.__employee = []

    def change_employee_info(self):
        print("Change employee info:")
        id_checkker = False
        while id_checkker == False:
            try:
                self.__employee_ID = input("Employee ID: ")
                id_checkker = True
            except :# vantar villumeldinguna þarf að prufa að keyra þetta
                continue
        self.__employee = self.__UI_API.get_personal_info(self.__employee_ID)
        orgenallist = self.__employee.copy()

        # vannatar employee role checkker
        self.__employee[2] = input("New role: ")
        if self.__employee[2] == "":
            self.__employee[2] = orgenallist[2]

        licence_checkker = False
        while licence_checkker== False:
            self.__employee[3] = input("New Licence: ")
            if self.__employee[3] == "":
                self.__employee[3] = orgenallist[3]
            licence_checkker = licence_validation(self.__employee[3])

        email_chekker = False
        while email_chekker == False:
            self.__employee[4] = input("New email: ")
            if self.__employee[4] == "":
                self.__employee[4] = orgenallist[4]
            email_chekker = email_vaidation(self.__employee[4])

        address_checkker = False
        while address_checkker == False:
            self.__employee[5] = input("New address: ")
            if self.__employee[5] == "":
                self.__employee[5] = orgenallist[5]
            address_checkker = address_validation(self.__employee[5])

        gsm_checkker = False
        while gsm_checkker == False:
            self.__employee[6] = input("New GSM: ")
            if self.__employee[6] == "":
                self.__employee[6] = orgenallist[6]
            gsm_checkker = phone_validation(self.__employee[6])
        # hér væri gott að sýna breitingar
        self.__UI_API.set_changes_for_existing_employee(self.__employee)
