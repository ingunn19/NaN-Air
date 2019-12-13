from logic_layer.clock import Clock
from logic_layer.overview_worktrips import WorkTripOverviewLogic
from logic_layer.logic_parent import LogicParent
from datetime import datetime, timedelta

worktrips = WorkTripOverviewLogic()

class EmployeeOverviewLogic(LogicParent):
# Overview employees
    def req_overview_allemployees(self):
        #geting a list of all employees
        __return_list = self.crew.read_file()
        return __return_list

    def req_overview_pilots(self):
        #getting an list of all empoyees
        __all_employee = self.crew.read_file()
        __pilot_list = []
        #adding the first row(adding the header)
        __pilot_list.append(__all_employee[0])
        #each list is one employee
        for list in __all_employee:
            #if the role pilot is in
            if 'Pilot' == list[3]:
                __pilot_list.append(list)
        # if len(__pilot_list) <= 1:
        #     return None
        return __pilot_list

    def req_overview_flightattendants(self):
        #getting an list of all employees
        #same funtion as above but for
        __all_employee = self.crew.read_file()
        __flight_attendants = []
        __flight_attendants.append(__all_employee[0])

        for listi in __all_employee:
            if 'Cabincrew' in listi:
                __flight_attendants.append(listi)
        # if len(__flight_attendants) <= 1:
        #     return None
        return __flight_attendants

    #nákvæm leit, velja starfsmann, persónuuplýsingar
    def req_employee_personal_details(self, __identity):
        __identity = str(__identity)
        __all_employee = self.crew.read_file()
        __list_of_employee = []
        __list_of_employee.append(__all_employee[0])

        for employee in __all_employee:
            if __identity in employee:
                __list_of_employee.append(employee)

        # if len(__list_of_employee) <= 1:
        #     return None
        return __list_of_employee

    # nákvæm leiit,velja starfsmann,vikuskipulag (vika x)
    def req_employee_work_week_overview(self, __identity, __year, __week):
        #make a list of all fligts
        __all_flights = self.flight_records.read_file()

        #getting all the days in given week of year
        clock = Clock()
        __days_in_week_list = clock.list_of_dates_in_given_week_and_given_year(__year, __week)

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
        # if len(__week_overview) <= 1:
        #     return None

        #making the date an formated object
        for line in __week_overview:
            try:
                line[3] = datetime.strptime(line[3], '%Y-%m-%dT%H:%M:%S')
                line[4] = datetime.strptime(line[4], '%Y-%m-%dT%H:%M:%S')
            except:
                pass
        return __week_overview

    def req_all_employees_with_task(self, __date):
        __return_list = []
        __unavalible_employees = []
        __all_flights = self.flight_records.read_file()

        for line in __all_flights:
            if (__date == (line[3][:10] or line[4][:10])):
                    __return_list.append(line)
        # if len(__return_list) <= 1:
        #     return None

        for line in __return_list:
            __unavalible_employees = [i for i in line[6:11]]

        return __unavalible_employees

    def req_all_employees_not_with_task(self, __date):
        __unavalible_employees = []
        __flights_of_the_day = worktrips.req_worktrips_of_the_day(__date)

        #getting all of the employers id
        for line in __flights_of_the_day:
            __unavalible_employees = [i for i in line[6:11]]

        #removing duplicates
        new_unavalible_employees = []
        for ch in __unavalible_employees:
            if ch not in new_unavalible_employees:
                new_unavalible_employees.append(ch)

        #all_crew_id
        __all_crew = self.crew.read_file()
        __all_crew_list = []
        for line in __all_crew:
            if line[0]!= "id":
                __all_crew_list.append(line[0])

        #removing those who are unavalible
        for crew_id in __unavalible_employees:
            if crew_id in __all_crew_list:
                __all_crew_list.remove(crew_id)

        return __all_crew_list

    def req_all_pilots_with_licence_on_a_given_plane(self, __plane):
        classObject = EmployeeOverviewLogic()
        __pilot_list = classObject.req_overview_pilots()
        __pilots_with_licence = []
        __pilots_with_licence.append(__pilot_list[0])
        for pilot in __pilot_list:
            if pilot[4] == __plane:
                __pilots_with_licence.append(pilot)

        # if len(__pilots_with_licence) <= 1:
        #     return None
        return __pilots_with_licence

    def req_all_pilot_licences(self):
        __list_of_all_pilots = []
        classObject = EmployeeOverviewLogic()
        __list_of_all_pilots = classObject.req_overview_pilots()

        # if len(__list_of_all_pilots) <= 1:
        #     return None
        return __list_of_all_pilots

