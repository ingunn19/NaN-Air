class WorkTrip():
    def __init__(self, flight_id, depart_from, arrive_at, depart_time, return_time, plane_insignia='', pilot1='', pilot2='', fa1='', fa2='', fa3=''):
        self.__flight_id = flight_id
        self.__depart_from = depart_from
        self.__arrive_at = arrive_at
        self.__depart_time = depart_time
        self.__return_time = return_time
        self.__plane_insignia = plane_insignia
        self.__pilot1 = pilot1
        self.__pilot2 = pilot2
        self.__fa1 = fa1
        self.__fa2 = fa2
        self.__fa3 = fa3

    def __str__(self):
        return f"{self.__flight_id}, {self.__depart_from}, {self.__arrive_at}, {self.__depart_time}, {self.__return_time}, {self.__plane_insignia}, {self.__pilot1}, {self.__pilot2}, {self.__fa1}, {self.__fa2}, {self.__fa2}"

# Getters

    def get_flight_id(self):
        return self.__flight_id

    def get_departure(self):
        return self.__depart_from

    def get_destination(self):
        return self.__arrive_at

    def get_depart_time(self):
        return self.__depart_time

    def get_plane_insignia(self):
        return self.__plane_insignia

    def get_pilot1(self):
        return self.__pilot1

    def get_pilot2(self):
        return self.__pilot2

    def get_fa1(self):
        return self.__fa1

    def get_fa2(self):
        return self.__fa2

    def get_fa3(self):
        return self.__fa3

# Setters

    def set_flight_id(self, new_flight_id):
        self.__flight_id = new_flight_id

    def set_derpart_from(self, new_depart_from):
        self.__depart_from = new_depart_from

    def set_destination(self, new_arrive_at):
        self.__arrive_at = new_arrive_at

    def set_depart_time(self, new_depart_time):
        self.__depart_time = new_depart_time

    def set_plane_insignia(self, new_plane_insignia):
        self.__plane_insignia = new_plane_insignia

    def set_pilot1(self, new_pilot1):
        self.__pilot1 = new_pilot1

    def set_pilot2(self, new_pilot2):
        self.__pilot2 = new_pilot2

    def set_fa1(self, new_fa1):
        self.__fa1 = new_fa1

    def set_fa2(self, new_fa2):
        self.__fa2 = new_fa2

    def set_fa3(self, new_fa3):
        self.__fa3 = new_fa3