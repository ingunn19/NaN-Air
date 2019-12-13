from logic_layer.logic_parent import LogicParent

class AddNewOrChangeAirplane(LogicParent):
    # Adding
    def add_new_airplane(self, __airplane_info_list):
        all_aircrafts = self.aircraft.read_file()
        all_aircrafts.append(__airplane_info_list)
        self.aircraft.write_file(all_aircrafts)

    # Changing
    def replace_info(self, __airplane_info_list, original_ID):
        __all_aircrafts = self.aircraft.read_file()
        for line in __all_aircrafts:
            if original_ID == line[0]:
                line = __airplane_info_list
        self.aircraft.write_file(__all_aircrafts)