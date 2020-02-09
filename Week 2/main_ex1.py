# Used for testing exercises
import Exercise1 as ex1

ex1.print_file_content(
    'ClassExercises\\Downloads\\befkbhalderstatkode.csv')  # ex1.A
# Prints ['AAR', 'BYDEL', 'ALDER', 'STATKODE', 'PERSONER'] followed by data

ex1.write_list_to_file('test_writeListToFile.txt',
                       'Line one', 'Line two', 'Line three')  # ex1.B
# Writes the following:
# Line one
# Line two
# Line three
# (See output file in repository)

print(ex1.read_csv('ClassExercises\\Downloads\\befkbhalderstatkode.csv'))  # ex1.C
# List of header and rows.

# ex1.2 results can be seen in Exercise1.py
