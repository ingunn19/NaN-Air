import string
import datetime
from ui_layer.uiAPI import UI_API

UIapi = UI_API()

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
    ROLE = "cabin crew"

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

# Check if exists
def employee_validation(employee):
    if UIapi.check_employee(employee):
        return True
    else:
        print("ERROR! Invalid employee.")
        return False

def plane_type_ID_validation(plane_type_ID):
    if UIapi.check_planeID(plane_type_ID):
        return True
    else:
        print("ERROR! Plane does not exist.")
        return False

def departure_validation(departure):
    if UIapi.check_departure(departure):
        return True
    else:
        print("ERROR! Invalid departure.")
        return False

def aircraft_validation(aircraft):
    if UIapi.check_aircraftID(aircraft):
        return True
    else:
        print("ERROR! Invalid aricraft ID.")
        return 

def check_pilot_validation(pilot):
    if UIapi.check_pilot(pilot):
        return True
    else:
        print("ERROR! Invalid pilot.")
        return False

def attendant_validation(attendant):
    if UIapi.check_attendant(attendant):
        return True
    else:
        print("ERROR! Invalid attendant.")
        return False

def destination_ID_validation(destination_ID):
    if UIapi.check_destination_ID(destination_ID):
        return True
    else:
        print("ERROR! Invalid destination ID.")
        return False

def contact_number(contact_number):
    if UIapi.check_contact_number(contact_number):
        return True
    else:
        print("ERROR! Invalid contact number.")
        return False

def role_validation(role):
    if UIapi.check_role_validation(role_validation):
        return True
    else:
        print("ERROR! Role does not exist.")
        return False

def check_employee_validation(employee):
    if UIapi.check_employee_validation(employee_validation):
        return True
    else:
        print("ERROR! Employee not available.")
        return False

def check_aircraft_validation(aircraft):
    if UIapi.check_aircraft_validation(aircraft_validation):
        return True
    else:
        print("ERROR! Aircraft not available.")
        return False

def pilot_licence_validation(pilot_licence):
    if UIapi.check_pilot_licence_validation(pilot_licence_validation):
        return True
    else:
        print("ERROR! Pilot does not have licence for that aircraft.")
        return False

def employee_gsm_validation(employee_gsm):
    if UIapi.check_employee_gsm_validation(employee_gsm_validation):
        print("ERROR! This phonenumber is already in use.")
        return False
    else:
        return True

def employee_email_validation(employee_email):
    if UIapi.check_employee_email_validation(employee_email_validation):
        print("ERROR! This email address is already in use.")
        return False
    else:
        return True

def is_ssn_available(ssn):
    if UIapi.check_if_ssn_exists(ssn):
        print("ERROR! This phonenumber is already in use.")
        return False
    else:
        return True