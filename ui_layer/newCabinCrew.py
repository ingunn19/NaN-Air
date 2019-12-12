from ui_layer.uiAPI import UI_API
from ui_layer.validation import ssn_validation, name_validation, pilot_validation, phone_validation, email_validation, address_validation


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

    # EMPLOYEE_ID //
    # SSN +
    # NAME +
    # ROLE +
    # LICENCE //
    # ADDRESS +
    # GSM +
    # EMAIL +
    def create_Cabin_crew(self):

        ssn_check = False
        while ssn_check == False:
            self.__ssn = input("SSN: ")
            ssn_check = ssn_validation(self.__ssn)
            # is ssn avaleble

        name_check = False
        while name_check == False:
            self.__name = input("Full name: ")
            name_check = name_validation(self.__name)

        role_check = False
        while role_check == False:
            self.__role = input("Role: ").lower()
            role_check = pilot_validation(self.__role)

        address_checkker = False
        while address_checkker == False:
            self.__address = input("Address: ")
            address_checkker = address_validation(self.__address)

        gsm_cheker = False
        while gsm_cheker == False:
            self.__gsm = input("GSM: ")
            gsm_cheker = phone_validation(self.__gsm)

        email_check = False
        while email_check == False:
            self.__email = input("Email: ")
            email_check = email_validation(self.__email)


        #Hér væri flott að prenta út nýa flugþjóninn
        print(f"{self.__ssn}    {self.__name}    {self.__role}    {self.__address}    {self.__gsm}    {self.__email}")
        print(SPACER)
        self.__UI_API.set_Cabin_crew(self.__ssn, self.__name, self.__role, self.__address, self.__gsm, self.__email)