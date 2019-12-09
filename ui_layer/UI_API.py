SPACER = "_____________________________________________"
class UI_Api:
    def __inti__(self):
        self.__LL_Api = LL_Api()

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

    def get_all_employees(self):
        #self.__LL_Api.get_all_employees()
        #Her þarf að raða gögnum úr lista og prenta út
        print("This is me showing of all employees")
        print(SPACER)

    def get_personal_info(self, employee):
        pemp_employee = ["2105972719", "Birgir Snær Ingason", "Pilot","Fokker", "Drekavellir 63", "8453461"]
        #self.__LL_Api.get_personal_info(employee)
        print("here we have personal info")
        print(SPACER)
        if employee == "1":
            return pemp_employee

    def get_work_schedule(self, employee):
        # self.__LL_Api.get_work_schedule(employee)
        print("Here we have work schedule")
        print(SPACER)

    def get_all_pilots(self):
        # self.__LL_Api.get_all_pilots()
        # Her þarf að raða gögnum úr lista og prenta út
        print("This is me showing of all pilots")
        print(SPACER)

    def get_all_cabin_crew(self):
        # self.__LL_Api.get_all_cabin_crew()
        # Her þarf að raða gögnum úr lista og prenta út
        print("This is me showing of all cabincrew")
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