from logic_layer.logic_parent import LogicParent

class AddNewOrChangeDestinaion(LogicParent):
    #checkers
    def check_if_id_is_taken(self, __id):
        all_destinations = self.destinations.read_file()
        for line in all_destinations:
            if __id in line:
                return None
        return True

    def check_if_destination_is_taken(self, __destination):
        all_destinations = self.destinations.read_file()
        for line in all_destinations:
            if __destination in line:
                return None
        return True

    def check_if_contact_number_is_taken(self, __contact_number):
        all_destinations = self.destinations.read_file()
        for line in all_destinations:
            if __contact_number in line:
                return None
        return True

    #adding
    def add_new_destination(self, __new_list):
        all_destinations = self.destinations.read_file()
        all_destinations.append(__new_list)
        self.destinations.write_file(all_destinations)

    #changing
    def replace_info(self, __destination_info_list):
        __all_destinations = self.destinations.read_file()
        for line in __all_destinations:
            if __destination_info_list[0] == line[0]:
                line = __destination_info_list
            else:
                return None
        self.destinations.write_file(__all_destinations)



