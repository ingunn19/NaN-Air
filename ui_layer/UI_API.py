#from LogicLayerTest import LogicAPI
from logic_layer.LogicLayerTest import LogicAPI
from datetime import date, timedelta, datetime
SPACER = "_____________________________________________"
classObject = LogicAPI()
class UI_Api:
    def __inti__(self):
        self.__LL_Api = LogicAPI()
        self.classObject = LogicAPI()

    def set_pilot(self, ssn, name, role, licence, address, gsm):
        set_pilot_list = [ssn, name, role, licence, address, gsm]
        print(set_pilot_list)
        #self.__LL_Api.set_pilot(set_pilot_list)

    def set_airplane(self, Plane_Insignia, plane_type_Id):
        set_airplane_list = [Plane_Insignia, plane_type_Id]
        print(set_airplane_list)
        #self.__LL_Api.set_airplane(set_airplane_list)

    def set_Cabin_crew(self, ssn, name, role, address, gsm):
        set_cabin_crew_list = [ssn, name, role, address, gsm]
        print(set_cabin_crew_list)
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
        test_listi1a = classObject.req_overview_allemployees()
        for line in test_listi1a:
            id, name, role, licence, address, phonenumber, email, eight = line
            print(f'{id:4}{name:15}{role:22}{licence:12}{address:18}{phonenumber:17}{email:14}{eight}')
        print(SPACER)

    def get_personal_info(self, employee):
        print('Employee Info')
        test_listi1d = classObject.picking_employee_personal_det(8)

        for line in test_listi1d:
            id, name, role, licence, address, phonenumber, email, eight = line
            print(f'{id:4}{name:15}{role:22}{licence:12}{address:17}{phonenumber:17}{email:14}{eight}')
        print(SPACER)

    def get_work_schedule(self, employee, year, week):
        print("Picking_employee_work_overview_week")
        test_listi2 = classObject.picking_employee_work_overview_week(ID, year, week)
        for line in test_listi2:
            flightNumber, departingFrom, arrivingAt, departure_time, return_time, aircraftID, pilot1, pilot2, fa1, fa2, fa3 = line
            print(
                f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
        print(SPACER)

    # This is Alexanders code /all pilots
    def get_all_pilots(self):
        print("req_overview_pilots")
        test_listi1b = classObject.req_overview_pilots()
        for line in test_listi1b:
            id, name, role, licence, address, phonenumber, email, eight = line
            print(f'{id:4}{name:15}{role:22}{licence:12}{address:18}{phonenumber:17}{email:14}{eight}')
        print(SPACER)

    # This is Alexanders code /all cabin crew
    def get_all_cabin_crew(self):
        print("req_overview_flightattendants")
        test_listi1c = classObject.req_overview_flightattendants()
        for line in test_listi1c:
            id, name, role, licence, address, phonenumber, email, eight = line
            print(f'{id:4}{name:15}{role:22}{licence:12}{address:18}{phonenumber:17}{email:14}{eight}')
        print(SPACER)

    def get_name(self, employee_id):
        testname = "birgir"
        #self.__LL_Api.get_name()
        print("Employee name")# þessi print setning er bara svo eg fái ekki errror
        print(SPACER)
        return testname

    def get_day_with_task(self, task_day):
        # self.__LL_Api.get_day_with_task(task_day)
        print("Employees with task")# þessi print setning er bara svo eg fái ekki errror
        print(SPACER)

    def get_day_no_task(self, task_day):
        # self.__LL_Api.get_day_no_task(task_day)
        print("Employees without a task")  # þessi print setning er bara svo eg fái ekki errror
        print(SPACER)

    def get_airplane_licence(self, model):
        #self.__LL_Api.get_airplane_licence(model)
        print("Print pilots with licence on given model of plane")# þessi print setning er bara svo eg fái ekki errror
        print(SPACER)

    def get_pilot_licence(self):
        #self.__LL_Api.get_pilot_licence()
        print("print all pilots and there licences")# þessi print setning er bara svo eg fái ekki errror
        print(SPACER)

    def get_all_worktrips(self):
        #self.__LL_Api.get_all_worktrips()
        print("Here we list all worktrips")
        print(SPACER)

    def get_week_worktrip(self, display_workweek):
        #self.__LL_Api.get_week_worktrips(display_workweek)
        print("Here we list the worktrips for a chosen week")
        print(SPACER)

    def get_day_worktrip(self, display_workday):
        #self.__LL_Api.get_day_worktrip(display_workday)
        print("Here we list the worktrips for a chosen day")
        print(SPACER)

    def get_all_destinations(self):
        #self.__LL_Api.get_all_destinations()
        print("Here we list all destinations")
        print(SPACER)

    def get_specific_destination(self, a_destination):
        testdestinationlist = ["1", "Greenland", "Birgir", "845-3461"]
        #self.__LL_Api.get_specific_destination(a_destination)
        print("Here we list a specific destination")
        print(SPACER)
        return testdestinationlist

    def get_all_planes(self):
        #self.__LL_Api.get_all_planes()
        print("Here we list all planes")
        print(SPACER)

    def get_plane_state(self):
        #self.__LL_Api.get_stadeof_planes()
        print("here we list state of all planes")
        print(SPACER)

    def set_changes_for_existing_employee(self, employee):
        #self.__LL_Api.set_changes_for_existing_employee(employee)
        print("Setja inn breytt gögn um notanda")

    def set_changes_for_existing_destination(self, destination):
        #self.__LL_Api.set_changes_for_existing_destination(destination)
        print("Setja inn breytt gögn um áfangastað")

    def get_specific_aircraft(self, plane_insignia):
        testaircraft = ["plane_insignia", "plane ID"]
        #self.__LL_Api.get_specific_aircraft(plane_insignia)
        print("hér sýnum við áhverðna flugvél")
        print(SPACER)
        return testaircraft

    def set_changes_for_existing_aircraft(self, aircraft):
        #self.__LL_Api.set_changes_for_existing_aircraft(aircraft)
        print("Setja inn breytt gögn um flugvél")

    def get_specific_worktrip(self, flight_number):
        testworktrip = ["100", "reykjavik", "greenland", "timeto", "timehome", "ID", "jónas", "lisa", "katrin", "maggey", "lirgir"]# pilot1, pilot2, cc1, cc2, cc3
        #self.__LL_Api.get_specific_worktrip(flight_number)
        print("ná í upplýsingar um staka vinnuferð")
        print(SPACER)
        return testworktrip

    def set_changes_for_existing_worktrip(self, worktrip):
        #self.__LL_Api.set_changes_for_existing_worktrip(worktrip)
        print("Setja inn breytt gögn um vinnuferð")