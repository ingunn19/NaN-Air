from ui_layer.uiAPI import UI_API
from ui_layer.validation import destination_ID_validation, time_validation, plane_insignia_validation, pilot_validation, cabin_crew_validation
SPACER = "_____________________________________________"

class New_WorkTrip:
    def __init__(self):
        self.__UI_API = UI_API()
        self.__arrivingAt = ""
        self.__departure = ""
        self.__aircraftID = ""
        self.__pilot1 = ""
        self.__pilot2 = ""
        self.__flightAttendant1 = ""
        self.__flightAttendant2 = ""
        self.__flightAttendant3 = ""

        # ARRIVING_AT
        # DEPARTURE
        # AIRCRAFT_ID
        # PILOT1
        # PILOT2
        # CABINCREW1
        # CABINCREW2
        # CABINCREW3

    def Initialize_WorkTrip(self):
        print("New WorkTrip")
        arriving_at_checkker = False
        while arriving_at_checkker == False:
            self.__arrivingAt = input("Destination: ")
            arriving_at_checkker = destination_ID_validation(self.__arrivingAt) # það er ekki til neitt sem checkar input

        departure_checkker = False
        while departure_checkker == False:
            self.__departure = input("Departure time: ")
            departure_checkker = time_validation(self.__departure)
            # er brottfaratími laus?

        plane_id_checkker = False
        while plane_id_checkker == False:
            self.__aircraftID = input("Aircraft insignia: ")
            plane_id_checkker = plane_insignia_validation(self.__aircraftID)
            # er flugvél laus?

        pilot_checkker1 = False
        while pilot_checkker1 == False:
            self.__pilot1 = input("1. Pilot ID: ")
            pilot_checkker1 = pilot_validation(self.__pilot1)
            # er þetta örugglega flugmaður?
            # er flugmaður með leifi á flugvélina?
            # er flugmaður laus?

        pilot_checkker2 = False
        while pilot_checkker2 == False:
            self.__pilot2 = input("2. Pilot ID: ")
            pilot_checkker2 = pilot_validation(self.__pilot2)
            # er þetta örugglega flugmaður?
            # er flugmaður með leifi á flugvélina?
            # er flugmaður laus?

            cabin_crew_checkker = False
            while cabin_crew_checkker == False:
                self.__flightAttendant1 = input("1. Flight attendant ID: ")
                cabin_crew_checkker = cabin_crew_validation(self.__flightAttendant1)
                # er þetta örugglega flugþjónn
                # er flugþjónn laus

            cabin_crew_checkker = False
            while cabin_crew_checkker == False:
                self.__flightAttendant2 = input("2. Flight attendant ID: ")
                cabin_crew_checkker = cabin_crew_validation(self.__flightAttendant2)
                # er þetta örugglega flugþjónn
                # er flugþjónn laus

            cabin_crew_checkker = False
            while cabin_crew_checkker == False:
                self.__flightAttendant3 = input("3. Flight attendant ID: ")
                cabin_crew_checkker = cabin_crew_validation(self.__flightAttendant3)
                # er þetta örugglega flugþjónn
                # er flugþjónn laus

        print(SPACER)
        self.__UI_API.set_WorkTrip(self.__arrivingAt, self.__departure, self.__aircraftID, self.__pilot1, self.__pilot2, self.__flightAttendant1, self.__flightAttendant2, self.__flightAttendant3)