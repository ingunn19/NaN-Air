#data layer

class Data:
    def __init__(self, name_of_file):
        self.name_of_file = name_of_file


    def write_file(self, info):
        '''writes into an existing file , if the file does not exist the program creates it.'''
        with open(f'csv_{self.name_of_file}_data.csv', 'a') as __csv_data:
            for line in info:
                __csv_data.write(line + '\n')


    def read_file(self):
        '''in start of application the logic worker tries to read a certan file.
        if the file does not extis None get sent up to the logic worker
        the logic worker then calls the write methood and a new file will be created.
        first line in the file will be names of the columns'''

        try:
            with open(f'csv_{self.name_of_file}_data.csv', 'r') as __csv_data:
                return __csv_data
        except FileNotFoundError:
            return None









