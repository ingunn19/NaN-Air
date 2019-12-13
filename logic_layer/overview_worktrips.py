from logic_layer.clock import Clock
from logic_layer.logic_parent import LogicParent

class WorkTripOverviewLogic(LogicParent):
#overview of worktrips
    def req_all_worktrips(self):
        __all_worktrips = self.flight_records.read_file()
        # if len(__all_worktrips) <= 1:
        #     return None

        # making the right format for the date
        for line in __all_worktrips:
            try:
                line[3] = datetime.strptime(line[3], '%Y-%m-%dT%H:%M:%S')
                line[4] = datetime.strptime(line[4], '%Y-%m-%dT%H:%M:%S')
            except:
                pass
        return __all_worktrips

    def req_worktrips_of_the_week(self, __year, __week):
        clock = Clock()
        __all_worktrips = self.flight_records.read_file()
        __days_in_week_list = clock.list_of_dates_in_given_week_and_given_year(__year, __week)
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
        # if len(__week_overview) <= 1:
        #     return None
        #making the right format for the date
        for line in __week_overview:
            try:
                line[3] = datetime.strptime(line[3], '%Y-%m-%dT%H:%M:%S')
                line[4] = datetime.strptime(line[4], '%Y-%m-%dT%H:%M:%S')
            except:
                pass
        return __week_overview

    def req_worktrips_of_the_day(self,date):
        __all_worktrips = self.flight_records.read_file()
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
        # if len(__day_overview) <= 1:
        #     return None
        return __day_overview

    def req_single_worktrip(self,flight_number):
        __all_worktrips = self.flight_records.read_file()
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