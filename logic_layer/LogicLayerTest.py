#used in methood picking_employee_work_overview_week
from datetime import date, timedelta, datetime
from dataLayer import DataAPI

#following class has various methoods that serve as an overview for employees

class LogicAPI:
    def __init__(self):
        self.__crew = DataAPI("Crew")
        self.__aircraft = DataAPI("Aircraft")
        self.__destinations = DataAPI("Destinations")
        self.__flight_records = DataAPI("FlightRecords")

    def req_overview_allemployees(self):
        #geting a list of all employees
        __return_list = self.__crew.read_file()
        return __return_list

    def req_overview_pilots(self):
        #getting an list of all empoyees
        __all_employee = self.__crew.read_file()
        __pilot_list = []
        #adding the first row(adding the header)
        __pilot_list.append(__all_employee[0])
        #each list is one employee
        for list in __all_employee:
            #if the role pilot is in
            if 'Pilot' == list[3]:
                __pilot_list.append(list)

        if len(__pilot_list) <= 1:
            return None

        return __pilot_list

    def req_overview_flightattendants(self):
        #getting an list of all employees
        #same funtion as above but for
        __all_employee = self.__crew.read_file()
        __flight_attendants = []
        __flight_attendants.append(__all_employee[0])
        for listi in __all_employee:
            if 'Cabincrew' in listi:
                __flight_attendants.append(listi)
        if len(__flight_attendants) <= 1:
            return None

        return __flight_attendants

    #nákvæm leiit,velja starfsmann, persónuuplýsingar
    def picking_employee_personal_det(self, __identity):
        __identity = str(__identity)
        __all_employee = self.__crew.read_file()
        __list_of_employee = []
        __list_of_employee.append(__all_employee[0])
        for employee in __all_employee:
            if __identity in employee:
                __list_of_employee.append(employee)

        if len(__list_of_employee) <= 1:
            return None


        return __list_of_employee

    #nessecery part of picking_employee_work_week
    def list_of_dates_in_given_week_and_given_year(self, __year, __week):
        __day = date(__year, 1, 1)
        __day = __day - timedelta(__day.weekday())
        __delta = timedelta(days=(__week - 1) * 7)
        return [str(__day + __delta), str(__day + __delta + timedelta(days=1)), str(__day + __delta + timedelta(days=2)),
                str(__day + __delta + timedelta(days=3)),
                str(__day + __delta + timedelta(days=4)), str(__day + __delta + timedelta(days=5)),
                str(__day + __delta + timedelta(days=6))]

    # nákvæm leiit,velja starfsmann,vikuskipulag (vika x)
    def picking_employee_work_overview_week(self, __identity, __year, __week):
        #make a list of all fligts
        __all_flights = self.__flight_records.read_file()

        #getting all the days in given week of year
        classObject = LogicAPI()
        __days_in_week_list = classObject.list_of_dates_in_given_week_and_given_year(__year, __week)

        __week_overview = []
        #take the days from the respectable value and search for that in the all_flights (if identity and weedays... then append to list)
        #adding the first line
        __week_overview.append(__all_flights[0])
        #each line in all flights
        for line in __all_flights:
            #each date in week
            for date in __days_in_week_list:
                #check if date maches any dates in each line of all_flights
                if (date == (line[3][:10] or line[4][:10])):
                    #if it does it checks if the pilots id is there
                    if str(__identity) in line:
                        #appending to the week overwiew
                        __week_overview.append(line)

        if len(__week_overview) <= 1:
            return None

        #making the date an formated object
        for line in __week_overview:
            try:
                line[3] = datetime.strptime(line[3], '%Y-%m-%dT%H:%M:%S')
                line[4] = datetime.strptime(line[4], '%Y-%m-%dT%H:%M:%S')

            except:
                pass
        return __week_overview

    def all_employees_with_task(self, __date):
        __return_list = []
        __unavalible_employees = []
        __all_flights = self.__flight_records.read_file()

        for line in __all_flights:
            if (__date == (line[3][:10] or line[4][:10])):
                    __return_list.append(line)

        if len(__return_list) <= 1:
            return None
        for line in __return_list:
            __unavalible_employees.append(line[6])
            __unavalible_employees.append(line[7])
            __unavalible_employees.append(line[8])
            __unavalible_employees.append(line[9])
            __unavalible_employees.append(line[10])

        return __unavalible_employees

    def all_employees_not_with_task(self, __date):
        __temp_list = []
        __unavalible_employees = []
        __all_flights = self.__flight_records.read_file()
        for line in __all_flights:
            if (__date == (line[3][:10] or line[4][:10])):
                    __temp_list.append(line)


        if len(__temp_list) < 1:
            return None
        #getting all of the employers id
        for line in __temp_list:
            __unavalible_employees.append(line[6])
            __unavalible_employees.append(line[7])
            __unavalible_employees.append(line[8])
            __unavalible_employees.append(line[9])
            __unavalible_employees.append(line[10])


        #removing duplicates
        new_unavalible_employees = []
        for ch in __unavalible_employees:
            if ch not in new_unavalible_employees:
                new_unavalible_employees.append(ch)

        #all_crew_id
        __all_crew = self.__crew.read_file()
        __all_crew_list = []
        for line in __all_crew:
            if line[0]!= "id":
                __all_crew_list.append(line[0])

        #removing those who are unavalible
        for crew_id in __unavalible_employees:
            if crew_id in __all_crew_list:
                __all_crew_list.remove(crew_id)

        return __all_crew_list


    def all_pilots_with_licence_on_an_given_plane(self, __plane):
        classObject = LogicAPI()
        __pilot_list = classObject.req_overview_pilots()
        __pilots_with_licence = []
        __pilots_with_licence.append(__pilot_list[0])
        for pilot in __pilot_list:
            if pilot[4] == __plane:
                __pilots_with_licence.append(pilot)

        if len(__pilots_with_licence) <= 1:
            return None

        return __pilots_with_licence

    def all_pilots_with_licences_all_planes(self):
        __list_of_all_pilots = []
        classObject = LogicAPI()
        __list_of_all_pilots = classObject.req_overview_pilots()

        if len(__list_of_all_pilots) <= 1:
            return None

        return __list_of_all_pilots

