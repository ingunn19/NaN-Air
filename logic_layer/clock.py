from datetime import date, timedelta, datetime

class Clock():
    def __init__(self, date_time=''):
        self.__date_time = date_time

    def get_current_time(self):
        now = datetime.now()
        # now.strftime("%Y-%m-%dT%H:%M:%S")
        return now

    def calculate_time_diff(self, time2):
        time_1 = datetime.strptime(self.__date_time, '%Y-%m-%dT%H:%M:%S')
        time_2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S')
        time_diff = (time_1 - time_2)
        return time_diff.total_seconds() / 3600

    def calculate_return_time(self, travel_time):
        datetime_takeoff = datetime.strptime(self.__date_time, '%Y-%m-%dT%H:%M:%S')
        timedelta_flight_duration = timedelta(hours=int(travel_time))
        return_time = (datetime_takeoff + timedelta_flight_duration)
        return return_time.strftime('%Y-%m-%dT%H:%M:%S')

    def aricraft_next_available(self):
        datetime_return_time = datetime.strptime(self.__date_time, '%Y-%m-%dT%H:%M:%S')
        datetime_waiting_time = timedelta(hours=1)
        time_next_available = (datetime_return_time + datetime_waiting_time)
        return time_next_available.strftime('%Y-%m-&dT%H:%M:%S')

    #nessecery part of picking_employee_work_week
    def list_of_dates_in_given_week_and_given_year(self, __year, __week):
        __day = date(__year, 1, 1)
        __day = __day - timedelta(__day.weekday())
        __delta = timedelta(days=(__week - 1) * 7)
        return [str(__day + __delta), str(__day + __delta + timedelta(days=1)), str(__day + __delta + timedelta(days=2)),
                str(__day + __delta + timedelta(days=3)),
                str(__day + __delta + timedelta(days=4)), str(__day + __delta + timedelta(days=5)),
                str(__day + __delta + timedelta(days=6))]