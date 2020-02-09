# This is the exercises found at the bottom of the notebook. Had to name it like this to import.

# 1) Write a program that converts the Excel spreadsheet ./iris_data.xlsx into a CSV file with the same data.
# Start with writing a unit test against which you implement your solution.
import openpyxl
import csv
import platform
import os


def convert_xlsx_to_csv(filepath):
    """Converting given .xlsx file (with only one sheet lol) to .csv"""
    # filename.extension / './iris_data.xlsx'
    file_name_and_extension = os.path.basename(filepath)  # iris_data.xlsx
    filename = os.path.splitext(file_name_and_extension)[0]  # iris_data
    wb = openpyxl.load_workbook(file_name_and_extension)

    if platform.system() == 'Windows':
        newline = ''
    else:
        newline = None

    with open(('./' + filename + '.csv'), 'w', newline=newline) as output_file:  # iris_data.csv
        output_writer = csv.writer(output_file)
        sheet = wb.get_active_sheet()  # Only one sheet and it is per default the active
        for row in sheet:
            rowCells = []
            for cell in row:
                # print('cellValue:', cell.value)
                rowCells.append(cell.value)
            output_writer.writerow(rowCells)
    return(f'Succesfully wrote to {filename}.csv')


# 2) Write a program, which converts befkbhalderstatkode.csv
#  from a CSV file into a Python module kkdata.py containing a dictionary named STATISTICS.

# Convert .csv to a .py file containing results in a dictionary

def convert_csv_to_py(filepath):
    file_name_and_extension = os.path.basename(filepath)  # test.txt
    filename = os.path.splitext(file_name_and_extension)[0]  # test
    STATISTICS = {}

    with open(file_name_and_extension) as _file:
        reader = csv.reader(_file)
        header_row = next(reader)
        # STATISTICS = {}

        for idx, row in enumerate(reader, start=1):
            STATISTICS = {idx, dict(row}

        # for idx, row in enumerate(reader, start=1):
        #    if(reader.line_num > 5):
        #        break
        #    print(row, idx)
        #    if STATISTICS[row[0]]:
        #        print('ayoo')
        #        break
        #    else:

        #        for value in row:
        #            print("rowValue", value)
        # print('Row #' + str(reader.line_num) + ' ' + str(row))
        # if row[0] not in STATISTICS:
        # STATISTICS[row[0]]
        # else:
        # STATISTICS[row[0]][idx] = row[1:]
    print(STATISTICS)