#overview of worktrips
    def all_worktrips(self):
        __all_worktrips = self.__flight_records.read_file()

        if len(__all_worktrips) <= 1:
            return None

        # making the right format for the date
        for line in __all_worktrips:
            try:
                line[3] = datetime.strptime(line[3], '%Y-%m-%dT%H:%M:%S')
                line[4] = datetime.strptime(line[4], '%Y-%m-%dT%H:%M:%S')

            except:
                pass

        return __all_worktrips

    def get_week_of_worktrip(self, __year, __week):
        classObject = LogicAPI()
        __all_worktrips = self.__flight_records.read_file()
        __days_in_week_list = classObject.list_of_dates_in_given_week_and_given_year(__year, __week)
        __week_overview = []
        # take the days from the respectable value and search for that in the all_worktrips (if identity and weedays... then append to list)
        # adding the first line
        __week_overview.append(__all_worktrips[0])
        # each line in all worktrips
        for line in __all_worktrips:
            # each date in week
            for date in __days_in_week_list:
                # check if date maches any dates in each line of all_worktrip
                if (date == (line[3][:10] or line[4][:10])):

                    # appending to the week overwiew
                    __week_overview.append(line)

        if len(__week_overview) <= 1:
            return None
        #making the right format for the date
        for line in __week_overview:
            try:
                line[3] = datetime.strptime(line[3], '%Y-%m-%dT%H:%M:%S')
                line[4] = datetime.strptime(line[4], '%Y-%m-%dT%H:%M:%S')
            except:
                pass
        return __week_overview

    def worktrips_of_the_day(self,date):
        __all_worktrips = self.__flight_records.read_file()
        __day_overview = []
        # take the days from the respectable value and search for that in the all_worktrips (if identity and weedays... then append to list)
        # adding the first line
        __day_overview.append(__all_worktrips[0])
        # each line in all worktrips
        for line in __all_worktrips:
                # check if date maches any dates in each line of all_worktrip
                if (date == (line[3][:10] or line[4][:10])):
                    # appending to the week overview
                    __day_overview.append(line)
                    try:
                        line[3] = datetime.strptime(line[3], '%Y-%m-%dT%H:%M:%S')
                        line[4] = datetime.strptime(line[4], '%Y-%m-%dT%H:%M:%S')
                    except:
                        pass
        if len(__day_overview) <= 1:
            return None

        return __day_overview

    def singe_worktrip(self,flight_number):
        __all_worktrips = self.__flight_records.read_file()
        return_list = []
        return_list.append(__all_worktrips[0])
        for line in __all_worktrips:
            if flight_number in line:
                try:
                    line[3] = datetime.strptime(line[3], '%Y-%m-%dT%H:%M:%S')
                    line[4] = datetime.strptime(line[4], '%Y-%m-%dT%H:%M:%S')
                except:
                    pass
                return_list.append(line)
        return return_list


