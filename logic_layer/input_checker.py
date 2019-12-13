import string
import datetime


def ssn_format_check(ssn):
    SSN_LENGTH = 10
    if len(ssn) != SSN_LENGTH:
        return False
    if len(ssn) == SSN_LENGTH:
        try:
            int(ssn)
            return True
        except ValueError:
            return False

def name_format_check(name):
    NAME_LENGTH = 50
    if len(name) > NAME_LENGTH:
        return False
    if len(name) <= 0:
        return False
    for x in name:
        if x in string.punctuation:
            return False
        try:
            int(x)
            return False
        except ValueError:
            continue
    return True

def email_format_check(e_mail):
    e_mail_list = e_mail.split("@")
    if e_mail_list[1] == "nanair.com":
        return True
    else:
        return False

def phone_format_check(gsm):
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
        return False

def address_format_check(address):
    for x in address:
        if x in string.punctuation:
            return False
        
    address_list = address.split(" ")
    for y in address_list[0]:
        try:
            int(y)
            return False
        except ValueError:
            continue
    return True

def plane_insignia_format_check(plane_insignia):
    PLANE_INSIGNIA = 6

    if len(plane_insignia) > PLANE_INSIGNIA:
        return False
    if len(plane_insignia) < PLANE_INSIGNIA:
        return False
    if plane_insignia[0] != "T":
        return False
    if plane_insignia[1] != "F":
        return False
    for x in plane_insignia:
        if plane_insignia[2] == "-":
            continue
        else:
            return False
    for x in plane_insignia:
        try:
            int(x)
            return False
        except ValueError:
            continue
    return True

def date_format_check(date):
    try:
        datetime_date = datetime.datetime.strptime(date, '%Y, %m, %d')
        return True
    except:
        return False

def week_format_check(week):
    if 1 <= week <= 52:
        return True
    else:
        return False