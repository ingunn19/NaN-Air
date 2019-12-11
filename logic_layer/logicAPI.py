# Overview
from employee_overview import EmployeeOverviewLogic
from airplane_overview import PlaneOverviewLogic
from destination_overview import DestinationOverviewLogic
from worktrip_overview import WorkTripOverviewLogic
# Add new
from add_new_worktrip import New_WorkTrip
# Edit existing


class LogicAPI():
    def __init__(self):
        # Overview
        self.__employee_data = EmployeeOverviewLogic()
        self.__airplane_data = PlaneOverviewLogic()
        self.__destination_data = DestinationOverviewLogic()
        self.__worktrip_data = WorkTripOverviewLogic()
        # Add new
        self.__add_work_trip = New_WorkTrip()
        # Edit existing


    #add new
    def set_employee(self, employee_info_list):
        #code
        pass

    def set_airplane(self, airplane_info_list):
        #code
        pass

    def set_workTrip(self, trip_info_list):
        depart_from, arrive_at, depart_time, plane_insignia, pilot1, pilot2, fa1, fa2, fa3 = [i for i in trip_info_list]
        if self.__add_work_trip.check_timeslot_availability(depart_time) == None:
            return None
        if self.__add_work_trip.check_destination(arrive_at) == None:
            return None
        if self.__add_work_trip.get_aircraft_type(plane_insignia) == None:
            return None
        if self.__add_work_trip.check_aircraft_availability(plane_insignia, depart_time) == None:
            return None
        for employee in trip_info_list[4: ]:
            if self.__add_work_trip.check_employee_availability(employee, depart_time) == None:
                return None
        for pilot in trip_info_list[4: 6]:
            if self.__add_work_trip.check_pilot_licence(pilot, plane_insignia) == None:
                return None
        self.__add_work_trip.new_worktrip(trip_info_list)

    def set_destination(self, destination_info_list):
        # code
        pass


    # Overview
    def view_all_employees(self):
        return self.__employee_data.req_overview_allemployees()

    def view_employee_details(self, employee_id):
        if self.__employee_data.req_employee_personal_details(employee_id):
            return self.__employee_data.req_employee_personal_details(employee_id)
        return None
    
    def view_employee_work_week(self, employee_id, year, week):
        if 1 > int(week)  or int(week) > 52:
            return None
        if self.__employee_data.req_employee_personal_details(employee_id):
            return self.__employee_data.req_employee_work_week_overview(employee_id, year, week)
        return None

    def view_all_pilots(self):
        return self.__employee_data.req_overview_pilots()

    def view_all_cabin_crew(self):
        return self.__employee_data.req_overview_flightattendants()

    def get_name(self):
        """Hvað er þetta?"""
        # code
        pass

    def view_working_today(self, date):
        # is this date real checker     ATH!!!
        return self.__employee_data.req_all_employees_with_task(date)

    def view_available_today(self, date):
        # is this date real checker     ATH!!!
        return self.__employee_data.req_all_employees_not_with_task(date)

    def view_all_with_licence_on_model(self, airplane_type):
        if airplane_type in self.__airplane_data.req_all_planes():
            return self.__employee_data.req_all_pilots_with_licence_on_a_given_plane(airplane_type)
        return None
    
    def view_all_pilot_licences(self):
        return self.__employee_data.req_all_pilot_licences()

    def view_all_work_trips(self):
        return self.__worktrip_data.req_all_worktrips()

    def view_single_worktrip(self, flight_id):
        worktrip = self.__worktrip_data.req_single_worktrip(flight_id)
        if worktrip:
            return worktrip
        return None

    def view_work_week(self, week_year_maybe):
        year, week = week_year_maybe.split()
        # is this week realchecker   ATH!!!
        return self.__worktrip_data.req_worktrips_of_the_week(year, week)

    def view_work_day(self, date):
        # is this date real checker   ATH!!!
        return self.__worktrip_data.req_worktrips_of_the_day

    def view_all_destinations(self):
        return self.__destination_data.req_all_destinations

    def view_single_destination(self, destination_id):
        __destination = self.__destination_data.req_one_destination(destination_id)
        if __destination:
            return __destination
        return None

    def view_all_planes(self):
        return self.__airplane_data.req_all_planes

    def view_one_airplane(self, plane_id):
        __airplane = self.__airplane_data.req_single_plane
        if __airplane:
            return __airplane
        return None

    def view_state_of_planes(self, date):
        # is this date real checker   ATH!!!
        return self.__airplane_data.req_state_of_planes(date)


    # Edit existing
    def edit_employee(self, employee):
        # code
        pass

    def edit_airplane(self, plane_id):
        # code
        pass

    def edit_worktrip_crew(self, flight_id):
        # code
        pass

    def edit_destination_contact(self, destination_id):
        # code
        pass