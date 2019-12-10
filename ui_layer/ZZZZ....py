from logic_layer.LogicLayerTest import LogicAPI
from datetime import date, timedelta, datetime

classObject = LogicAPI()
print("------------------------------------------------------------------------------------------------------------")
print("All employees")
test_listi1a = classObject.req_overview_allemployees()
for line in test_listi1a:
    id, name, role, licence, address, phonenumber, email, eight = line
    print(f'{id:4}{name:15}{role:22}{licence:12}{address:18}{phonenumber:17}{email:14}{eight}')

print("------------------------------------------------------------------------------------------------------------")
print("req_overview_pilots")
test_listi1b = classObject.req_overview_pilots()
for line in test_listi1b:
    id, name, role, licence, address, phonenumber, email, eight = line
    print(f'{id:4}{name:15}{role:22}{licence:12}{address:18}{phonenumber:17}{email:14}{eight}')
print("------------------------------------------------------------------------------------------------------------")
print("req_overview_flightattendants")
test_listi1c = classObject.req_overview_flightattendants()
for line in test_listi1c:
    id, name, role, licence, address, phonenumber, email, eight = line
    print(f'{id:4}{name:15}{role:22}{licence:12}{address:18}{phonenumber:17}{email:14}{eight}')
print("------------------------------------------------------------------------------------------------------------")

print('Employee Info')
#test for employee_overview stuff
test_listi1d = classObject.picking_employee_personal_det(8)

for line in test_listi1d:
    id, name, role, licence, address, phonenumber, email, eight = line
    print(f'{id:4}{name:15}{role:22}{licence:12}{address:17}{phonenumber:17}{email:14}{eight}')

print("------------------------------------------------------------------------------------------------------------")
print("Picking_employee_work_overview_week")
test_listi2 = classObject.picking_employee_work_overview_week(ID, Year, week)
for line in test_listi2:
    flightNumber, departingFrom, arrivingAt, departure_time, return_time, aircraftID, pilot1, pilot2, fa1, fa2,fa3=line
    print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
print("------------------------------------------------------------------------------------------------------------")
print("Employee_with_task")
test_listi3 = classObject.all_employees_with_task("2019-11-24")
print('Employee Id: ', end="")
for ch in test_listi3:
    print(ch, end=" ")
print("\n")
print("------------------------------------------------------------------------------------------------------------")
print("Employee_not_with_task")
test_listi4 = classObject.all_employees_not_with_task("2019-11-24")
print('Employee Id: ', end="")
for ch in test_listi4:
    print(ch, end=" ")
print("\n")
print("------------------------------------------------------------------------------------------------------------")
print("Pilots with licence on one plane")
test_listi5 = classObject.all_pilots_with_licence_on_an_given_plane("NAFokkerF100")
for line in test_listi5:
    id, ssn, name, role, licence, address, phonenumber, email = line
    print(f"{id:4}{ssn:12}{name:52}{role:15}{licence:20}{address:20}{phonenumber:15}{email:100}")
print("------------------------------------------------------------------------------------------------------------")
print("Pilots with licence")
test_listi6 = classObject.all_pilots_with_licences_all_planes()
for line in test_listi6:
    id,ssn,name,role,licence,address,phonenumber,email= line
    print(f"{id:4}{ssn:12}{name:52}{role:15}{licence:20}{address:20}{phonenumber:15}{email:100}")
print("------------------------------------------------------------------------------------------------------------")
print("All worktrips")
test_listi7 = classObject.all_worktrips()
counter = 0
for line in test_listi7:
    flightNumber,departingFrom,arrivingAt,departure_time,return_time,aircraftID,pilot1,pilot2,fa1,fa2,fa3=line
    print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
print("------------------------------------------------------------------------------------------------------------")
print("All worktrips in given year,week")
test_listi8 = classObject.get_week_of_worktrip(2019, 47)
for line in test_listi8:
    flightNumber,departingFrom,arrivingAt,departure_time,return_time,aircraftID,pilot1,pilot2,fa1,fa2,fa3=line
    print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
print("------------------------------------------------------------------------------------------------------------")
print("All worktrips in given date")
test_listi9a = classObject.worktrips_of_the_day("2019-11-24")
for line in test_listi9a:
    flightNumber,departingFrom,arrivingAt,departure_time,return_time,aircraftID,pilot1,pilot2,fa1,fa2,fa3=line
    print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
print("------------------------------------------------------------------------------------------------------------")
print("All worktrips of the day")
test_listi9b = classObject.worktrips_of_the_day("2019-11-20")
for line in test_listi9b:
    flightNumber,departingFrom,arrivingAt,departure_time,return_time,aircraftID,pilot1,pilot2,fa1,fa2,fa3=line
    print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
print("------------------------------------------------------------------------------------------------------------")
print("Single worktrip")
test_listi9c = classObject.singe_worktrip("100")
for line in test_listi9c:
    flightNumber,departingFrom,arrivingAt,departure_time,return_time,aircraftID,pilot1,pilot2,fa1,fa2,fa3=line
    print(f"{flightNumber:14}{departingFrom:15}{arrivingAt:12}{str(departure_time):21}{str(return_time):21}{aircraftID:12}{pilot1:8}{pilot2:8}{fa1:5}{fa2:5}{fa3:5}")
print("------------------------------------------------------------------------------------------------------------")
print("All destinaions")
test_listi10 = classObject.all_destinations()
for line in test_listi10:
    id, destination, travel_time, contact_name, contact_number = line
    print(f"{id:4}{destination:15}{travel_time:13}{contact_name:17}{contact_number:10}")

print("------------------------------------------------------------------------------------------------------------")
print("One destinaion")
test_listi11 = classObject.one_destination("LYR")
for line in test_listi11:
    id, destination, travel_time, contact_name, contact_number = line
    print(f"{id:4}{destination:15}{travel_time:13}{contact_name:17}{contact_number:10}")
print("------------------------------------------------------------------------------------------------------------")
print("All airplane")
test_listi12 = classObject.all_planes()
for line in test_listi12:
    planeInsignia, planetypeId = line
    print(f"{planeInsignia:<15}{planetypeId}")

print("------------------------------------------------------------------------------------------------------------")
print("Single airplanes")
test_listi13 = classObject.single_plane("TF-XUP")
for line in test_listi13:
    planeInsignia, planetypeId = line
    print(f"{planeInsignia:<15}{planetypeId}")
print("------------------------------------------------------------------------------------------------------------")
print("State of planes")
test = classObject.state_of_plane("2019-11-02T14:21:00")
for line in test:
    planeType, planeInsignia, status, next_available, destination, flightNumber = line
    print(f"{planeInsignia:15}{planeType:15}{status:14}{str(next_available):20}{destination:13}{flightNumber}")

















