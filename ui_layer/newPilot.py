from ui_layer.uiAPI import UI_API
from ui_layer.validation import ssn_validation, name_validation, pilot_validation, plane_type_ID_validation, phone_validation, email_validation, address_validation, is_ssn_available, employee_email_validation, employee_gsm_validation

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

    # EMPLOYEE_ID //
    # SSN +
    # NAME +
    # ROLE +
    # LICENCE +
    # ADDRESS +
    # GSM +
    # EMAIL +
    def create_pilot(self):
        print("New Pilot: ")

        check = False
        while check == False:
            self.__ssn = input("SSN: ")
            ssn_check = ssn_validation(self.__ssn)
            avalable_ssn = is_ssn_available(self.__ssn)
            if ssn_check == True:
                if avalable_ssn == True:
                    check = True

        name_check = False
        while name_check == False:
            self.__name = input("Full name: ")
            name_check = name_validation(self.__name)

        role_check = False
        while role_check == False:
            self.__role = input("Role: ").lower()
            role_check = pilot_validation(self.__role)

        licence_check = False
        while licence_check == False:
            self.__licence = input("Licence: ")
            licence_check = plane_type_ID_validation(self.__licence)

        check = False
        while check == False:
            self.__email = input("Email: ")
            email_check = email_validation(self.__email)
            email_avalble = employee_email_validation(self.__email)
            if email_check == True:
                if email_avalble == True:
                    check = True

        address_checkker = False
        while address_checkker == False:
            self.__address = input("Address: ")
            address_checkker = address_validation(self.__address)

        cheker = False
        while cheker == False:
            self.__gsm = input("GSM: ")
            gsm_cheker = phone_validation(self.__gsm)
            gsm_avalable = employee_gsm_validation(self.__gsm)
            if gsm_cheker == True:
                if gsm_avalable == True:
                    cheker = True


        print(f"{self.__ssn}    {self.__name}    {self.__role}    {self.__licence}    {self.__address}    {self.__gsm}    {self.__email}")
        print(SPACER)
        self.__UI_API.set_pilot(self.__ssn, self.__name, self.__role, self.__licence, self.__address, self.__gsm, self.__email)