from ui_layer.uiAPI import UI_API
SPACER = "_____________________________________________"
class ChangeWorkTrip:
    def __init__(self):
        self.__UI_API = UI_API()
        self.flight_number = ""
        self.worktrip = []

    def change_workTrip(self):
        print("Change worktrip info:")
        self.flight_number = input("Flight number: ")
        self.worktrip = self.__UI_API.get_specific_worktrip(self.flight_number)
        original_list = self.worktrip.copy()

        self.worktrip[1] = input("Departing from: ")
        if self.worktrip[1] == "":
            self.worktrip[1] = original_list[1]

        self.worktrip[2] = input("Arriving at: ")
        if self.worktrip[2] == "":
            self.worktrip[2] = original_list[2]

        self.worktrip[3] = input("Departure: ")
        if self.worktrip[3] == "":
            self.worktrip[3] = original_list[3]

        self.worktrip[4] = input("Return: ")
        if self.worktrip[4] == "":
            self.worktrip[4] = original_list[4]

        self.worktrip[5] = input("Aircraft ID: ")
        if self.worktrip[5] == "":
            self.worktrip[5] = original_list[5]

        self.worktrip[6] = input("Pilot1: ")
        if self.worktrip[6] == "":
            self.worktrip[6] = original_list[6]

        self.worktrip[7] = input("Pilot2: ")
        if self.worktrip[7] == "":
            self.worktrip[7] = original_list[7]

        self.worktrip[8] = input("Cabin crew1: ")
        if self.worktrip[8] == "":
            self.worktrip[8] = original_list[8]

        self.worktrip[9] = input("Cabin crew2: ")
        if self.worktrip[9] == "":
            self.worktrip[9] = original_list[9]

        self.worktrip[10] = input("Cabin crew3: ")
        if self.worktrip[10] == "":
            self.worktrip[10] = original_list[10]
        # Hér væri gott að sýna breytingar
        self.__UI_API.set_changes_for_existing_worktrip(self.worktrip)