#overview destination
    def all_destinations(self):
        #getting all destination
        __all_destinaions = self.__destinations.read_file()

        if len(__all_destinaions) <=1:
            return None

        return __all_destinaions

    def one_destination(self, dest):
        #getting a list of all of the destinations
        __all_destinaions = self.__destinations.read_file()
        list_of_the_destinataion = []
        #getting the first row of the csv file (aka: header)
        list_of_the_destinataion.append(__all_destinaions[0])
        #for each line ew are gonna check if the first column in the row is equal to destination
        #if it is true we add the line to the list of destination
        for line in __all_destinaions:
            if line[0] == dest:
                list_of_the_destinataion.append(line)


        if len(list_of_the_destinataion) <= 1:
            return None

        return list_of_the_destinataion

#overview aeroplanes

    def all_planes(self):
        #getting all planes
        __all_planes = self.__aircraft.read_file()

        if len(__all_planes) <= 1:
            return None

        return __all_planes

    def single_plane(self, plane_insignia):
        __all_planes = self.__aircraft.read_file()
        return_list = []
        return_list.append(__all_planes[0])
        for line in __all_planes:
            if line[0] == plane_insignia:
                return_list.append(line)
                return return_list
        return None

    def state_of_plane(self, date_input):

        #importing all planes
        classObject = LogicAPI()
        __list_of_all_planes = classObject.all_planes()
        __list_of_all_planes.pop(0)
        __list_of_avalible_planes_insignia = []

        #taking only the insignia an appending it to the list
        for line in __list_of_all_planes:
            __list_of_avalible_planes_insignia.append(line[0])


        #importing all worktrips
        __list_of_all_worktrips = classObject.all_worktrips()

        #making the date  an isoformat

        date_iso_format = datetime.strptime(date_input, '%Y-%m-%dT%H:%M:%S')

        #making the final list
        __final_list = []
        __final_list.append(['planeType', 'planeInsignia', 'status', 'next available', 'destination', 'flightNumber'])

        __list_of_all_worktrips.pop(0)

        #parsing
        for line in __list_of_all_worktrips:

            #getting the planetype name fokker300...
            for plane_row in __list_of_all_planes:
                if line[5] in plane_row:
                    planeType = plane_row[1]

            departure = line[3]
            arrival = line[4]
            # if date is between dep. and (arrival + 1hr) then is aircraft is unavailable.
            # if datetime.strptime(departure, '%Y-%m-%dT%H:%M:%S') <= date_iso_format <= ((datetime.strptime(arrival, '%Y-%m-%dT%H:%M:%S')) + timedelta(hours=1)):

            if departure <= date_iso_format <= arrival + timedelta(hours=1):
                #making all of the attributes that go to the list
                next_available = line[4] + timedelta(hours=1)
                planeinsignia = line[5]
                destination = line[2]
                flightnumber = line[0]
                #placing the attributes into the list
                __final_list.append([planeType, planeinsignia, 'In Use', next_available, destination, flightnumber])

                #removing the plane insignia from the avalible planes.
                try:
                    __list_of_avalible_planes_insignia.remove(line[5])
                except ValueError:
                    continue

        for plane_insignia in __list_of_avalible_planes_insignia:
            # getting the planetype name fokker300...
            for plane_row in __list_of_all_planes:
                if plane_insignia in plane_row:
                    planeType = plane_row[1]

            __final_list.append([planeType, plane_insignia, 'Available', 'N/A', 'N/A', 'N/A'])

        return __final_list
