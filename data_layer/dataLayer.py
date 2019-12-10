import os

class DataAPI:

    def __init__(self, name_of_file):
        self.name_of_file = name_of_file


    def write_file(self, info):
        '''writes into an existing file , if the file does not exist the program creates it.'''
        __file_path = os.path.realpath(f'../csv_data/{self.name_of_file}')
        with open(__file_path, 'w') as __csv_data:
            for line in info:
                __csv_data.write(','.join(line) + '\n')


    def read_file(self):
        '''in start of application the logic worker tries to read a certan file.
        if the file does not extis None get sent up to the logic worker
        the logic worker then calls the write methood and a new file will be created.
        first line in the file will be names of the columns'''
        __file_path = os.path.realpath(f'../csv_data/{self.name_of_file}')
        try:
            with open(__file_path, 'r') as __csv_data:
                self.__data_list = [line.strip().split(",") for line in __csv_data]
                return self.__data_list

        except FileNotFoundError:
            return None