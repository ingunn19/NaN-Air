from UI_API import UI_Api
SPACER = "_____________________________________________"
class New_WorkTrip:
    def __init__(self):
        self.__UI_API = UI_Api()
        self.__arrivingAt = ""
        self.__departure = ""
        self.__aircraftID = ""
        self.__pilot1 = ""
        self.__pilot2 = ""
        self.__flightAttendant1 = ""
        self.__flightAttendant2 = ""
        self.__flightAttendant3 = ""
    def Initialize_WorkTrip(self):
        print("New WorkTrip")
        self.__arrivingAt = input("Destination: ")
        #self.__departure = inpit("")
        self.__aircraftID = input("Aircraft ID: ")
        self.__pilot1 = input("1. Pilot ID: ")
        self.__pilot2 = input("2. Pilot ID: ")
        self.__flightAttendant1 = input("1. Flight attendant ID: ")
        self.__flightAttendant2 = input("2. Flight attendant ID: ")
        self.__flightAttendant3 = input("3. Flight attendant ID: ")
        print(SPACER)
        self.__UI_API.set_WorkTrip(self.__arrivingAt, self.__aircraftID, self.__pilot1, self.__pilot2, self.__flightAttendant1, self.__flightAttendant2, self.__flightAttendant3)