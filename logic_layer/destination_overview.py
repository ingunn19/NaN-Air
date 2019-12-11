from logic_parent import LogicParent

class DestinationOverviewLogic(LogicParent):
#overview destination
    def req_all_destinations(self):
        #getting all destination
        __all_destinaions = self.__destinations.read_file()
        if len(__all_destinaions) <=1:
            return None
        return __all_destinaions

    def req_one_destination(self, dest):
        #getting a list of all of the destinations
        __all_destinaions = self.__destinations.read_file()
        list_of_the_destinataion = []
        #getting the first row of the csv file (aka: header)
        list_of_the_destinataion.append(__all_destinaions[0])
        #for each line ew are gonna check if the first column in the row is equal to destination
        #if it is true we add the line to the list of destination
        for line in __all_destinaions:
            if line[0] == dest:
                list_of_the_destinataion.append(line)

        if len(list_of_the_destinataion) <= 1:
            return None
        return list_of_the_destinataion