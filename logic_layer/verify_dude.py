from logic_layer.new_or_change_employee import AddNewOrChangeEmployee
from logic_layer.new_or_change_airplane import AddNewOrChangeAirplane
from logic_layer.new_or_change_destination import AddNewOrChangeDestinaion
from logic_layer.new_or_change_work_trip import AddNewOrChangeNewWorkTrip

#checks if the stuff existst (aka: line or an employee or something exists in the csv files)
#returns True if the stuff exists else None

def check_edit_employee(__employee_list):
    __employee = AddNewOrChangeEmployee()
    __id, __ssn, __name, __role, __licence, __address, __phonenumber, __email = __employee_list
    if __employee.check_ssn(__ssn) == None:
        return True

    else:
        return None
    # elif __employee.check_if_role_exists(__role) == None:
    #     return None
    #
    # elif __employee.check_if_licence_exists(__licence) == None:
    #     return None
    #
    # elif __employee.check_phone_number(__phonenumber) == None:
    #     return None
    #
    # elif __employee.check_email(__email) == None:
    #     return None
    #
    # else:
    #     return True


def check_edit_airplane(__airplane_list):
    __airplane = AddNewOrChangeAirplane()
    __planeInsignia, __planeTypeId = __airplane_list

    if __airplane.check_if_insignia_is_taken(__planeInsignia) == None:
        return True
    else:
        return None


def check_edit_worktrip_crew(__worktrip_list):
    __worktrip = AddNewOrChangeNewWorkTrip()
    __flightNumber, __departingFrom, __arrivingAt, __departuretime, __returntime, __aircraftID, __pilot1, __pilot2, __fa1,__fa2, __fa3 = __worktrip_list

    #add on later

def check_edit_destination(__dest_list):
    __destination = AddNewOrChangeDestinaion()
    identification, destination, travel_time, contact_name, contact_number = __dest_list

    if __destination.check_if_id_is_taken(identification) == None:
        return True
    else:
        return None






