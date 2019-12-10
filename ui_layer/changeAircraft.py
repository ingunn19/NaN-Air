from ui_layer.uiAPI import UI_API
SPACER = "_____________________________________________"
class ChangeAircraft:
    def __init__(self):
        self.__UI_API = UI_API()
        self.aircraft_insignia = ""
        self.aircraft = []

    def change_aircraft(self):
        print("Change aircraft info:")
        self.aircraft_insignia = input("Aircraft insignia: ")
        self.aircraft = self.__UI_API.get_specific_aircraft(self.aircraft_insignia)
        orginallist = self.aircraft.copy()
        print(self.aircraft)
        self.aircraft[0] = input("New aircraft insignia: ")
        if self.aircraft[0] == "":
            self.aircraft[0] = orginallist[0]
        self.aircraft[1] = input("New aircraft type ID: ")
        if self.aircraft[1] == "":
            self.aircraft[1] = orginallist[1]
        print(self.aircraft)
        self.__UI_API.set_changes_for_existing_aircraft(self.aircraft)
