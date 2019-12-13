from ui_layer.uiAPI import UI_API
from ui_layer.validation import plane_type_ID_validation, email_validation, address_validation, phone_validation, role_validation, is_ssn_available, employee_gsm_change, employee_email_change, employee_validation
SPACER = "____________________________________________________________________________________________________________________________________________________________________________"
class ChangeEmployee:
    def __init__(self):
        self.__UI_API = UI_API()
        self.__employee_ID = ""
        self.__employee = []

    def change_employee_info(self):
        print("Change employee info:")
        id_checkker = False
        while id_checkker == False:
            self.__employee_ID = input("Employee ID: ")
            id_checkker = employee_validation(self.__employee_ID)
                
        self.__employee = self.__UI_API.get_personal_info(self.__employee_ID)
        change_employee = self.__employee[1]
        orgenallist = change_employee.copy()
        EMPLOYEE_ID = change_employee[0]
        SSN = change_employee[1]
        NAME = change_employee[2]
        ROLE = change_employee[3]
        LICENCE = change_employee[4]
        ADDRESS = change_employee[5]
        GSM = change_employee[6]
        EMAIL = change_employee[7]

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
            role_checkker = role_validation(ROLE)

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

        checkker = False
        while checkker == False:
            GSM = input("New GSM: ")
            if GSM != "":
                gsm_checkker = phone_validation(GSM)
                if gsm_checkker == True:
                    gsm_available = employee_gsm_change(self.__employee_ID, GSM)
                    if gsm_available == True:
                        checkker = True
            else:
                GSM = ORGINAL_GSM
                checkker = True

        chekker = False
        while chekker == False:
            EMAIL = input("New email: ")
            if EMAIL != "":
                email_chekker = email_validation(EMAIL)
                if email_chekker == True:
                    email_available = employee_email_change(self.__employee_ID, EMAIL)
                    if email_available == True:
                        chekker = True
            else:
                EMAIL = ORGINAL_EMAIL
                chekker = True

        checkker_list = [EMPLOYEE_ID, SSN, NAME, ROLE, LICENCE, ADDRESS, GSM, EMAIL]

        print(f"{EMPLOYEE_ID}    {SSN}    {NAME}    {ROLE}    {LICENCE}    {ADDRESS}    {GSM}    {EMAIL}")
        self.__UI_API.set_changes_for_existing_employee(checkker_list)
