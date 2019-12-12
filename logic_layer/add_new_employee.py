from logic_layer.logic_parent import LogicParent

class AddNewEmployee(LogicParent):
    def check_ssn(self, ssn):
        __all_employee_list = self.crew.read_file()
        for line in __all_employee_list:
            if ssn in line:
                return None
        return True

    def check_if_role_exists(self, role):
        __all_employee_list = self.crew.read_file()
        for line in __all_employee_list:
            if role in line:
                return True
        return None

    def check_if_licence_exists(self, licence):
        __airplane_list = self.aircraft.read_file()
        if licence == "N/A":
            return True
        else:
            for line in __airplane_list:
                if licence in line:
                    return True

    def check_phone_number(self, phone_number):
        __all_employee_list = self.crew.read_file()
        for line in __all_employee_list:
            if phone_number in line:
                return None
        return True

    def check_email(self, email):
        __all_employee_list = self.crew.read_file()
        for line in __all_employee_list:
            if email in line:
                return None
        return True

    def get_new_employee_id(self):
        __all_employee_list = self.crew.read_file()
        __new_id = str(int(__all_employee_list[-1][0]) + 1)
        return __new_id

    def add_new_employee(self, employee_info_list):
        classObject = AddNewEmployee()
        __all_employee_list = self.crew.read_file()
        employee_info_list.insert(0, '')
        __employee_id = classObject.get_new_employee_id()
        employee_info_list[0] = __employee_id
        __all_employee_list.append(employee_info_list)
        self.crew.write_file(__all_employee_list)

    def replace_info(self, employee_info_list):
        __all_employee_list = self.crew.read_file()
        __employee_id = employee_info_list[0]
        for line in __all_employee_list:
            if __employee_id in line:
                line = employee_info_list
            else:
                return None


