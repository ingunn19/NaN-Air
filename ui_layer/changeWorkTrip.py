from ui_layer.uiAPI import UI_API
from ui_layer.validation import destination_ID_validation, time_validation, plane_insignia_validation, pilot_validation, cabin_crew_validation, check_aircraft_validation, departure_validation,check_pilot_validation, pilot_licence_validation, check_employee_validation, attendant_validation
SPACER = "_____________________________________________"
class ChangeWorkTrip:
    def __init__(self):
        self.__UI_API = UI_API()
        self.flight_number = ""
        self.worktrip = []

    def change_workTrip(self):
        print("Change worktrip info:")
        self.flight_number = input("Flight number: ")
        self.worktrip = self.__UI_API.get_specific_worktrip(self.flight_number)
        change_worktrip = self.worktrip[1]
        original_list = self.worktrip[1].copy()

        FLIGHT_NUM = change_worktrip[0]
        DESTINATION_FROM = change_worktrip[1]
        ARRIVING_AT = change_worktrip[2]
        DEPARTURE = change_worktrip[3]
        RETURN = change_worktrip[4]
        AIRCRAFT_ID = change_worktrip[5]
        PILOT1 = change_worktrip[6]
        PILOT2 = change_worktrip[7]
        CABINCREW1 = change_worktrip[8]
        CABINCREW2 = change_worktrip[9]
        CABINCREW3 = change_worktrip[10]

        ORGINAL_FLIGHT_NUM = original_list[0]
        ORGINAL_DESTINATION_FROM = original_list[1]
        ORGINAL_ARRIVING_AT = original_list[2]
        ORGINAL_DEPARTURE = original_list[3]
        ORGINAL_RETURN = original_list[4]
        ORGINAL_AIRCRAFT_ID = original_list[5]
        ORGINAL_PILOT1 = original_list[6]
        ORGINAL_PILOT2 = original_list[7]
        ORGINAL_CABINCREW1 = original_list[8]
        ORGINAL_CABINCREW2 = original_list[9]
        ORGINAL_CABINCREW3 = original_list[10]

        arriving_at_checkker = False
        while arriving_at_checkker == False:
                ARRIVING_AT = input("Arriving at: ")
                if ARRIVING_AT == "":
                    ARRIVING_AT = ORGINAL_ARRIVING_AT
                arriving_at_checkker = destination_ID_validation(ARRIVING_AT) # það er ekki til neitt sem athugar formattið á input destination

        departure_checkker = False
        while departure_checkker == False:
            ARRIVING_AT = input("Departure time: ")
            if ARRIVING_AT == "":
                ARRIVING_AT = ORGINAL_ARRIVING_AT
            departure_checkker = time_validation(ARRIVING_AT)
            # er þessi brottfaratími laus?

        plane_id_checkker = False
        while plane_id_checkker == False:
            AIRCRAFT_ID = input("Aircraft insignia: ")
            if AIRCRAFT_ID == "":
                AIRCRAFT_ID = ORGINAL_AIRCRAFT_ID
            plane_id_checkker = plane_insignia_validation(AIRCRAFT_ID)
            # eigum við þessa flugvél til?
            # er flugvél laus?

        pilot_checkker1 = False
        while pilot_checkker1 == False:
            PILOT1 = input("Pilot1: ")
            if PILOT1 == "":
                PILOT1 = ORGINAL_PILOT1
            pilot_checkker1 = pilot_validation(PILOT1)
            # er þetta örugglega flugmaður?
            # er flugmaður með leifi á flugvélina?
            # er flugmaður laus?

        pilot_checkker2 = False
        while pilot_checkker2 == False:
            PILOT2 = input("Pilot2: ")
            if PILOT2 == "":
                PILOT2 = ORGINAL_PILOT2
            pilot_checkker2 = pilot_validation(PILOT1)
            # er þetta örugglega flugmaður?
            # er flugmaður með leifi á flugvélina?
            # er flugmaður laus?

        cabin_crew_checkker1 = False
        while cabin_crew_checkker1 == False:
            CABINCREW1 = input("Cabin crew1: ")
            if CABINCREW1 == "":
                CABINCREW1 = ORGINAL_CABINCREW1
            cabin_crew_checkker1 = cabin_crew_validation(CABINCREW1)
            # er þetta örugglega flugþjónn?
            # er flugþjónn laus?

        cabin_crew_checkker2 = False
        while cabin_crew_checkker2 == False:
            CABINCREW2 = input("Cabin crew2: ")
            if CABINCREW2 == "":
                CABINCREW2 = ORGINAL_CABINCREW2
            cabin_crew_checkker2 = cabin_crew_validation(CABINCREW2)
            # er þetta örugglega flugþjónn?
            # er flugþjónn laus?

        cabin_crew_checkker3 = False
        while cabin_crew_checkker3 == False:
            CABINCREW3 = input("Cabin crew3: ")
            if CABINCREW3 == "":
                CABINCREW3 = ORGINAL_CABINCREW3
            cabin_crew_checkker3 = cabin_crew_validation(CABINCREW3)
            # er þetta örugglega flugþjónn?
            # er flugþjónn laus?

        change_list = [FLIGHT_NUM, DESTINATION_FROM, ARRIVING_AT, DEPARTURE, RETURN, AIRCRAFT_ID, PILOT1, PILOT2, CABINCREW1, CABINCREW2, CABINCREW3]
        print(f"{FLIGHT_NUM}    {DESTINATION_FROM}    {ARRIVING_AT}    {DEPARTURE}    {RETURN}    {AIRCRAFT_ID}    {PILOT1}    {PILOT2}    {CABINCREW1}    {CABINCREW2}    {CABINCREW3}")
        self.__UI_API.set_changes_for_existing_worktrip(change_list)
        self.__UI_API.set_changes_for_existing_worktrip(change_list)
