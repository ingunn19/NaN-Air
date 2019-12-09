from UI_API import UI_Api
SPACER = "_____________________________________________"
class New_Airplane:
    def __init__(self):
        self.__UI_API = UI_Api()
        self.Plane_Insignia = ""
        self.plane_type_Id = ""

    def New_Airplane(self):

        print("New airplane: ")
        self.Plane_Insignia = input("Plane Insignia: ").upper()
        self.plane_type_Id = input("plane type Id: ")
        print(SPACER)
        # Villuchekka
        # Prenta út nýa flugvél
        self.__UI_API.set_airplane(self.Plane_Insignia, self.plane_type_Id)