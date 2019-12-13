import string
import datetime
from ui_layer.uiAPI import UI_API

UIapi = UI_API()
ll_validation = UIapi.get_logic_checker()

# Check input
def ssn_validation(ssn):
    SSN_LENGTH = 10
    if len(ssn) != SSN_LENGTH:
        print("ERROR! Invalid ssn")
        return False
    if len(ssn) == SSN_LENGTH:
        try:
            int(ssn)
            return True
        except ValueError:
            print("ERROR! Cannot include letters.")
            return False

def name_validation(name):
    NAME_LENGTH = 50
    if len(name) > NAME_LENGTH:
        print("ERROR! Name too long.")
        return False
    if len(name) <= 0:
        print("ERROR! Name too short")
        return False

    for x in name:
        if x in string.punctuation:
            print("ERROR! Name cannot include punctuations.")
            return False
        try:
            int(x)
            print("ERROR! Name cannot include numbers.")
            return False
        except ValueError:
            continue
    return True

def pilot_validation(pilot):
    ROLE = "pilot"

    if pilot == ROLE:
        return True
    else:
        print(f"ERROR! Invalid role.\nChoose the following role: {ROLE}")
        return False

def cabin_crew_validation(cabin_crew):
    ROLE = "cabincrew"

    if cabin_crew == ROLE:
        return True
    else:
        print(f"ERROR! Invalid role.\nChoose the following role: {ROLE}")
        return False

def email_validation(e_mail):
    e_mail_list = e_mail.split("@")
    if e_mail_list[1] == "nanair.com":
        return True
    else:
        print("ERROR! Invalid email.\nNot a corporate email.")
        return False

def phone_validation(gsm):
    gsm_list = []
    for x in gsm:
        gsm_list.append(x)
    gsm_count = 0
    for x in gsm_list:
        if x == "-":
            gsm_list.pop(gsm_count)
        gsm_count += 1
    gsm_string = "".join(gsm_list)
    try:
        int(gsm_string)
        return True
    except ValueError:
        print("ERROR! Gsm cannot include letters.")
        return False

def address_validation(address):
    for x in address:
        if x in string.punctuation:
            print("ERROR! Cannot include punctuations in address.")
            return False
        
    address_list = address.split(" ")
    for y in address_list[0]:
        try:
            int(y)
            print("ERROR! Cannot include numbers in first half of address.")
            return False
        except ValueError:
            continue
    return True

def time_validation(time):
    if type(time) == int:
        return True
    else:
        print("ERROR! Invalid time.")
        return False

def plane_insignia_validation(plane_insignia):
    PLANE_INSIGNIA = 6

    if len(plane_insignia) > PLANE_INSIGNIA:
        print("ERROR! Insignia too long.")
        return False
    if len(plane_insignia) < PLANE_INSIGNIA:
        print("ERROR! Insignia too short.")
        return False
    if plane_insignia[0] != "T":
        print("ERROR! Insignia invalid.")
        return False
    if plane_insignia[1] != "F":
        print("ERROR! Insignia invalid.")
        return False
    for x in plane_insignia:
        if plane_insignia[2] == "-":
            continue
        else:
            print("ERROR! Invalid insignia.\nRequires '-'")
            return False
    for x in plane_insignia:
        try:
            int(x)
            print("ERROR! Insignia cannot include numbers.")
            return False
        except ValueError:
            continue
    return True

def date_validation(date):
    try:
        datetime_date = datetime.datetime.strptime(date, '%Y, %m, %d')
        return True
    except:
        print("ERROR! Invalid date.")
        return False

def week_validation(week):
    if 1 <= week <= 52:
        return True
    else:
        print("ERROR! Invalid week.")
        return False

def employee_gsm_change(employee, gsm):
    if ll_validation.check_gsm_change_available(employee, gsm):
        return True
    else:
        print("ERROR! This phone number is already in use.")
        return False

def employee_email_change(employee, email):
    if ll_validation.check_gsm_change_available(employee, email):
        return True
    else:
        print("ERROR! This email is already in use.")
        return False

def contact_number_change(destination, number):
    if ll_validation.check_contact_number_change(destination, number):
        return True
    else:
        print("ERROR! This contact number is already in use.")


# Check if exists
def employee_validation(employee):
    if ll_validation.check_if_employee_exists(employee):
        return True
    else:
        print("ERROR! Invalid employee.")
        return False

def plane_type_ID_validation(plane_type_ID):
    if ll_validation.check_if_plane_type_exists(plane_type_ID):
        return True
    else:
        print("ERROR! Plane does not exist.")
        return False

def departure_validation(departure):
    if ll_validation.check_depart_time_availability(departure):
        return True
    else:
        print("ERROR! Departure time is not available.")
        return False

def aircraft_validation(aircraft):
    if ll_validation.check_if_insignia_exists(aircraft):
        return True
    else:
        print("ERROR! Invalid aricraft ID.")
        return False

def check_pilot_validation(pilot):
    if ll_validation.check_if_pilot(pilot):
        return True
    else:
        print("ERROR! Employee is not a pilot.")
        return False

def attendant_validation(attendant):
    if ll_validation.check_if_cabin_crew(attendant):
        return True
    else:
        print("ERROR! Employee is not a flight attendant.")
        return False

def destination_ID_validation(destination_ID):
    if ll_validation.check_if_destination_exists(destination_ID):
        return True
    else:
        print("ERROR! Invalid destination ID.")
        return False

def contact_number(contact_number):
    if ll_validation.check_if_contact_number_exists(contact_number):
        print("ERROR! This contact number is already in use.")
        return False
    else:
        return True

def role_validation(role):
    if ll_validation.check_if_role_exists(role):
        return True
    else:
        print("ERROR! Role does not exist.")
        return False

def check_employee_validation(employee, day):
    if ll_validation.check_employee_availability(employee, day):
        return True
    else:
        print("ERROR! Employee not available.")
        return False

def check_aircraft_validation(aircraft, depart_time):
    if ll_validation.check_aircraft_availability(aircraft, depart_time):
        return True
    else:
        print("ERROR! Aircraft not available.")
        return False

def pilot_licence_validation(pilot_id, plane_insignia):
    if ll_validation.check_pilot_licence(pilot_id, plane_insignia):
        return True
    else:
        print("ERROR! Pilot does not have licence for that aircraft.")
        return False

def employee_gsm_validation(employee_gsm):
    if ll_validation.check_if_phone_number_exists(employee_gsm):
        print("ERROR! This phonenumber is already in use.")
        return False
    else:
        return True

def employee_email_validation(employee_email):
    if ll_validation.check_if_email_exists(employee_email):
        print("ERROR! This email address is already in use.")
        return False
    else:
        return True

def is_ssn_available(ssn):
    if ll_validation.check_if_ssn_exists(ssn):
        print("ERROR! This ssn is already in use.")
        return False
    else:
        return True

def has_trip_happened(flight_id):
    if ll_validation.check_if_trip_is_finished(flight_id):
        print("ERROR! Please choose a work trip that has not concluded.")
        return False
    else:
        return True

def does_trip_exist(flight_id):
    if ll_validation.check_if_flight_id_exists(flight_id):
        return True
    else:
        print("ERROR! Invalid flight ID.")
        return False