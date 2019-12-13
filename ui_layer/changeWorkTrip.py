from ui_layer.uiAPI import UI_API
from ui_layer.validation import destination_ID_validation, time_validation, plane_insignia_validation, pilot_validation, cabin_crew_validation, check_aircraft_validation, departure_validation,check_pilot_validation, pilot_licence_validation, check_employee_validation, attendant_validation
SPACER = "_______________________________________________________________________________________________________________________________________________________________________________"
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

        checkker = False
        while checkker == False:
            AIRCRAFT_ID = input("Aircraft insignia: ")
            if AIRCRAFT_ID == "":
                AIRCRAFT_ID = ORGINAL_AIRCRAFT_ID
                checkker = True
            plane_id_checkker = plane_insignia_validation(AIRCRAFT_ID)
            is_plane_ready = check_aircraft_validation(AIRCRAFT_ID, DEPARTURE)
            if plane_id_checkker == True:
                if is_plane_ready == True:
                    checkker = True

        checkker = False
        while checkker == False:
            PILOT1 = input("1. Pilot: ")
            if PILOT1 == "":
                PILOT1 = ORGINAL_PILOT1
                checkker = True
            is_it_a_pilot = check_pilot_validation(PILOT1)
            can_pilot_fly_this_plane = pilot_licence_validation(PILOT1, AIRCRAFT_ID)
            can_pilot_work = check_employee_validation(PILOT1, DEPARTURE)
            if is_it_a_pilot == True:
                if can_pilot_fly_this_plane == True:
                    if can_pilot_work == True:
                        checkker = True

        checkker = False
        while checkker == False:
            PILOT2 = input("2. Pilot: ")
            if PILOT2 == "":
                PILOT2 = ORGINAL_PILOT2
                checkker = True
            is_it_a_pilot = check_pilot_validation(PILOT2)
            can_pilot_fly_this_plane = pilot_licence_validation(PILOT2, AIRCRAFT_ID)
            can_pilot_work = check_employee_validation(PILOT2, DEPARTURE)
            if is_it_a_pilot == True:
                if can_pilot_fly_this_plane == True:
                    if can_pilot_work == True:
                        checkker = True

        checkker = False
        while checkker == False:
            CABINCREW1 = input("1. Cabin crew: ")
            if CABINCREW1 == "":
                CABINCREW1 = ORGINAL_CABINCREW1
                checkker = True
            is_it_cabin_crew = attendant_validation(CABINCREW1)
            can_cabin_crew_work = check_employee_validation(CABINCREW1, DEPARTURE)
            if is_it_cabin_crew == True:
                if can_cabin_crew_work == True:
                    checkker = True

        checkker = False
        while checkker == False:
            CABINCREW2 = input("2. Cabin crew: ")
            if CABINCREW2 == "":
                CABINCREW2 = ORGINAL_CABINCREW2
                checkker = True
            is_it_cabin_crew = attendant_validation(CABINCREW2)
            can_cabin_crew_work = check_employee_validation(CABINCREW2, DEPARTURE)
            if is_it_cabin_crew == True:
                if can_cabin_crew_work == True:
                    checkker = True

        checkker = False
        while checkker == False:
            CABINCREW3 = input("3. Cabin crew: ")
            if CABINCREW3 == "":
                CABINCREW3 = ORGINAL_CABINCREW3
                checkker = True
            is_it_cabin_crew = attendant_validation(CABINCREW3)
            can_cabin_crew_work = check_employee_validation(CABINCREW3, DEPARTURE)
            if is_it_cabin_crew == True:
                if can_cabin_crew_work == True:
                    checkker = True

        change_list = [FLIGHT_NUM, DESTINATION_FROM, ARRIVING_AT, DEPARTURE, RETURN, AIRCRAFT_ID, PILOT1, PILOT2, CABINCREW1, CABINCREW2, CABINCREW3]
        print(f"{FLIGHT_NUM}    {DESTINATION_FROM}    {ARRIVING_AT}    {DEPARTURE}    {RETURN}    {AIRCRAFT_ID}    {PILOT1}    {PILOT2}    {CABINCREW1}    {CABINCREW2}    {CABINCREW3}")
        self.__UI_API.set_changes_for_existing_worktrip(change_list)
