from models.work_trip import WorkTrip
from datetime import date, timedelta, datetime
from logic_layer.overview_employees import EmployeeOverviewLogic
from logic_layer.clock import Clock
from logic_layer.logic_parent import LogicParent

class AddNewOrChangeWorkTrip(LogicParent):
    def get_aircraft_type(self, plane_insignia):
        """Takes in plane insignia and returns aircraft type ID"""
        planes_list = self.aircraft.read_file()
        for line in planes_list:
            if plane_insignia in line:
                return planes_list[planes_list.index(line)][1]

    def get_travel_time(self, destination):
        """Takes in a destination, reads destination information file
            returns the travel time to destination"""
        destination_list = self.destinations.read_file()
        for line in destination_list:
            if destination in line:
                return line[2]
        return None

    def get_return_time(self, destination, depart_time):
        """Takes in a destination and departure time
            calculates the return time for the trip
            and returns it"""
        classObject = AddNewOrChangeWorkTrip()
        time_to_destination = int(classObject.get_travel_time(destination))
        travel_time = (time_to_destination * 2) + 1
        depart_time = Clock(depart_time)
        return_time = depart_time.calculate_return_time(travel_time)
        return return_time

    def register_trip(self, new_trip):
        """Takes in information list to register a new trip,
            reads the flight records file, inserts the new flight chronologically
            and generates a flight ID for the new trip and adjusts any shifted flights.
            Saves the edited file and returns the new trip's flight ID"""
        __FLIGHT_ID = 0
        __DEPARTURE = 3
        __flight_record_list = self.flight_records.read_file()

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
        self.flight_records.write_file(__flight_record_list)

    # Adding
    def add_new_worktrip(self, flight_info_list):
        """Takes in a list of information to register a new worktrip, 
            generates a return time, flight id, feeds the information into a model and returns it"""
        classObject = AddNewOrChangeWorkTrip()
        arrive_at = flight_info_list[1]
        depart_time = flight_info_list[2]
        return_time = classObject.get_return_time(arrive_at, depart_time)
        flight_info_list.insert(0, '')
        flight_info_list.insert(4, return_time)
        classObject.register_trip(flight_info_list)

    # Changing
    def replace_info(self, flight_info_list):
        __flight_record_list = self.flight_records.read_file()
        __flight_id = flight_info_list[0]
        for line in __flight_record_list:
            if __flight_id == line[0]:
                __flight_record_list[__flight_record_list.index(line)] = flight_info_list
                break
        self.flight_records.write_file(__flight_record_list)