#from LogicLayerTest import LogicAPI
from logic_layer.LogicLayerTest import LogicAPI
from datetime import date, timedelta, datetime

SPACER = "_____________________________________________"
logic_API = LogicAPI()
class UI_API:
    def __inti__(self):
        self.__logic_API = LogicAPI()

    def set_pilot(self, ssn, name, role, licence, email,  address, gsm):
        set_pilot_list = [ssn, name, role, licence, email, address, gsm]
        #self.__LL_Api.set_pilot(set_pilot_list)

    def set_airplane(self, Plane_Insignia, plane_type_Id):
        set_airplane_list = [Plane_Insignia, plane_type_Id]
        print(set_airplane_list)
        #self.__LL_Api.set_airplane(set_airplane_list)

    def set_Cabin_crew(self, ssn, name, role, email, address, gsm):
        set_cabin_crew_list = [ssn, name, role, "N/A", email, address, gsm]
        #self.__LL_Api.set_cabin_crew(set_cabin_crew_list)

    def set_WorkTrip(self, arrivingAt, aircraftID, pilot1, pilot2, flightAttendant1, flightAttendant2, flightAttendant3):
        set_workTrip_list =[arrivingAt, aircraftID, pilot1, pilot2, flightAttendant1, flightAttendant2, flightAttendant3]
        print(set_workTrip_list)
        #self.__LL_Api.set_worktrip(set_workTrip_list)

    def set_Destination(self, airportID, destination, contact_name, contact_number):
        set_destination_list = [airportID, destination, contact_name, contact_number]
        print(set_destination_list)
        #self.__LL_Api.set_destination(set_destination_list)

    #This is Alexanders code /all employees
    def get_all_employees(self):
        print("All employees")
        test_listi1a = logic_API.req_overview_allemployees()
        for line in test_listi1a:
            id, name, role, licence, address, phonenumber, email, eight = line
            print(f'{id:4}{name:15}{role:22}{licence:12}{address:18}{phonenumber:17}{email:14}{eight}')
        print(SPACER)

    def get_personal_info(self, employee):
        print('Employee Info')
        employee_info_list = logic_API.picking_employee_personal_det(employee)

        for line in employee_info_list:
            id, name, role, licence, address, phonenumber, email, eight = line
            print(f'{id:4}{name:15}{role:22}{licence:12}{address:17}{phonenumber:17}{email:14}{eight}')
        print(SPACER)

        return employee_info_list

    def get_work_schedule(self, employee, year, week):
        print("Picking_employee_work_overview_week")
        test_listi2 = logic_API.picking_employee_work_overview_week(employee, year, week)
        for line in test_listi2:
            flightNumber, departingFrom, arrivingAt, departure_time, return_time, aircraftID, pilot1, pilot2, fa1, fa2, fa3 = line
            print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
        print(SPACER)

    # This is Alexanders code /all pilots
    def get_all_pilots(self):
        print("req_overview_pilots")
        test_listi1b = logic_API.req_overview_pilots()
        for line in test_listi1b:
            id, name, role, licence, address, phonenumber, email, eight = line
            print(f'{id:4}{name:15}{role:22}{licence:12}{address:18}{phonenumber:17}{email:14}{eight}')
        print(SPACER)

    # This is Alexanders code /all cabin crew
    def get_all_cabin_crew(self):
        print("req_overview_flightattendants")
        test_listi1c = logic_API.req_overview_flightattendants()
        for line in test_listi1c:
            id, name, role, licence, address, phonenumber, email, eight = line
            print(f'{id:4}{name:15}{role:22}{licence:12}{address:18}{phonenumber:17}{email:14}{eight}')
        print(SPACER)

    def get_name(self, employee_id): # Vantar get name
        testname = "birgir"
        #self.__LL_Api.get_name()
        print("Employee name")# þessi print setning er bara svo eg fái ekki errror
        print(SPACER)
        return testname

    def get_day_with_task(self, task_day):
        print("Employee_with_task")
        #
        test_listi3 = logic_API.all_employees_with_task(task_day)
        print('Employee Id: ', end="")
        for ch in test_listi3:
            print(ch, end=" ")
        print("\n")
        #print(SPACER) Kíkja á það hvernig hægt er að koma þessum spacer fyrir

    def get_day_no_task(self, task_day):
        print("Employee_not_with_task")
        test_listi4 = logic_API.all_employees_not_with_task(task_day)
        print('Employee Id: ', end="")
        for ch in test_listi4:
            print(ch, end=" ")
        print("\n")
        #print(SPACER) Kíkja á það hvernig hægt er að koma þessum spacer fyrir

    def get_airplane_licence(self, model):
        print("Pilots with licence on one plane")
        test_listi5 = logic_API.all_pilots_with_licence_on_an_given_plane(model)
        for line in test_listi5:
            id, ssn, name, role, licence, address, phonenumber, email = line
            print(f"{id:4}{ssn:12}{name:52}{role:15}{licence:20}{address:20}{phonenumber:15}{email:100}")
        print(SPACER)

    def get_pilot_licence(self):
        print("Pilots with licence")
        test_listi6 = logic_API.all_pilots_with_licences_all_planes()
        for line in test_listi6:
            id, ssn, name, role, licence, address, phonenumber, email = line
            print(f"{id:4}{ssn:12}{name:52}{role:15}{licence:20}{address:20}{phonenumber:15}{email:100}")
        print(SPACER)

    def get_all_worktrips(self):
        print("All worktrips")
        test_listi7 = logic_API.all_worktrips()
        for line in test_listi7:
            flightNumber, departingFrom, arrivingAt, departure_time, return_time, aircraftID, pilot1, pilot2, fa1, fa2, fa3 = line
            print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
        print(SPACER)

    def get_week_worktrip(self, year, week):
        print("All worktrips in given year,week")
        test_listi8 = logic_API.get_week_of_worktrip(year, week)
        for line in test_listi8:
            flightNumber, departingFrom, arrivingAt, departure_time, return_time, aircraftID, pilot1, pilot2, fa1, fa2, fa3 = line
            print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
        print(SPACER)

    def get_day_worktrip(self, display_workday):
        print("All worktrips in given date")
        test_listi9a = logic_API.worktrips_of_the_day(display_workday)
        for line in test_listi9a:
            flightNumber, departingFrom, arrivingAt, departure_time, return_time, aircraftID, pilot1, pilot2, fa1, fa2, fa3 = line
            print(
                f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
        print(SPACER)
        return test_listi9a

    def get_all_destinations(self):
        print("All destinaions")
        test_listi10 = logic_API.all_destinations()
        for line in test_listi10:
            id, destination, travel_time, contact_name, contact_number = line
            print(f"{id:4}{destination:15}{travel_time:13}{contact_name:17}{contact_number:10}")
        print(SPACER)

    def get_specific_destination(self, a_destination):
        print("One destinaion")
        test_listi11 = logic_API.one_destination("LYR")
        for line in test_listi11:
            id, destination, travel_time, contact_name, contact_number = line
            print(f"{id:4}{destination:15}{travel_time:13}{contact_name:17}{contact_number:10}")
        return test_listi11

    def get_all_planes(self):
        print("All airplane")
        test_listi12 = logic_API.all_planes()
        for line in test_listi12:
            planeInsignia, planetypeId = line
            print(f"{planeInsignia:<15}{planetypeId}")
        print(SPACER)

    def get_plane_state(self):
        print("State of planes")
        test = logic_API.state_of_plane("2019-11-02T14:21:00")
        for line in test:
            planeType, planeInsignia, status, next_available, destination, flightNumber = line
            print(f"{planeInsignia:15}{planeType:15}{status:14}{str(next_available):20}{destination:13}{flightNumber}")
        print(SPACER)

    def set_changes_for_existing_employee(self, employee):
        #self.__LL_Api.set_changes_for_existing_employee(employee)
        print("Setja inn breytt gögn um notanda")

    def set_changes_for_existing_destination(self, destination):
        #self.__LL_Api.set_changes_for_existing_destination(destination)
        print("Setja inn breytt gögn um áfangastað")

    def get_specific_aircraft(self, plane_insignia):
        print("Single airplanes")
        test_listi13 = logic_API.single_plane(plane_insignia)
        for line in test_listi13:
            planeInsignia, planetypeId = line
            print(f"{planeInsignia:<15}{planetypeId}")
        print(SPACER)
        return test_listi13

    def set_changes_for_existing_aircraft(self, aircraft):
        #self.__LL_Api.set_changes_for_existing_aircraft(aircraft)
        print("Setja inn breytt gögn um flugvél")

    def get_specific_worktrip(self, flight_number):
        print("Single worktrip")
        test_listi9c = logic_API.singe_worktrip(flight_number)
        for line in test_listi9c:
            flightNumber,departingFrom,arrivingAt,departure_time,return_time,aircraftID,pilot1,pilot2,fa1,fa2,fa3=line
            print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
        print(SPACER)
        return test_listi9c

    def set_changes_for_existing_worktrip(self, worktrip):
        #self.__LL_Api.set_changes_for_existing_worktrip(worktrip)
        print("Setja inn breytt gögn um vinnuferð")