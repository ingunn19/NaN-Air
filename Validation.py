import string
import datetime

def ssn_validation(ssn):
    SSN_LENGTH = 10
    if len(ssn) != 10:
        return print("ERROR! Invalid ssn")
    if len(ssn) == 10:
        try:
            int(ssn)
            return ssn
        except ValueError:
            return print("ERROR! Cannot include letters.")

def name_validation(name):
    NAME_LENGTH = 50
    name_list = []
    if len(name) > NAME_LENGTH:
        return print("ERROR! Name too long.")
    if len(name) <= 0:
        return print("ERROR! Name too short")
    for x in name:
        try:
            integer = int(x)
            return print("ERROR! Name cannot include numbers.")
        except ValueError:
            return name
        if x == string.punctuation:
            return print("ERROR! Name cannot include punctuations.")

def role_validation(role):
    ROLE = "Pilot"
    ROLE2 = "Cabin crew"

    if role == ROLE or role == ROLE2:
        return role
    else:
        return print(f"ERROR! Invalid role.\nChoose from the following roles: {ROLE}, {ROLE2}")

def licence_validation(licence):
    LICENCE = "NAFokkerF100"
    LICENCE2 = "NAFokkerF28"
    LICENCE3 = "NABAE146"
    LICENCE_LIST = [LICENCE, LICENCE2, LICENCE3]

    if licence not in LICENCE_LIST:
        return print(f"ERROR! Invalid licence.\nChoose from the following licences: {LICENCE}, {LICENCE2}, {LICENCE3}")

def email_vaidation(e_mail):

    e_mail_list = e_mail.split("@")
    if e_mail_list[1] == "nanair.com":
        return e_mail
    else:
        return print("ERROR! Invalid email.\nNot a corporate email.")

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
        return print("ERROR! Gsm cannot include letters.")

def plane_insignia_validation(plane_insignia):
    PLANE_INSIGNIA = 6

    insignia_list = []
    if len(plane_insignia) > PLANE_INSIGNIA:
        return print("ERROR! Insignia too long.")
    if len(plane_insignia) < PLANE_INSIGNIA:
        return print("ERROR! Insignia too short.")
    if plane_insignia[0] != "T":
        return print("ERROR! Insignia invalid.")
    if plane_insignia[1] != "F":
        return print("ERROR! Insignia invalid.")
    for x in plane_insignia:
        if plane_insignia[2] == "-":
            continue
        else:
            return print("ERROR! Invalid insignia.\nRequires '-'")
    for x in plane_insignia:
        try:
            integer = int(x)
            return print("ERROR! Insignia cannot include numbers.")
        except ValueError:
            continue

def plane_type_ID_validation(plane_type_ID):
    LICENCE = "NAFokkerF100"
    LICENCE2 = "NAFokkerF28"
    LICENCE3 = "NABAE146"
    LICENCE_LIST = [LICENCE, LICENCE2, LICENCE3]

    if plane_type_ID not in LICENCE_LIST:
        return print(f"ERROR! Invalid licence.\nChoose from the following: {LICENCE}, {LICENCE2}, {LICENCE3}")

def checker_worktrip(destination, departure, aircraftID, pilot, attendant):
    if LLapi.check_destination(destination):
        return
    else:
        return print("ERROR! Invalid destination.")

    if LLapi.check_departure(departure):
        return
    else:
        return print("ERROR! Invalid departure.")

    if LLapi.check_aircraftID(aircraftID):
        return
    else:
        return print("ERROR! Invalid aricraft ID.")

    if LLapi.check_pilot(pilot):
        return
    else:
        return print("ERROR! Invalid pilot.")

    if LLapi.check_attendant(attendant):
        return
    else:
        return print("ERROR! Invalid attendant.")

def checker_destination(destination_ID, destination, contact_name, contact_number):
    if LLapi.check_destination(destination):
        return
    else:
        return print("ERROR! Invalid destination.")

    if LLapi.check_destination_ID(destination_ID):
        return
    else:
        return print("ERROR! Invalid destination ID.")

    if LLapi.check_contact_name(contact_name):
        return
    else:
        return print("ERROR! Invalid contact name.")

    if LLapi.check_contact_number(contact_number):
        return
    else:
        return print("ERROR! Invalid contact number.")

def checker_week_and_day(day, week):
    if LLapi.check_day(day):
        return
    else:
        return print("ERROR! Invalid date")
    
    if LLapi.check_week(week):
        return
    else:
        return print("ERROR! Invalid week.")

def checker_datetime(date):
    try:
        datetime_date = datetime.datetime.strptime(date, '%Y, %m, %d')
        return #print(datetime_date.strftime('%Y-%m-%d'))
    except:
        return print("ERROR! Invalid date.")


def main():
    ssn = "9807g54455"
    check = ssn_validation(ssn)

main()