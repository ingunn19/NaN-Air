from logic_layer.logic_parent import LogicParent

class AddNewAirplane(LogicParent):
    # checking
    def check_if_insignia_is_taken(self, __insignia):
        all_aircrafts = self.aircraft.read_file()
        for line in all_aircrafts:
            if __insignia in line:
                return None
        return True

    # adding
    def add_new_airplane(self, __airplane_info_list):
        all_aircrafts = self.aircraft.read_file()
        all_aircrafts.append(__airplane_info_list)
        self.aircraft.write_file(all_aircrafts)

    # changing
    def replace_info(self, __airplane_info_list):
        __all_aircrafts = self.aircraft.read_file()
        for line in __all_aircrafts:
            if __airplane_info_list[0] == line[0]:
                line = __airplane_info_list
            else:
                return None
        self.aircraft.write_file(__all_aircrafts)


