from logic_layer.logic_parent import LogicParent

class AddNewOrChangeEmployee(LogicParent):
    def get_new_employee_id(self):
        __all_employee_list = self.crew.read_file()
        __new_id = str(int(__all_employee_list[-1][0]) + 1)
        return __new_id

    # Adding
    def add_new_employee(self, employee_info_list):
        classObject = AddNewOrChangeEmployee()
        __all_employee_list = self.crew.read_file()
        employee_info_list.insert(0, '')
        __employee_id = classObject.get_new_employee_id()
        employee_info_list[0] = __employee_id
        __all_employee_list.append(employee_info_list)
        self.crew.write_file(__all_employee_list)

    # Changing
    def replace_info(self, employee_info_list):
        __all_employee_list = self.crew.read_file()
        __employee_id = employee_info_list[0]
        for line in __all_employee_list:
            if __employee_id in line:
                __all_employee_list[__all_employee_list.index(line)] = employee_info_list
        self.crew.write_file(__all_employee_list)


