from data_layer.dataLayer import DataAPI

class LogicParent():
    def __init__(self):
        self.__crew = DataAPI("Crew")
        self.__aircraft = DataAPI("Aircraft")
        self.__destinations = DataAPI("Destinations")
        self.__flight_records = DataAPI("FlightRecords")