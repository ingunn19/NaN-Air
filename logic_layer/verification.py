from logic_layer.validation_checker import ValidationChecker
from logic_layer.logic_parent import LogicParent

validate = ValidationChecker()

class CheckSeries(LogicParent):
    # Add new
    def check_add_employee(self, __employee_info):
        __ssn, __name, __role, __licence, __address, __phonenumber, __email = __employee_info
        if validate.check_if_ssn_exists(__ssn):
            return None
        if validate.check_if_phone_number_exists(__phonenumber):
            return None
        if validate.check_if_email_exists(__email):
            return None
        if validate.check_if_role_exists(__role):
            if __role.lower == "pilot":
                if validate.check_if_licence_exists(__licence):
                    return True
        return True

    def check_add_airplane(self, __airplane_info):
        __plane_insignia, __plane_type_id = __airplane_info
        if validate.check_if_insignia_exists(__plane_insignia):
            return None
        return True

    def check_add__worktrip(self, __worktrip_info):
        departFrom, arrivingAt, depart_time, aircraftID, pilot1, pilot2, flightAttendant1, flightAttendant2, flightAttendant3 = __worktrip_info
        if validate.check_if_destination_exists(arrivingAt) != True:
            return None
        if validate.check_depart_time_availability(depart_time) != True:
            return None
        if validate.check_if_insignia_exists(aircraftID):
            if validate.check_aircraft_availability(aircraftID, depart_time) != True:
                return None
        for employee in __worktrip_info[4: ]:
            if validate.check_if_employee_exists(employee) != True:
                return None
            if validate.check_employee_availability(employee, depart_time) != True:
                return None
        for employee in __worktrip_info[4: 6]:
            if validate.check_if_pilot(employee):
                if validate.check_pilot_licence(employee, aircraftID):
                    pass
                else:
                    return None
            else:
                return None
        for employee in __worktrip_info[6: ]:
            if validate.check_if_cabin_crew(employee):
                return True
            else:
                return None
        return None

    def check_add_destination(self, __destination_info):
        airportID, travel_time, destination, contact_name, contact_number = __destination_info
        if validate.check_if_destination_exists(airportID):
            if validate.check_if_contact_number_exists(contact_number):
                return None
            else:
                return True
        return None


    # Overview
    def check_view_employee_week(self, __employee_id, __week):
        if validate.check_if_employee_exists(__employee_id):
            if 1 <= int(__week) <= 52:
                return True
        return None

    def check_date(self, __date):
        try:
            datetime_date = datetime.datetime.strptime(date, '%Y, %m, %d')
            return True
        except:
            return False

    def check_week(self, __year, __week):
        if 1 <= int(__week) <= 52:
            return True
        else:
            return None

    # Edit existing
    def check_edit_employee(self, __employee_info):
        id, ssn, name, role, licence, email, address, gsm = __employee_info
        __all_crew = self.crew.read_file()
        if validate.check_if_role_exists(role):
            if validate.check_if_licence_exists(licence):
                for line in __all_crew:
                    if line[0] != id:
                        if email in line:
                            return None
                        if address in line:
                            return None
                        if gsm in line:
                            return None
                        return True
        return None

    def check_edit_airplane(self, __airplane_info):
        Plane_Insignia, plane_type_Id = __airplane_info
        if validate.check_if_plane_type_exists:
            if validate.check_if_insignia_exists(Plane_Insignia):
                return True

    def check_edit_crew(self, __flight_info):
        flight_id, departFrom, arrivingAt, depart_time, return_time, aircraftID, pilot1, pilot2, flightAttendant1, flightAttendant2, flightAttendant3 = __flight_info
        if validate.check_aircraft_availability(aircraftID, depart_time):
            for employee in __worktrip_info[6: ]:
                if validate.check_if_employee_exists(employee) != True:
                    return None
                if validate.check_employee_availability(employee, depart_time) != True:
                    return None

            for employee in __worktrip_info[6: 7]:
                if validate.check_if_pilot(employee):
                    if validate.check_pilot_licence(employee, aircraftID):
                        pass
                    else:
                        return None
                else:
                    return None

            for employee in __worktrip_info[7: ]:
                if validate.check_if_cabin_crew(employee):
                    return True
                else:
                    return None
        return None

    def check_edit_contact(self, __destination_info):
        airportID, travel_time, destination, contact_name, contact_number = __destination_info
        __all_destinations = self.destinations.read_file()
        for line in __all_destinations:
            if airportID != line[0]:
                if contact_number in line:
                    return None
                else:
                    return True
        return None