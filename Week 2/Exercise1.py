
# 1) Create a python file with 3 functions:
#   A) def print_file_content(file) that can print content of a csv file to the console
#
#   B) def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
#       B2) rewrite the function so that it gets an arbitrary number of strings instead of a list
#
#   C) def read_csv(input_file) that take a csv file and read each row into a list

import csv
import argparse
import os


def print_file_content(file):  # A
    with open(file) as file_object:
        reader = csv.reader(file_object)
        for row in reader:
            print(str(row))


def write_list_to_file(output_file, *strings):  # B + B2
    with open(output_file, 'w') as file_object:
        for string in strings:
            file_object.write(string + '\n')


def read_csv(input_file):  # C
    list_of_rows = []
    with open(input_file) as file_object:
        reader = csv.reader(file_object)
        for row in reader:
            list_of_rows.append(row)
    return list_of_rows


# 2) Add a functionality so that the file can be called from cli with 2 arguments
    # A) path to csv file
    # B) an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.
# 3) Add a --help cli argument to describe how the module is used
parser = argparse.ArgumentParser(
    description='Program that reads a CSV file and returns a python list of all rows. See commands path and --file_name')

parser.add_argument('path', help='path to the CSV file to be read')

parser.add_argument('-f', '--file_name',
                    help='File to write to. If not given, output will be printed to console',)

if __name__ == '__main__':
    def read_csv_extended(input_file, output_file):  # C
        list_of_rows = []
        with open(input_file) as file_object:
            reader = csv.reader(file_object)
            for row in reader:
                list_of_rows.append(row)
        if (output_file):
            print(f'Writing to requested file: {output_file}')
            with open(output_file, 'w') as output_object:
                string_to_write = ""
                for element in list_of_rows:
                    for string in element:
                        # not required but just to easier read the .txt file
                        string_to_write += string+'\n'
                # str([[string + '\n' for string in items] for items in list_of_rows]) tried with list comprehension...
                output_object.write(string_to_write)
        else:
            print('No output file found. Printing to console...')
            print(list_of_rows)

    args = parser.parse_args()
    input_file = args.path
    output_file = args.file_name  # either output or False

    read_csv_extended(input_file, output_file)
    # python Exercise1.py "classExercises\Downloads\befkbhalderstatkode.csv"
    # returns a console print of the file.
    # python Exercise1.py "ClassExercises\Downloads\befkbhalderstatkode.csv" -f "read_csv_extended_result.txt"
    # returns the output file in the repository.
