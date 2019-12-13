from datetime import datetime, timedelta
from logic_layer.overview_worktrips import WorkTripOverviewLogic
from logic_layer.logic_parent import LogicParent

class PlaneOverviewLogic(LogicParent):
#overview airplanes
    def req_all_planes(self):
        #getting all planes
        __all_planes = self.aircraft.read_file()
        # if len(__all_planes) <= 1:
        #     return None
        return __all_planes

    def req_single_plane(self, plane_insignia):
        __all_planes = self.aircraft.read_file()
        return_list = []
        return_list.append(__all_planes[0])
        for line in __all_planes:
            if line[0] == plane_insignia:
                return_list.append(line)
                return return_list
        return None

    def req_state_of_planes(self, date_input):
        #importing all planes
        tripData = WorkTripOverviewLogic()
        planeData = PlaneOverviewLogic()
        __list_of_all_planes = planeData.req_all_planes()
        __list_of_all_planes.pop(0)
        __list_of_avalible_planes_insignia = []

        #taking only the insignia an appending it to the list
        for line in __list_of_all_planes:
            __list_of_avalible_planes_insignia.append(line[0])

        #importing all worktrips
        __list_of_all_worktrips = tripData.req_all_worktrips()

        #making the date  an isoformat
        date_iso_format = datetime.strptime(date_input, '%Y-%m-%dT%H:%M:%S')

        #making the final list
        __final_list = []
        __final_list.append(['Plane type', 'Plane insignia', 'Status', 'Next available', 'Destination', 'Flight number'])
        __list_of_all_worktrips.pop(0)

        #parsing
        for line in __list_of_all_worktrips:
            #getting the planetype name fokker300...
            for plane_row in __list_of_all_planes:
                if line[5] in plane_row:
                    planeType = plane_row[1]
            departure = line[3]
            arrival = line[4]

            # if date is between dep. and (arrival + 1hr) then is aircraft is unavailable.
            # if datetime.strptime(departure, '%Y-%m-%dT%H:%M:%S') <= date_iso_format <= ((datetime.strptime(arrival, '%Y-%m-%dT%H:%M:%S')) + timedelta(hours=1)):
            if departure <= date_iso_format <= arrival + timedelta(hours=1):
                #making all of the attributes that go to the list
                next_available = line[4] + timedelta(hours=1)
                planeinsignia = line[5]
                destination = line[2]
                flightnumber = line[0]
                #placing the attributes into the list
                __final_list.append([planeType, planeinsignia, 'In Use', next_available, destination, flightnumber])

                #removing the plane insignia from the avalible planes.
                try:
                    __list_of_avalible_planes_insignia.remove(line[5])
                except ValueError:
                    continue

        for plane_insignia in __list_of_avalible_planes_insignia:
            # getting the planetype name fokker300...
            for plane_row in __list_of_all_planes:
                if plane_insignia in plane_row:
                    planeType = plane_row[1]

            __final_list.append([planeType, plane_insignia, 'Available', 'N/A', 'N/A', 'N/A'])
        return __final_list