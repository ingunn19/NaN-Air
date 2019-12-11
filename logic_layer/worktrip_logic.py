from data_layer.dataLayer import DataAPI
from models.work_trip import WorkTrip
from datetime import date, timedelta, datetime
from employee_overview import EmployeeOverviewLogic
from clock import Clock
from logic_parent import LogicParent

class WorkTripLogic(LogicParent):
    def check_employee_availability(self, employee_id, day):
        """Takes in employee_id and time of day, checks if employee is busy that day
            returns None if busy, True if available"""
        __flight_list = self.__flight_records.read_file()
        __employee_shifts = []
        for line in __flight_list:
            if day == (line[3][:10] or line[4][:10]):
                if employee_id in line:
                    return None
        return True

    def check_aircraft_availability(self, plane_insignia, depart_time):
        """Takes in a plane insignia and departure time, checks if at least and hour
            has passed from it's last flight to the new departure time
            returns None if aircraft not ready, True if available"""
        plane_trips = []
        __flight_records = self.__flight_records.read_file()
        for line in __flight_records:
            if plane_insignia in line:
                plane_trips.append(line)
        most_recent_trip = plane_trips[-1][4]
        depart_time = Clock(depart_time)
        time_diff = depart_time.calculate_time_diff(most_recent_trip)
        if time_diff >= 1:
            return True
        return None

    def check_pilot_licence(self, employee_id, plane_insignia):
        """Takes in employee_id and time of aircraft type, checks if pilot 
            has the needed licence for that aircraft
            returns None if no licence, True if it checks out"""
        pilotData = EmployeeOverviewLogic()
        classObject = WorkTripLogic()
        plane_type = classObject.get_aircraft_type(plane_insignia)
        employee_list = pilotData.req_overview_pilots()
        for line in employee_list:
            if employee_id in line:
                if plane_type in line:
                    return True
        return None

    def check_timeslot_availability(self, time_slot):
        """Takes in a time and date, reads the flight records
            and checks if the time and date are not in use
            return None if timeslot is busy, True if timeslot is available"""
        flight_list = self.__flight_records.read_file()
        for line in flight_list:
            if time_slot in line:
                return True
        return None

    def check_destination(self, destination):
        """Checks if destination is registered
            returns True if registered, None if not"""
        destination_to_check = destination
        destination_list = self.__destinations.read_file()
        for line in destination_list:
            if destination_to_check in line:
                return True
        return None

    def get_aircraft_type(self, plane_insignia):
        """Takes in plane insignia and returns aircraft type ID"""
        planes_list = self.__aircraft.read_file()
        for line in planes_list:
            if plane_insignia in line:
                return planes_list[planes_list.index(line)][1]

    def get_new_flight_id(self, new_trip):
        """Takes in information list to register a new trip,
            reads the flight records file, inserts the new flight chronologically
            and generates a flight ID for the new trip and adjusts any shifted flights.
            Saves the edited file and returns the new trip's flight ID"""
        __FLIGHT_ID = 0
        __DEPARTURE = 3
        __flight_record_list = self.__flight_records.read_file()

        # Pop header, append new trip and sort by departure time
        __header = __flight_record_list[0]
        __flight_record_list.pop(0)
        __flight_record_list.append(new_trip)
        __flight_record_list.sort(key=lambda index: index[__DEPARTURE])

        # Gather all departure times
        __takeoff_time = [line[__DEPARTURE] for line in __flight_record_list]
        # Get the flight id of newly added trip
        __new_trip_index = __takeoff_time.index(new_trip[__DEPARTURE])
        __new_id = str(int(__flight_record_list[__new_trip_index - 1][__FLIGHT_ID]) + 1)
        __flight_record_list[__new_trip_index][__FLIGHT_ID] = __new_id

        # Adjust flight id of all later trip if needed
        if __new_trip_index != len(__takeoff_time) - 1:
            for index in range(__new_trip_index + 1, len(__flight_record_list)):
                __flight_record_list[index][__FLIGHT_ID] = str(int(__flight_record_list[index - 1][__FLIGHT_ID]) + 1)

        # Return header to top and save updated records to file
        __flight_record_list.insert(0, __header)
        self.__flight_records.write_file(__flight_record_list)
        return __new_id

    def get_travel_time(self, destination):
        """Takes in a destination, reads destination information file
            returns the travel time to destination"""
        destination_list = self.__destinations.read_file()
        for line in destination_list:
            if destination in line:
                return line[2]
        return None

    def get_return_time(self, destination, depart_time):
        """Takes in a destination and departure time
            calculates the return time for the trip
            and returns it"""
        classObject = WorkTripLogic()
        time_to_destination = int(classObject.get_travel_time(destination))
        travel_time = (time_to_destination * 2) + 1
        depart_time = Clock(depart_time)
        return_time = depart_time.calculate_return_time(travel_time)
        return return_time

    def new_worktrip(self, flight_info_list):
        """Takes in a list of information to register a new worktrip, 
            generates a return time, flight id, feeds the information into a model and returns it"""
        classObject = WorkTripLogic()
        depart_from, arrive_at, depart_time, plane_insignia, pilot1, pilot2, fa1, fa2, fa3 = [i for i in flight_info_list]
        return_time = classObject.get_return_time(arrive_at, depart_time)
        flight_info_list.insert(0, '')
        flight_info_list.insert(4, return_time)
        flight_id = classObject.get_new_flight_id(flight_info_list)
        return WorkTrip(flight_id, depart_from, arrive_at, depart_time, return_time, plane_insignia, pilot1, pilot2, fa1, fa2, fa3)