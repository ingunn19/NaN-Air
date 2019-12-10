from datetime import date, timedelta, datetime

class Clock():
    def __init__(self, date_time=''):
        self.__date_time = date_time

    def get_current_time(self):
        now = datetime.now()
        return now.strftime("%Y-%m-%dT%H:%M:%S")

    def calculate_time_diff(self, time2):
        time_1 = datetime.datetime.strptime(self.__date_time, '%Y-%m-%dT%H:%M:%S')
        time_2 = datetime.datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S')
        time_diff = (time_2 - time_1)
        return int(time_diff.strftime('%H'))

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