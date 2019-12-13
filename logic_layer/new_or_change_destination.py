from logic_layer.logic_parent import LogicParent

class AddNewOrChangeDestinaion(LogicParent):
    # Adding
    def add_new_destination(self, __new_list):
        all_destinations = self.destinations.read_file()
        all_destinations.append(__new_list)
        self.destinations.write_file(all_destinations)

    # Changing
    def replace_info(self, __destination_info_list):
        __all_destinations = self.destinations.read_file()
        for line in __all_destinations:
            if __destination_info_list[0] == line[0]:
                __all_destinations[__all_destinations.index(line)] = __destination_info_list
        self.destinations.write_file(__all_destinations)



