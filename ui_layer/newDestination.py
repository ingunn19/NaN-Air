from ui_layer.uiAPI import UI_API

SPACER = "_____________________________________________"

class New_Destination:
    def __init__(self):
        self.__UI_API = UI_API()
        self.__airportID = ""
        self.__destination	 = ""
        self.__contact_name = ""
        self.__contact_number = ""

    def Initialize_Destination(self):
        print("New Destination")
        self.__airportID = input("Airport ID: ")
        #Flight time to destination vantar
        self.__destination = input("Destination: ")
        self.__contact_name = input("Emergency contact: ")
        self.__contact_number = input("Emergency number: ")
        print(SPACER)
        self.__UI_API.set_Destination(self.__airportID, self.__destination, self.__contact_name, self.__contact_number)