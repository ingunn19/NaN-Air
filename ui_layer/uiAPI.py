from logic_layer.logicAPI import LogicAPI
from datetime import date, timedelta, datetime

SPACER = "_____________________________________________"
logic_API = LogicAPI()

class UI_API:
    # Set new
    def set_pilot(self, ssn, name, role, licence, email,  address, gsm):
        set_pilot_list = [ssn, name, role, licence, email, address, gsm]
        logic_API.set_employee(set_pilot_list)

    def set_airplane(self, Plane_Insignia, plane_type_Id):
        set_airplane_list = [Plane_Insignia, plane_type_Id]
        print(set_airplane_list)
        logic_API.set_airplane(set_airplane_list)

    def set_Cabin_crew(self, ssn, name, role, address, gsm, email):
        set_cabin_crew_list = [ssn, name, role, "N/A", address, gsm, email]
        logic_API.set_employee(set_cabin_crew_list)

    # Vantar að taka inn departure time ATH!!!
    def set_WorkTrip(self, arrivingAt, depart_time, aircraftID, pilot1, pilot2, flightAttendant1, flightAttendant2, flightAttendant3):
        set_workTrip_list = ['RKV', arrivingAt, depart_time, aircraftID, pilot1, pilot2, flightAttendant1, flightAttendant2, flightAttendant3]
        print(set_workTrip_list)
        logic_API.set_workTrip(set_workTrip_list)

    def set_Destination(self, airportID, travel_time, destination, contact_name, contact_number):
        set_destination_list = [airportID, travel_time, destination, contact_name, contact_number]
        print(set_destination_list)
        logic_API.set_destination(set_destination_list)

    # Get overview
    def get_all_employees(self):
        print("All employees")
        __all_employee_list = logic_API.view_all_employees()
        for line in __all_employee_list:
            id, name, role, licence, address, phonenumber, email, eight = line
            print(f'{id:4}{name:15}{role:22}{licence:12}{address:18}{phonenumber:17}{email:14}{eight}')
        print(SPACER)

    def get_personal_info(self, employee):
        print('Employee Info')
        employee_info_list = logic_API.view_employee_details(employee)
        for line in employee_info_list:
            id, name, role, licence, address, phonenumber, email, eight = line
            print(f'{id:4}{name:15}{role:22}{licence:12}{address:17}{phonenumber:17}{email:14}{eight}')
        print(SPACER)

        return employee_info_list # Á þetta að vera?

    def get_work_schedule(self, employee, year, week):
        print("Picking_employee_work_overview_week")
        __employee_work_week_list = logic_API.view_employee_work_week(employee, year, week)
        for line in __employee_work_week_list:
            flightNumber, departingFrom, arrivingAt, departure_time, return_time, aircraftID, pilot1, pilot2, fa1, fa2, fa3 = line
            print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
        print(SPACER)

    def get_all_pilots(self):
        print("req_overview_pilots")
        __pilots_list = logic_API.view_all_pilots()
        for line in __pilots_list:
            id, name, role, licence, address, phonenumber, email, eight = line
            print(f'{id:4}{name:15}{role:22}{licence:12}{address:18}{phonenumber:17}{email:14}{eight}')
        print(SPACER)

    # This is Alexanders code /all cabin crew
    def get_all_cabin_crew(self):
        print("req_overview_flight attendants")
        __cabin_crew_list = logic_API.view_all_cabin_crew()
        for line in __cabin_crew_list:
            id, name, role, licence, address, phonenumber, email, eight = line
            print(f'{id:4}{name:15}{role:22}{licence:12}{address:18}{phonenumber:17}{email:14}{eight}')
        print(SPACER)

    def get_name(self, employee_id): # Vantar get name
        # __employee_name = self.__logic_API.get_name(employee_id)
        print("Employee name")# þessi print setning er bara svo eg fái ekki errror
        print(SPACER)
        # return __employee_name

    def get_day_with_task(self, task_day):
        print("Employee_with_task")
        __working_employees_list = logic_API.view_working_today(task_day)
        print('Employee Id: ', end="")
        for employee in __working_employees_list:
            print(employee, end=" ")
        print("\n")
        #print(SPACER) Kíkja á það hvernig hægt er að koma þessum spacer fyrir

    def get_day_no_task(self, task_day):
        print("Employee_not_with_task")
        __available_employees_list = logic_API.view_available_today(task_day)
        print('Employee Id: ', end="")
        for employee in __available_employees_list:
            print(employee, end=" ")
        print("\n")
        #print(SPACER) Kíkja á það hvernig hægt er að koma þessum spacer fyrir

    def get_airplane_licence(self, model):
        print("Pilots with licence on one plane")
        __pilots_with_licence_list = logic_API.view_all_with_licence_on_model(model)
        for line in __pilots_with_licence_list:
            id, ssn, name, role, licence, address, phonenumber, email = line
            print(f"{id:4}{ssn:12}{name:52}{role:15}{licence:20}{address:20}{phonenumber:15}{email:100}")
        print(SPACER)

    def get_pilot_licence(self):
        print("Pilots with licence")
        __all_licences_list = logic_API.view_all_pilot_licences()
        for line in __all_licences_list:
            id, ssn, name, role, licence, address, phonenumber, email = line
            print(f"{id:4}{ssn:12}{name:52}{role:15}{licence:20}{address:20}{phonenumber:15}{email:100}")
        print(SPACER)

    def get_all_worktrips(self):
        print("All worktrips")
        __all_work_trips_list = logic_API.view_all_work_trips()
        for line in __all_work_trips_list:
            flightNumber, departingFrom, arrivingAt, departure_time, return_time, aircraftID, pilot1, pilot2, fa1, fa2, fa3 = line
            print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
        print(SPACER)

    def get_week_worktrip(self, year, week):
        print("All worktrips in given year,week")
        __work_week_list = logic_API.view_work_week(year, week)
        for line in __work_week_list :
            flightNumber, departingFrom, arrivingAt, departure_time, return_time, aircraftID, pilot1, pilot2, fa1, fa2, fa3 = line
            print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
        print(SPACER)

    def get_day_worktrip(self, display_workday):
        print("All worktrips in given date")
        __work_day_list = logic_API.view_work_day(display_workday)
        for line in __work_day_list:
            flightNumber, departingFrom, arrivingAt, departure_time, return_time, aircraftID, pilot1, pilot2, fa1, fa2, fa3 = line
            print(
                f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
        print(SPACER)
        return __work_day_list # Á þetta að vera?

    def get_specific_worktrip(self, flight_number):
        print("Single worktrip")
        __work_trip_info_list = logic_API.view_single_worktrip(flight_number)
        for line in __work_trip_info_list:
            flightNumber,departingFrom,arrivingAt,departure_time,return_time,aircraftID,pilot1,pilot2,fa1,fa2,fa3=line
            print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
        print(SPACER)
        return __work_trip_info_list # Á þetta að vera?

    def get_all_destinations(self):
        print("All destinaions")
        __all_destinations_list = logic_API.view_all_destinations()
        for line in __all_destinations_list:
            id, destination, travel_time, contact_name, contact_number = line
            print(f"{id:4}{destination:15}{travel_time:13}{contact_name:17}{contact_number:10}")
        print(SPACER)

    def get_specific_destination(self, a_destination):
        print("One destinaion")
        __destination_info_list = logic_API.view_single_destination(a_destination)
        for line in __destination_info_list:
            id, destination, travel_time, contact_name, contact_number = line
            print(f"{id:4}{destination:15}{travel_time:13}{contact_name:17}{contact_number:10}")

        return __destination_info_list # Á þetta að vera?

    def get_all_planes(self):
        print("All airplane")
        __all_airplanes_list = logic_API.view_all_planes()
        for line in __all_airplanes_list:
            planeInsignia, planetypeId = line
            print(f"{planeInsignia:<15}{planetypeId}")
        print(SPACER)

    def get_specific_aircraft(self, plane_insignia):
        print("Single airplanes")
        __airplane_info_list = logic_API.view_single_airplane(plane_insignia)
        for line in __airplane_info_list:
            planeInsignia, planetypeId = line
            print(f"{planeInsignia:<15}{planetypeId}")
        print(SPACER)

        return __airplane_info_list # Á þetta að vera?

    def get_plane_state(self):
        print("State of planes")
        __state_of_airplanes_list = logic_API.view_state_of_planes(date)
        for line in __state_of_airplanes_list:
            planeType, planeInsignia, status, next_available, destination, flightNumber = line
            print(f"{planeInsignia:15}{planeType:15}{status:14}{str(next_available):20}{destination:13}{flightNumber}")
        print(SPACER)


    # Set changes
    def set_changes_for_existing_employee(self, employee):
        logic_API.edit_employee(employee) # Vantar!
        print("Setja inn breytt gögn um notanda")

    def set_changes_for_existing_destination(self, destination):
        logic_API.edit_destination_contact(destination) # Vantar!
        print("Setja inn breytt gögn um áfangastað")

    def set_changes_for_existing_aircraft(self, aircraft):
        logic_API.edit_airplane(aircraft) # Vantar!
        print("Setja inn breytt gögn um flugvél")

    def set_changes_for_existing_worktrip(self, worktrip):
        logic_API.edit_worktrip_crew(worktrip) # Vantar!
        print("Setja inn breytt gögn um vinnuferð")