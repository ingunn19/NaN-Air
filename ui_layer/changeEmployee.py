from ui_layer.uiAPI import UI_API
from ui_layer.validation import plane_type_ID_validation, email_vaidation, address_validation, phone_validation, employee_validation
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
        EMPLOYEE_ID = self.__employee[0]
        SSN = self.__employee[1]
        NAME = self.__employee[2]
        ROLE = self.__employee[3]
        LICENCE = self.__employee[4]
        ADDRESS = self.__employee[5]
        GSM = self.__employee[6]
        EMAIL = self.__employee[7]

        ORGINAL_EMPLOYEE_ID = orgenallist[0]
        ORGINAL_SSN = orgenallist[1]
        ORGINAL_NAME = orgenallist[2]
        ORGINAL_ROLE = orgenallist[3]
        ORGINAL_LICENCE = orgenallist[4]
        ORGINAL_ADDRESS = orgenallist[5]
        ORGINAL_GSM = orgenallist[6]
        ORGINAL_EMAIL = orgenallist[7]

        role_checkker = False
        while role_checkker == False:
            ROLE = input("New role: ")
            if ROLE == "":
                ROLE = ORGINAL_ROLE
            role_checkker = employee_validation(ROLE)

        licence_checkker = False
        while licence_checkker== False:
            LICENCE = input("New Licence: ")
            if LICENCE == "":
                LICENCE = ORGINAL_LICENCE
            licence_checkker = plane_type_ID_validation(LICENCE)

        address_checkker = False
        while address_checkker == False:
            ADDRESS = input("New address: ")
            if ADDRESS == "":
                ADDRESS = ORGINAL_ADDRESS
            address_checkker = address_validation(ADDRESS)

        gsm_checkker = False
        while gsm_checkker == False:
            GSM = input("New GSM: ")
            if GSM == "":
                GSM = ORGINAL_GSM
            gsm_checkker = phone_validation(GSM)

        email_chekker = False
        while email_chekker == False:
            EMAIL = input("New email: ")
            if EMAIL == "":
                EMAIL = ORGINAL_EMAIL
            email_chekker = email_vaidation(EMAIL)


        # hér væri gott að sýna breitingar
        self.__UI_API.set_changes_for_existing_employee(self.__employee)
