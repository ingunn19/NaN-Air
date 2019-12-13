from ui_layer.uiAPI import UI_API
from ui_layer.validation import destination_ID_validation, contact_number_change
SPACER = "____________________________________________________________________________________________________________________________________________________________________________"
class ChangeDestination:
    def __init__(self):
        self.__UI_API = UI_API()
        self.destination_name = ""
        self.destination = []
    def change_destination(self):
        print("Change destination info:")
        destination_checkker = False
        while destination_checkker == False:
            self.destination_name = input("Destination ID: ")
            destination_checkker = destination_ID_validation(self.destination_name)

        self.destination = self.__UI_API.get_specific_destination(self.destination_name)
        originallist = self.destination.copy()
        ID = self.destination[0]
        DESTIONATION = self.destination[1]
        TRAVEL_TIME = self.destination[2]
        CONTACT_NAME = self.destination[3]
        CONTACT_NUMBER = self.destination[4]

        ORIGINAL_ID = originallist[0]
        ORIGINAL_DESTIONATION = originallist[1]
        ORIGINAL_TRAVEL_TIME = originallist[2]
        ORIGINAL_CONTACT_NAME = originallist[3]
        ORIGINAL_CONTACT_NUMBER = originallist[4]


        CONTACT_NAME = input("New emergency contact name: ")
        if CONTACT_NAME == "":
            CONTACT_NAME = ORIGINAL_CONTACT_NAME


        contact_number_checkker = False
        while contact_number_checkker == False:
            CONTACT_NUMBER = input("New emergency contact GSM: ")
            if CONTACT_NUMBER == "":
                CONTACT_NUMBER = ORIGINAL_CONTACT_NUMBER
            contact_number_checkker = contact_number_change(self.destination_name, CONTACT_NUMBER)

        change_list = [ID, DESTIONATION, TRAVEL_TIME, CONTACT_NAME, CONTACT_NUMBER]

        print(f"{ID}    {DESTIONATION}    {TRAVEL_TIME}    {CONTACT_NAME}    {CONTACT_NUMBER}")
        self.__UI_API.set_changes_for_existing_destination(change_list)
