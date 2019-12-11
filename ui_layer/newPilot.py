from ui_layer.uiAPI import UI_API
from ui_layer.validation import ssn_validation, name_validation, pilot_validation, licence_validation, phone_validation, email_vaidation

SPACER = "_____________________________________________"

class New_Pilot:
    def __init__(self):
        self.__UI_API = UI_API()
        self.__ssn = ""
        self.__name = ""
        self.__role = ""
        self.__licence = ""
        self.__email = ""
        self.__address = ""
        self.__gsm = ""

    def create_pilot(self):
        print("New Pilot: ")
        ssn_check = ""
        while ssn_check != None:
            self.__ssn = input("SSN: ")
            ssn_check = ssn_validation(self.__ssn)

        name_check = "BOB"
        while name_check != None:
            self.__name = input("Full name: ")
            name_check = name_validation(self.__name)
        role_check = "BOB"
        while role_check != None:
            self.__role = input("Role: ").lower()
            role_check = pilot_validation(self.__role)
        licence_check = "BOB"

        while licence_check != None:
            self.__licence = input("Licence: ")
            licence_check = licence_validation(self.__licence)

        email_check = "BOB"
        while email_check != None:
            self.__email = input("Email: ")
            email_check = email_vaidation(self.__email)

        gsm_cheker = "BOB"
        self.__address = input("Address: ")
        while gsm_cheker != None:
            self.__gsm = input("GSM: ")
            gsm_cheker = phone_validation(self.__gsm)

        # Villuchekka
        # Hér væri gott að prenta út nýan pilot
        print(SPACER)
        self.__UI_API.set_pilot(self.__ssn, self.__name, self.__role, self.__licence, self.__email, self.__address, self.__gsm)