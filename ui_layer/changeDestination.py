from ui_layer.uiAPI import UI_API
SPACER = "_____________________________________________"
class ChangeDestination:
    def __init__(self):
        self.__UI_API = UI_API()
        self.destination_name = ""
        self.destination = []
    def change_destination(self):
        print("Change destination info:")
        self.destination_name = input("Destination: ")
        self.destination = self.__UI_API.get_specific_destination(self.destination_name)
        originallist = self.destination.copy()
        print(self.destination)
        self.destination[2] = input("New emergency contact name: ")
        if self.destination[2] == "":
            self.destination[2] = originallist[2]
        self.destination[3] = input("New emergency contact GSM: ")
        if self.destination[3] == "":
            self.destination[3] = originallist[3]
        print(self.destination)
        self.__UI_API.set_changes_for_existing_destination(self.destination)