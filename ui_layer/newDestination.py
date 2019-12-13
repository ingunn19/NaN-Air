from ui_layer.uiAPI import UI_API
from ui_layer.validation import destination_ID_validation, time_validation, contact_number
SPACER = "_______________________________________________________________________________________________________________________________________"

class New_Destination:
    def __init__(self):
        self.__UI_API = UI_API()
        self.__airportID = ""
        self.__travel_time = ""
        self.__destination = ""
        self.__contact_name = ""
        self.__contact_number = ""

    #ID
    #DESTIONATION
    #TRAVEL_TIME
    #CONTACT_NAME
    #CONTACT_NUMBER


    def Initialize_Destination(self):
        print("New Destination")
        airportID_checkker = False
        while airportID_checkker == False:
            self.__airportID = input("Airport ID: ")
            airportID_checkker = True

        travel_time_checkker = False
        while travel_time_checkker == False:
            try:
                self.__travel_time = int(input("Travel time: "))
            except ValueError:
                print("ERROR! Not a integer")
            travel_time_checkker = time_validation(self.__travel_time)

        self.__destination = input("Destination: ")

        self.__contact_name = input("Emergency contact: ")

        contact_number_checkker = False
        while contact_number_checkker == False:
            self.__contact_number = input("Emergency number: ")
            contact_number_checkker = contact_number(self.__contact_number)

        print(f"{self.__airportID}    {self.__travel_time}    {self.__destination}    {self.__contact_name}    {self.__contact_number}")
        print(SPACER)
        self.__UI_API.set_Destination(self.__airportID, str(self.__travel_time), self.__destination, self.__contact_name, self.__contact_number)