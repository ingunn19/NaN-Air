from logic_layer.validation_checker import ValidationChecker
from logic_layer import input_checker

validate = ValidationChecker()

class CheckSeries():
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
        if validate.check_if_destination_exists(arrivingAt):
            pass
        if validate.check_depart_time_availability(depart_time):
            pass
        if validate.check_if_insignia_exists(aircraftID):
            if validate.check_aircraft_availability(aircraftID, depart_time):
                pass
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
        pass

    def check_edit_airplane(self, __airplane_info):
        pass

    def check_edit_worktrip(self, __worktrip_info):
        pass

    def check_edit_contact(self, __destination_info):
        pass