from data_layer.dataLayer import DataAPI

class LogicParent():
    def __init__(self):
        self.crew = DataAPI("Crew")
        self.aircraft = DataAPI("Aircraft")
        self.destinations = DataAPI("Destinations")
        self.flight_records = DataAPI("FlightRecords")