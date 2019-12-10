from ui_layer.uiAPI import UI_API

SPACER = "_____________________________________________"

class New_CabinCrew:
    def __init__(self):
        self.__UI_API = UI_API()
        self.__ssn = ""
        self.__name = ""
        self.__role = ""
        self.__address = ""
        self.__gsm = ""

    def create_Cabin_crew(self):
        print("New Pilot: ")
        self.__ssn = input("SSN: ")
        self.__name = input("Full name: ") # Spurning að gera þetta að lista og setja i hann fyrir og eftirnafn
        #a eða biðja um tvö input eitt fyrir fornafn og eitt fyrir eftirnafn
        self.__role = input("Role: ")
        self.__address = input("Address: ")
        self.__gsm = input("GSM: ")
        print(SPACER)
        #Villuchekka
        #Hér væri flott að prenta út ýa fugmannin
        self.__UI_API.set_Cabin_crew(self.__ssn, self.__name, self.__role, self.__address, self.__gsm)