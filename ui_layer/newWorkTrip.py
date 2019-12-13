from ui_layer.uiAPI import UI_API
from ui_layer.validation import destination_ID_validation, plane_insignia_validation, check_aircraft_validation, departure_validation,check_pilot_validation, pilot_licence_validation, check_employee_validation, attendant_validation, aircraft_validation, employee_validation
SPACER = "____________________________________________________________________________________________________________________________________________________________________________"

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
            arriving_at_checkker = destination_ID_validation(self.__arrivingAt) # það er ekki til neitt sem checkar input, Þetta virkar samt því þetta þarf að vera selgið inn rétt il þess að komast útir loopuni

        checkker = False
        while checkker == False:
            self.__departure = input("Departure time: yyyy-mm-ddThh:mm:ss \n")
            is_airport_in_use = departure_validation(self.__departure)
            if is_airport_in_use == True:
                checkker = True

        checkker = False
        while checkker == False:
            self.__aircraftID = input("Aircraft insignia: ")
            if self.__aircraftID != "":
                plane_id_checkker = plane_insignia_validation(self.__aircraftID)
                if plane_id_checkker == True:
                    dose_this_plane_exist = aircraft_validation(self.__aircraftID)
                    if dose_this_plane_exist == True:
                        is_plane_ready = check_aircraft_validation(self.__aircraftID, self.__departure)
                        if is_plane_ready == True:
                            checkker = True
            else:
                checkker = True

        checkker = False
        while checkker == False:
            self.__pilot1 = input("1. Pilot ID: ")
            if self.__pilot1 != "":
                is_it_a_employee = employee_validation(self.__pilot1)
                if is_it_a_employee == True:
                    is_it_a_pilot = check_pilot_validation(self.__pilot1)
                    if is_it_a_pilot == True:
                        can_pilot_fly_this_plane = pilot_licence_validation(self.__pilot1, self.__aircraftID)
                        if can_pilot_fly_this_plane == True:
                            can_pilot_work = check_employee_validation(self.__pilot1, self.__departure)
                            if can_pilot_work == True:
                                checkker = True
            else:
                checkker = True

        checkker1 = False
        while checkker1 == False:
            self.__pilot2 = input("2. Pilot ID: ")
            if self.__pilot2 != "":
                is_it_a_employee = employee_validation(self.__pilot2)
                if is_it_a_employee == True:
                    is_it_a_pilot = check_pilot_validation(self.__pilot2)
                    if is_it_a_pilot == True:
                        can_pilot_fly_this_plane = pilot_licence_validation(self.__pilot2, self.__aircraftID)
                        if can_pilot_fly_this_plane == True:
                            can_pilot_work = check_employee_validation(self.__pilot2, self.__departure)
                            if can_pilot_work == True:
                                checkker1 = True
            else:
                checkker1 = True

            checkker = False
            while checkker == False:
                self.__flightAttendant1 = input("1. Flight attendant ID: ")
                if self.__flightAttendant1 != "":
                    is_it_a_employee = employee_validation(self.__flightAttendant1)
                    if is_it_a_employee == True:
                        is_it_cabin_crew = attendant_validation(self.__flightAttendant1)
                        if is_it_cabin_crew == True:
                            can_cabin_crew_work = check_employee_validation(self.__flightAttendant1, self.__departure)
                            if can_cabin_crew_work == True:
                                checkker = True
                else:
                    checkker = True

            checkker = False
            while checkker == False:
                self.__flightAttendant2 = input("2. Flight attendant ID: ")
                if self.__flightAttendant2 != "":
                    is_it_a_employee = employee_validation(self.__flightAttendant2)
                    if is_it_a_employee == True:
                        is_it_cabin_crew = attendant_validation(self.__flightAttendant2)
                        if is_it_cabin_crew == True:
                            can_cabin_crew_work = check_employee_validation(self.__flightAttendant2, self.__departure)
                            if can_cabin_crew_work == True:
                                checkker = True
                else:
                    checkker = True

            checkker = False
            while checkker == False:
                self.__flightAttendant3 = input("3. Flight attendant ID: ")
                if self.__flightAttendant3 != "":
                    is_it_a_employee = employee_validation(self.__flightAttendant3)
                    if is_it_a_employee == True:
                        is_it_cabin_crew = attendant_validation(self.__flightAttendant3)
                        if is_it_cabin_crew == True:
                            can_cabin_crew_work = check_employee_validation(self.__flightAttendant3, self.__departure)
                            if can_cabin_crew_work == True:
                                checkker = True
                else:
                    checkker = True

        print(SPACER)
        self.__UI_API.set_WorkTrip(self.__arrivingAt, self.__departure, self.__aircraftID, self.__pilot1, self.__pilot2, self.__flightAttendant1, self.__flightAttendant2, self.__flightAttendant3)