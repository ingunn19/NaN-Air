from logic_layer.logic_parent import LogicParent
from logic_layer.overview_employees import EmployeeOverviewLogic
from logic_layer.clock import Clock


class ValitationChecker(LogicParent):
    # Check if exists
    def check_if_ssn_exists(self, __ssn):
        """Takes in ssn, checks if it already exists in logs
            returns True if it exists, None if not"""
        __all_employee_list = self.crew.read_file()
        for line in __all_employee_list:
            if __ssn in line:
                return True
        return None

    def check_if_employee_exists(self, __employee_id):
        """Takes in employee ID, checks if it already exists in logs
            returns True if it exists, None if not"""
        __all_employee_list = self.crew.read_file()
        for line in __all_employee_list:
            if __employee_id in line:
                return True
        return None

    def check_if_plane_type_exists(self, __plane_type):
        """Takes in plane type, checks if it already exists in logs
            returns True if it exists, None if not"""
        all_aircrafts = self.aircraft.read_file()
        for line in all_aircrafts:
            if __plane_type in line:
                return True
        return None

    def check_if_insignia_exists(self, __insignia):
        """Takes in plane insignia, checks if it already exists in logs
            returns True if it exists, None if not"""
        all_aircrafts = self.aircraft.read_file()
        for line in all_aircrafts:
            if __insignia in line:
                return True
        return None

    def check_if_destination_exists(self, __destination):
        """Checks if destination is registered
            returns True if registered, None if not"""
        destination_list = self.destinations.read_file()
        for line in destination_list:
            if __destination in line:
                return True
        return None

    def check_if_contact_number_exists(self, __contact_number):
        """Takes in contact number, checks if it already exists in logs
            returns True if it exists, None if not"""
        all_destinations = self.destinations.read_file()
        for line in all_destinations:
            if __contact_number in line:
                return True
        return None

    def check_if_role_exists(self, __role):
        """Takes in role and checks if it exists
            returns True if it does, None if it does not"""
        __all_employee_list = self.crew.read_file()
        for line in __all_employee_list:
            if __role in line:
                return True
        return None

    def check_if_pilot(self, __id):
        """Takes in employee ID, checks if employee is a pilot
            returns True if they are, None if they're not"""
        __all_employee_list = self.crew.read_file()
        for line in __all_employee_list:
            if __id in line:
                __employee_info = line
        if (__employee_info[3]).lower() == "pilot":
            return True
        return None

    def check_if_cabin_crew(self, __id):
        """Takes in employee ID, checks if employee is cabin crew
            returns True if they are, None if they're not"""
        __all_employee_list = self.crew.read_file()
        for line in __all_employee_list:
            if __id in line:
                __employee_info = line
        if (__employee_info[3]).lower() == "cabincrew":
            return True
        return None

    def check_if_licence_exists(self, __licence):
        """Takes in a pilot's licence, checks if the licence has a corresponding airplane
            returns True if it does, None if it does not"""
        __airplane_list = self.aircraft.read_file()
        for line in __airplane_list:
            if __licence in line:
                return True
        return None

    def check_if_phone_number_exists(self, __phonenumber):
        """Takes in phone number, checks if it already exists in logs
            returns True if it exists, None if not"""
        __all_employee_list = self.crew.read_file()
        for line in __all_employee_list:
            if __phonenumber in line:
                return True
        return None

    def check_if_email_exists(self, email):
        """Takes in email, checks if it already exists in logs
            returns True if it exists, None if not"""
        __all_employee_list = self.crew.read_file()
        for line in __all_employee_list:
            if email in line:
                return True
        return None


    # Check for availability
    def check_pilot_licence(self, __employee_id, __plane_insignia):
        """Takes in employee_id and time of aircraft type, checks if pilot 
            has the needed licence for that aircraft
            returns None if no licence, True if it checks out"""
        pilotData = EmployeeOverviewLogic()
        __employee_list = pilotData.req_overview_pilots()
        __planes_list = self.aircraft.read_file()

        for line in __planes_list:
            if __plane_insignia in line:
                __plane_type = __planes_list[__planes_list.index(line)][1]

        for line in __employee_list:
            if __employee_id in line:
                if __plane_type in line:
                    return True
        return None

    def check_employee_availability(self, __employee_id, __day):
        """Takes in employee_id and time of day, checks if employee is busy that day
            returns None if busy, True if available"""
        __flight_list = self.flight_records.read_file()
        __employee_shifts = []
        for line in __flight_list:
            if __day == (line[3][:10] or line[4][:10]):
                if __employee_id in line:
                    return None
        return True

    def check_aircraft_availability(self, __plane_insignia, __depart_time):
        """Takes in a plane insignia and departure time, checks if at least and hour
            has passed from it's last flight to the new departure time
            returns None if aircraft not ready, True if available"""
        __plane_trips = []
        __flight_records = self.flight_records.read_file()
        for line in __flight_records:
            if __plane_insignia in line:
                __plane_trips.append(line)
        __most_recent_trip = __plane_trips[-1][4]
        __depart_time = Clock(__depart_time)
        __time_diff = __depart_time.calculate_time_diff(__most_recent_trip)
        if __time_diff >= 1:
            return True
        return None

    def check_depart_time_availability(self, __time_slot):
        """Takes in a time and date, reads the flight records
            and checks if the time and date are not in use
            return None if timeslot is busy, True if timeslot is available"""
        __flight_list = self.flight_records.read_file()
        for line in __flight_list:
            if __time_slot in line:
                return None
        return True