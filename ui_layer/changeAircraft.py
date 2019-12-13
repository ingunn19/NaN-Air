from ui_layer.uiAPI import UI_API
from ui_layer.validation import plane_insignia_validation, plane_type_ID_validation
SPACER = "_______________________________________________________________________________________________________________________________________"
class ChangeAircraft:
    def __init__(self):
        self.__UI_API = UI_API()
        self.aircraft_insignia = ""
        self.aircraft = []

    def change_aircraft(self):
        print("Change aircraft info:")

        aircraft_insignia_checkker = False
        while aircraft_insignia_checkker == False:
            self.aircraft_insignia = input("Aircraft insignia: ")
            aircraft_insignia_checkker = plane_insignia_validation(self.aircraft_insignia)
        self.aircraft = self.__UI_API.get_specific_aircraft(self.aircraft_insignia)
        orginallist = self.aircraft.copy()

        aircraft_insignia_checkker = False
        while aircraft_insignia_checkker == False:
            self.aircraft[0] = input("New aircraft insignia: ")
            if self.aircraft[0] == "":
                self.aircraft[0] = orginallist[0]
            aircraft_insignia_checkker = plane_insignia_validation(self.aircraft[0])

        aircraft_type_checkker = False
        while aircraft_type_checkker == False:
            self.aircraft[1] = input("New aircraft type ID: ")
            if self.aircraft[1] == "":
                self.aircraft[1] = orginallist[1]
            aircraft_type_checkker = plane_type_ID_validation(self.aircraft[1])

        print(f"{self.aircraft[0]}    {self.aircraft[1]}")
        self.__UI_API.set_changes_for_existing_aircraft(self.aircraft, orginallist[0])