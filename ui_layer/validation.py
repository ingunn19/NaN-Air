import string
import datetime
# from logic_layer.logic import LogicAPI

# LLapi = LogicAPI()
def ssn_validation(ssn):
    SSN_LENGTH = 10
    if len(ssn) != 10:
        print("ERROR! Invalid ssn")
        return False
    if len(ssn) == 10:
        try:
            int(ssn)
            return ssn
        except ValueError:
            print("ERROR! Cannot include letters.")
            return False


def name_validation(name):
    NAME_LENGTH = 50
    name_list = []
    if len(name) > NAME_LENGTH:
        return print("ERROR! Name too long.")
    if len(name) <= 0:
        return print("ERROR! Name too short")

    for x in name:
        if x in string.punctuation:
            return print("ERROR! Name cannot include punctuations.")
        try:
            int(x)
            return print("ERROR! Name cannot include numbers.")
        except ValueError:
            continue



def pilot_validation(pilot):
    ROLE = "pilot"

    if pilot == ROLE:
        return pilot
    else:
        print(f"ERROR! Invalid role.\nChoose the following role: {ROLE}")
        return False

def cabin_crew_validation(cabin_crew):
    ROLE = "cabin crew"

    if cabin_crew == ROLE:
        return cabin_crew
    else:
        print(f"ERROR! Invalid role.\nChoose the following role: {ROLE}")
        return False


def licence_validation(licence):
    LICENCE = "NAFokkerF100"
    LICENCE2 = "NAFokkerF28"
    LICENCE3 = "NABAE146"
    LICENCE_LIST = [LICENCE, LICENCE2, LICENCE3]

    if licence not in LICENCE_LIST:
        print(f"ERROR! Invalid licence.\nChoose from the following licences: {LICENCE}, {LICENCE2}, {LICENCE3}")
        return False


def email_vaidation(e_mail):
    e_mail_list = e_mail.split("@")
    if e_mail_list[1] == "nanair.com":
        return e_mail
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
        return gsm
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
    return address


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


def plane_type_ID_validation(plane_type_ID):
    LICENCE = "NAFokkerF100"
    LICENCE2 = "NAFokkerF28"
    LICENCE3 = "NABAE146"
    LICENCE_LIST = [LICENCE, LICENCE2, LICENCE3]

    if plane_type_ID not in LICENCE_LIST:
        print(f"ERROR! Invalid licence.\nChoose from the following: {LICENCE}, {LICENCE2}, {LICENCE3}")
        return False


def checker_worktrip(destination, departure, aircraftID, pilot, attendant):
    count = 0
    if LLapi.check_destination(destination):
        count += 1
    else:
        print("ERROR! Invalid destination.")
        return False

    if LLapi.check_departure(departure):
        count += 1
    else:
        print("ERROR! Invalid departure.")
        return False

    if LLapi.check_aircraftID(aircraftID):
        count += 1
    else:
        print("ERROR! Invalid aricraft ID.")
        return False

    if LLapi.check_pilot(pilot):
        count += 1
    else:
        print("ERROR! Invalid pilot.")
        return False

    if LLapi.check_attendant(attendant):
        count += 1
    else:
        print("ERROR! Invalid attendant.")
        return False
    if count == 5:
        return True


def checker_destination(destination_ID, destination, contact_name, contact_number):
    count = 0
    if LLapi.check_destination(destination):
        count += 1
    else:
        print("ERROR! Invalid destination.")
        return False

    if LLapi.check_destination_ID(destination_ID):
        count += 1
    else:
        print("ERROR! Invalid destination ID.")
        return False

    if LLapi.check_contact_name(contact_name):
        count += 1
    else:
        return print("ERROR! Invalid contact name.")

    if LLapi.check_contact_number(contact_number):
        count += 1
    else:
        print("ERROR! Invalid contact number.")
        return False
    if count == 4:
        return True


def checker_week_and_day(day, week):
    count = 0
    if LLapi.check_day(day):
        count += 1
    else:
        print("ERROR! Invalid date")
        return True

    if LLapi.check_week(week):
        count += 1
    else:
        print("ERROR! Invalid week.")
        return False
    if count == 2:
        return True

def checker_datetime(date):
    try:
        datetime_date = datetime.datetime.strptime(date, '%Y, %m, %d')
        return  True# print(datetime_date.strftime('%Y-%m-%d'))
    except:
        print("ERROR! Invalid date.")
        return False