# Employee/pilot/attendant

#parent classi fyrir flugmenn og flugþjóna, það er möguleiki á því að við þurfum, ekki þennan parent en hann er allavegana til
class Employee:
    def __init__(self, name, employee_ssn, employee_id, adress, email, gsm):
        self.name = name
        self.employee_ssn = employee_ssn
        self.employee_id = employee_id
        self.adress = adress
        self.email = email
        self.gsm = gsm

class Pilot(Employee):
    def __init__(self, name, licence, employee_ssn, employee_id, adress, email, gsm):
        super().__init__(name, employee_ssn, employee_id, adress, email, gsm)
        self.pilot_name = name
        self.pilot_licence = licence
        self.pilot_ssn = employee_ssn
        self.pilot_id = employee_id
        self.pilot_adress = adress
        self.pilot_email = email
        self.pilot_gsm = gsm

    #Pilot Getters
    def get_pilot_name(self):
        return self.pilot_name

    def get_pilot_licence(self):
        return self.pilot_licence

    def get_pilot_ssn(self):
        return self.pilot_ssn

    def get_pilot_adress(self):
        return self.pilot_adress

    def get_pilot_id(self):
        return self.pilot_id

    def get_pilot_email(self):
        return self.pilot_email

    def get_pilot_gsm(self):
        return self.pilot_gsm

    #Pilot Setters
    # Commentaði út nafn og kennitölu svo ekki sé hægt að breyta þeim í keyrslu
    """
    def set_pilot_name(self, new_name):
        self.pilot_name = new_name

    def set_pilot_licence(self, new_licence):
        self.pilot_licence = new_licence"""

    def set_pilot_ssn(self, new_ssn):
        self.pilot_ssn = new_ssn

    def set_pilot_id(self, new_id):
        self.pilot_id = new_id

    def set_pilot_adress(self, new_adress):
        self.pilot_adress = new_adress

    def set_pilot_email(self, new_email):
        self.pilot_email = new_email

    def set_pilot_gsm(self, new_gsm):
        self.pilot_gsm = new_gsm

    def __str__(self):
        return f"{self.pilot_name} {self.pilot_licence} {self.pilot_ssn} {self.pilot_id} {self.pilot_adress} {self.pilot_email} {self.pilot_gsm}"

class FlightAttendant(Employee):
    def __init__(self, name, employee_ssn, employee_id, adress, email, gsm):
        super().__init__(name, employee_ssn, employee_id, adress, email, gsm)
        self.attendant_name = name
        self.attendant_ssn = employee_ssn
        self.attendant_id = employee_id
        self.attendant_adress = adress
        self.attendant_email = email
        self.attendant_gsm = gsm

    #Attendant Getters
    def get_attendant_name(self):
        return self.attendant_name

    def get_attendant_ssn(self):
        return self.attendant_ssn

    def get_attendant_id(self):
        return self.attendant_id

    def get_attendant_adress(self):
        return self.attendant_adress

    def get_attendant_email(self):
        return self.attendant_email

    def get_attendant_gsm(self):
        return self.attendant_gsm

    #Attendant Setters
    #Commentaði út nafn og kennitölu svo ekki sé hægt að breyta þeim í keyrslu
    """def set_attendant_name(self, new_name):
        self.attendant_name = new_name

    def set_attendant_ssn(self, new_ssn):
        self.attendant_ssn = new_ssn"""

    def set_adress(self, new_adress):
        self.attendant_adress = new_adress

    def set_attendant_id(self, new_id):
        self.attendant_id = new_id
    def set_attendant_email(self, new_email):
        self.attendant_email = new_email

    def set_attendant_gsm(self, new_gsm):
        self.attendant_gsm = new_gsm

    def __str__(self):
        return f"{self.attendant_name} {self.attendant_ssn} {self.attendant_id} {self.attendant_adress} {self.attendant_email} {self.attendant_gsm}"