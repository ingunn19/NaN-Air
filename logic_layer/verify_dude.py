from validation_checker import ValitationChecker

#checks if the stuff existst (aka: line or an employee or something exists in the csv files)
#returns True if the stuff exists else None

validate = ValitationChecker()

def check_edit_employee(__employee_list):
    __id, __ssn, __name, __role, __licence, __address, __phonenumber, __email = __employee_list
    if validate.check_if_exists(__ssn) == None:
        return True

    elif validate.check_if_role_exists(__role) == None:
        return None
    
    elif validate.check_if_licence_exists(__licence) == None:
        return None
    
    elif validate.check_phone_number(__phonenumber) == None:
        return None
    
    elif validate.check_email(__email) == None:
        return None

    else:
        return True


def check_edit_airplane(__airplane_list):
    __planeInsignia, __planeTypeId = __airplane_list
    if validate.check_if_insignia_is_taken(__planeInsignia) == None:
        return True
    else:
        return None


def check_edit_worktrip_crew(__worktrip_list):
    __worktrip = AddNewOrChangeNewWorkTrip()
    __flightNumber, __departingFrom, __arrivingAt, __departuretime, __returntime, __aircraftID, __pilot1, __pilot2, __fa1,__fa2, __fa3 = __worktrip_list

    #add on later

def check_edit_destination(__dest_list):
    identification, destination, travel_time, contact_name, contact_number = __dest_list

    if validate.check_if_id_is_taken(identification) == None:
        return True
    else:
        return None






