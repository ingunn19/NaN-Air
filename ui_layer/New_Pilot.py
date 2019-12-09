from UI_API import UI_Api
SPACER = "_____________________________________________"
class New_Pilot:
    def __init__(self):
        self.__UI_API = UI_Api()
        self.__ssn = ""
        self.__name = ""
        self.__role = ""
        self.__licence = ""
        self.__address = ""
        self.__gsm = ""

    def create_pilot(self):
        print("New Pilot: ")
        self.__ssn = input("SSN: ")
        self.__name = input("Full name: ") # Spurning að gera þetta að lista og setja i hann fyrir og eftirnafn
        #á eða biðja um tvö input eitt fyrir fornafn og eitt fyrir eftirnafn
        self.__role = input("Role: ")
        self.__licence = input("Licence: ")
        self.__address = input("Address: ")
        self.__gsm = input("GSM: ")
        # Villuchekka
        # Hér væri gott að prenta út nýan pilot
        print(SPACER)
        self.__UI_API.set_pilot(self.__ssn, self.__name, self.__role, self.__licence, self.__address, self.__gsm)