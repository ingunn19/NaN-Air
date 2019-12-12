from logic_layer.logic_parent import LogicParent

class AddNewaircaft(LogicParent):

    def check_if_insignia_is_taken(self, __insignia):
        all_aircrafts = self.aircraft.read_file()
        for line in all_aircrafts:
            if __insignia in line:
                return None
        return True

    #adding
    def add_aircraft(self, __planeInsignia, __planeTypeId):
        all_aircrafts = self.aircraft.read_file()
        new_aircraft = [__planeInsignia, __planeTypeId]
        all_aircrafts.append(new_aircraft)
        self.aircraft.write_file(all_aircrafts)

    #changing
    def replace_info(self, __new_list):
        self.aircraft.write_file(__new_list)


