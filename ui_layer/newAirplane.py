from ui_layer.uiAPI import UI_API
from ui_layer.validation import plane_insignia_validation, plane_type_ID_validation
SPACER = "_____________________________________________"

class New_Airplane:
    def __init__(self):
        self.__UI_API = UI_API()
        self.Plane_Insignia = ""
        self.plane_type_Id = ""

    def New_Airplane(self):
        print("New airplane: ")

        Plane_Insignia_cheker = False
        while Plane_Insignia_cheker == False:
            self.Plane_Insignia = input("Plane Insignia: ").upper()
            Plane_Insignia_cheker = plane_insignia_validation(self.Plane_Insignia)

        plane_type_cheker = False
        while plane_type_cheker == False:
            self.plane_type_Id = input("plane type Id: ")
            plane_type_cheker = plane_type_ID_validation(self.plane_type_Id)

        print(SPACER)
        # Prenta út nýa flugvél
        self.__UI_API.set_airplane(self.Plane_Insignia, self.plane_type_Id)