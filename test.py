from data_layer.dataLayer import DataAPI

flight_records = DataAPI("FlightRecords")

__employee_id = "14"
__day = "2019-12-13T20:30:00"
__flight_list = flight_records.read_file()
for line in __flight_list:
    if __day[:10] == (line[3][:10] or line[4][:10]):
        if __employee_id in line:
            print("False")
            break
    print("True")

# for line in __flight_list:
#     print(line)