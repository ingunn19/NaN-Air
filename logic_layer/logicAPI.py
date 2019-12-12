# Overview
from logic_layer.overview_employees import EmployeeOverviewLogic
from logic_layer.overview_airplanes import PlaneOverviewLogic
from logic_layer.overview_destinations import DestinationOverviewLogic
from logic_layer.overview_worktrips import WorkTripOverviewLogic
# Add new or edit existing
from logic_layer.new_or_change_work_trip import AddNewOrChangeWorkTrip
from logic_layer.new_or_change_airplane import AddNewOrChangeAirplane
from logic_layer.new_or_change_destination import AddNewOrChangeDestinaion
from logic_layer.new_or_change_employee import AddNewOrChangeEmployee
# Error checker
from logic_layer import verify_dude
from logic_layer.validation_checker import ValitationChecker


class LogicAPI():
    def __init__(self):
        # Overview
        self.__employee_data = EmployeeOverviewLogic()
        self.__airplane_data = PlaneOverviewLogic()
        self.__destination_data = DestinationOverviewLogic()
        self.__worktrip_data = WorkTripOverviewLogic()
        # Add new or edit existing
        self.__add_or_edit_work_trip = AddNewOrChangeWorkTrip()
        self.__add_or_edit_employee = AddNewOrChangeEmployee()
        self.__add_or_edit_destination = AddNewOrChangeDestinaion()
        self.__add_or_edit_airplane = AddNewOrChangeAirplane()


    # Add new
    def set_employee(self, employee_info_list):
        # checker
            self.__add_or_edit_employee.add_new_employee(employee_info_list)

    def set_airplane(self, airplane_info_list):
        # checker
        self.__add_or_edit_airplane.add_new_airplane(airplane_info_list)

    def set_workTrip(self, trip_info_list):
        # chekcer
        self.__add_or_edit_work_trip.add_new_worktrip(trip_info_list)

    def set_destination(self, destination_info_list):
        # checker
        self.__add_or_edit_destination.add_new_destination(destination_info_list)


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

    def view_work_week(self, year, week):
        # is this week realchecker   ATH!!!
        return self.__worktrip_data.req_worktrips_of_the_week(year, week)

    def view_work_day(self, date):
        # is this date real checker   ATH!!!
        return self.__worktrip_data.req_worktrips_of_the_day(date)

    def view_all_destinations(self):
        return self.__destination_data.req_all_destinations()

    def view_single_destination(self, destination_id):
        __destination = self.__destination_data.req_one_destination(destination_id)
        if __destination:
            return __destination
        return None

    def view_all_planes(self):
        return self.__airplane_data.req_all_planes()

    def view_single_airplane(self, plane_id):
        __airplane = self.__airplane_data.req_single_plane(plane_id)
        if __airplane:
            return __airplane
        return None

    def view_state_of_planes(self, date):
        # checker
        return self.__airplane_data.req_state_of_planes(date)


    # Edit existing
    def edit_employee(self, employee_info):
        # checker
        self.__add_or_edit_employee.replace_info(employee_info)

    def edit_airplane(self, plane_info):
        # checker
        self.__add_or_edit_airplane.replace_info(plane_info)

    def edit_worktrip_crew(self, flight_info):
        # checker
        self.__add_or_edit_work_trip.replace_info(flight_info)

    def edit_destination_contact(self, destination_info):
        # checker
        self.__add_or_edit_destination.replace_info(destination_info)

    # Return checker
    def logic_checker(self):
        return ValitationChecker()