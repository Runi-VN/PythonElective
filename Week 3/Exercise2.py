import csv
import Exercise1 as ex1
import os
# Ex 2 Exceptions
# read students.csv for testing
students_data = ex1.read_students(os.getcwd()+'/output/students.csv')


# If list is shorter than 3 raise your own custom exception (NotEnoughStudentsException)
class NotEnoughStudentsException(ValueError):
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)


# Create a function that can take a list of students and return the 3 students closest to completing their study.
def get_top3_students_by_ects(students: list):
    if (len(students) < 3):
        raise NotEnoughStudentsException(
            'Not enough students found. Minimum = 3. Actual = {}'.format(len(students)))
    student_sorted_top3 = sorted(
        students, key=lambda student: student.get_progression(), reverse=True)[:3]  # will not throw exception
    return student_sorted_top3


# print(get_top3_students_by_ects([1, 2])) #throws exception
# print(get_top3_students_by_ects(students_data))


# Create another function that can create a csv file with 3 students closest to completion
# If an exception is raised write an appropriate message to the file
def write_top3_students(path: str, students: list):
    """
    Takes a list of students, gets the top 3, and
    writes student objects in a list to csv\n
    path should be location+name+extension, e.g. /output/students.csv
    """
    # get top 3 students from list
    try:
        top3_students = get_top3_students_by_ects(students)
        with open(path, 'w', newline='') as file_object:
            writer = csv.writer(file_object)
            writer.writerow(["stud_name", "stud_gender",
                             "stud_data_sheet", "stud_img_url"])
            for student in top3_students:  # use sorted student collection
                # name: str, gender: str, data_sheet: DataSheet, image_url: str
                writer.writerow([student._name, student._gender,
                                 student._data_sheet, student._image_url])
        print('Succesfully wrote students to file:' + path)
    except NotEnoughStudentsException as e:
        print(e)
        with open(path, 'w', newline='') as file_object:
            writer = csv.writer(file_object)
            writer.writerow(['ERROR'])
            writer.writerow([str(e)])
        print('Error message written to file')


# write_top3_students(os.getcwd()+'/output/students_top3.csv', [1, 2]) #triggers  exception
write_top3_students(os.getcwd()+'/output/students_top3.csv', students_data)
