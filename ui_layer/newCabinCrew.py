from ui_layer.uiAPI import UI_API
from ui_layer.validation import ssn_validation, name_validation, pilot_validation, phone_validation, email_vaidation


SPACER = "_____________________________________________"

class New_CabinCrew:
    def __init__(self):
        self.__UI_API = UI_API()
        self.__ssn = ""
        self.__name = ""
        self.__role = ""
        self.__email = ""
        self.__address = ""
        self.__gsm = ""

    def create_Cabin_crew(self):
        ssn_check = True
        while ssn_check == True:
            self.__ssn = input("SSN: ")
            ssn_check = ssn_validation(self.__ssn)

        name_check = True
        while name_check == True:
            self.__name = input("Full name: ")
            name_check = name_validation(self.__name)

        role_check = True
        while role_check == True:
            self.__role = input("Role: ").lower()
            role_check = pilot_validation(self.__role)

        email_check = True
        while email_check == True:
            self.__email = input("Email: ")
            email_check = email_vaidation(self.__email)

        gsm_cheker = True
        self.__address = input("Address: ")
        while gsm_cheker == True:
            self.__gsm = input("GSM: ")
            gsm_cheker = phone_validation(self.__gsm)
        print(SPACER)
        #Villuchekka
        #Hér væri flott að prenta út ýa fugmannin
        self.__UI_API.set_Cabin_crew(self.__ssn, self.__name, self.__role, self.__email, self.__address, self.__gsm)