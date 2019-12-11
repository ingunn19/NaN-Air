import os

class DataAPI:
    def __init__(self, name_of_file):
        self.name_of_file = name_of_file

    def write_file(self, info):
        '''writes into an existing file , if the file does not exist the program creates it.'''
        with open(f'.//csv_data//{self.name_of_file}.csv', 'w') as __csv_data:
            for line in info:
                __csv_data.write(','.join(line) + '\n')

    def read_file(self):
        '''in start of application the logic worker tries to read a certan file.
        if the file does not extis None get sent up to the logic worker
        the logic worker then calls the write methood and a new file will be created.
        first line in the file will be names of the columns'''
        try:
            with open(f'..//csv_data//{self.name_of_file}.csv', 'r') as __csv_data:
                self.__data_list = [line.strip().split(",") for line in __csv_data]
                return self.__data_list

        except FileNotFoundError:
            return None