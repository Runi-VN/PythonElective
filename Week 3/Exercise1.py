# Ex 1 Classes
# Create 3 classes: Student, DataSheet and Course
# A student has a data_sheet and a data_sheet has multiple courses in particular order
# Each course has name, classroom, teacher, ETCS and optional grade if course is taken.
# In Student create init() so that a Student can be initiated with name, gender, data_sheet and image_url
# In DataSheet create a method to get_grades_as_list()
# In student create a method: get_avg_grade()


import matplotlib.pyplot as plt
import os
import csv
import random
import secrets


class Course():
    def __init__(self, name: str, classroom: str, teacher: str, ects: int, grade: int = None):
        self._name = name
        self._classroom = classroom
        self._teacher = teacher
        self._ects = ects
        self._grade = grade

    def __str__(self):
        # return f'[Course]name={self._name},classroom={self._classroom},teacher={self._teacher},ects={self._ects},grade={self._grade}[Course End]'
        # csv
        return f'{self._name},{self._classroom},{self._teacher},{self._ects},{self._grade}'

    def __repr__(self):
        # return 'Course(%r, %r, %r, %r, %r)' % (self._name, self._classroom, self._teacher, self._ects, self._grade)
        # csv
        return "%r, %r, %r, %r, %r" % (self._name, self._classroom, self._teacher, self._ects, self._grade)

    def get_grade(self):  # to be used for other methods
        return self._grade

    def get_ects(self):  # to be used for other methods
        return self._ects


class DataSheet():
    def __init__(self, *courses: Course):
        self._courses = list(courses)
        self._current = -1  # not read yet
        self._high = len(self._courses)

    def __str__(self):
        # return super(DataSheet, self).__str__() + f'[DataSheet]courses={self._courses}[DataSheet End]'
        # csv
        return super(DataSheet, self).__str__() + (str(self._courses))

    def __repr__(self):
        # return 'DataSheet(%r)' % (self._courses)
        return "%r" % (self._courses)  # csv

    def get_courses(self):  # to be used for other methods
        return self._courses

    def get_grades_as_list(self):
        grades_list = []
        for course in self.get_courses():
            grades_list.append(course.get_grade())
        return grades_list

    def add_course(self, course: Course):
        self._courses.append(course)

    # Extra: Make the Datasheet class iterable so that next(data_sheet) will return the next course in the list
    def __iter__(self):
        return iter(self._courses)

    def __next__(self):  # Python 2: def next(self)
        self._current += 1
        if self._current < self._high:
            courses = self.get_courses()
            return courses[self._current]
        raise StopIteration


class Student():
    def __init__(self, name: str, gender: str, data_sheet: DataSheet, image_url: str):
        self._name = name
        self._gender = gender
        self._data_sheet = data_sheet
        self._image_url = image_url

    def __str__(self):
        # return f'[Student]name={self._name},gender={self._gender},datasheet={str(self._data_sheet)},image_url={self._image_url}[Student End]'
        # csv
        return f'{self._name},{self._gender},{str(self._data_sheet)},{self._image_url}'

    def __repr__(self):
        # csv
        return "%r, %r, %r, %r" % (self._name, self._gender, self._data_sheet, self._image_url)

    def get_avg_grade(self):
        grades = self._data_sheet.get_grades_as_list()
        return sum(grades) / len(grades)

    def get_datasheet_courses(self):
        return self._data_sheet.get_courses()

    def get_progression(self):
        ects_total = 0
        for course in self._data_sheet.get_courses():
            if (course.get_grade()) >= 2:  # passed, ECTS granted
                ects_total += course.get_ects()
        return (ects_total/150)*100


# Create a function that can generate n number of students with random: name, gender, courses (from a fixed list of course names), grades, img_url
# student attributes
student_names = ['John', 'Anne Merethe', 'Lars',
                 'Pernille', 'Bo', 'Absalon', 'Runi', 'Lotte']

genders = ['Male', 'Female']

img_urls = ['https://www.example.com/', 'https://www.url1.com/',
            'https://www.nonexistant.dk/', 'http://www.unsafe.dev/']
# course attributes
course_names = ['Datamatiker', 'Testing', 'Frontend',
                'Backend', 'Havbiolog', 'Skorstensfejer']
course_classrooms = [101, 102, 203, 204, 305, 360]

course_teachers = ['Hr. Jørgensen', 'Fru. Karlsen', 'Frk. Knudsen']

course_ects = [0, 5, 7.5, 10, 15, 20]

course_grades = [-3, 00, 2, 4, 7, 10, 12]


def generate_students(amount_of_students: int):
    """Pass a number of students and a list will be returned.
    The list will contain random students, with all fields, including
    random DataSheets with  random Courses"""
    students = []
    courses = []
    # create courses: name, classroom, teacher, ects, grade=None
    # could also have used random.sample(list,key)
    amt_of_courses = secrets.SystemRandom().randint(1, 10)
    for i in range(0, amt_of_courses):
        c_name = secrets.choice(course_names)
        c_classroom = secrets.choice(course_classrooms)
        c_teacher = secrets.choice(course_teachers)
        c_ects = secrets.choice(course_ects)
        c_grade = secrets.choice(course_grades)
        rnd_course = Course(c_name, c_classroom, c_teacher, c_ects, c_grade)
        courses.append(rnd_course)
    for student in range(0, amount_of_students):
        amt_of_courses_to_enroll = secrets.SystemRandom().randint(1, len(courses))
        # create datasheet: *courses
        # random.sample() returns a list, so use * to convert into required *args
        s_sheet = DataSheet(
            *random.sample(courses, amt_of_courses_to_enroll))
        # create student: name, gender, data_sheet, image_url
        s_name = secrets.choice(student_names)
        s_gender = secrets.choice(genders)
        s_img = secrets.choice(img_urls)
        rnd_student = Student(s_name, s_gender, s_sheet, s_img)
        students.append(rnd_student)
    return students
# test
# print(generate_students(3))

# Let the function write the result to a csv file with format stud_name, course_name, teacher, ects, classroom, grade, img_url
# I will create a new function instead


def write_students(path: str, students: list):
    """
    Writes student objects in a list to csv
    path should be location+name+extension, e.g. /output/students.csv
    """
    with open(path, 'w', newline='') as file_object:
        writer = csv.writer(file_object)
        writer.writerow(["stud_name", "course_name", "teacher",
                         "ects", "classroom", "grades", "img_url"])
        for student in students:
            # specific order, so lets grab it in the required format
            #stud_name = student._name
            # stud_course_names = []  # "course_name"
            #stud_course_teachers = []
            #stud_course_classroom = []
            #stud_course_grades = []
            for course in student._data_sheet.get_courses():
                # stud_course_names.append(course._name)
                # stud_course_teachers.append(course._teacher)
                # stud_course_classroom.append(course._classroom)
                # stud_course_grades.append(course._grade)
                writer.writerow([student._name, course._name, course._teacher,
                                 course._ects, course._classroom, course._grade, student._image_url])
    print('Succesfully wrote students to file:' + path)


#write_students(os.getcwd()+'/output/students.csv', generate_students(10))


# 8) Read student data into a list of Students from a csv file:
def read_students(filename: str):
    students = []
    with open(filename) as file_object:
        reader = csv.reader(file_object)
        header = next(reader)  # discarded
        for row in reader:
            student_check = False  # Check if we have written data yet in this loop
            current_course = Course(
                row[1], row[4], row[2], int(row[3]), int(row[5]))
            for student in students:
                if row[0] == student._name:  # student already exists, uuid = name xd
                    # add course data to student
                    student._data_sheet.add_course(current_course)
                    student_check = True
                    # could add all other values
            # Ran through all students, does not exist.
            if not student_check:
                # create datasheet to hold courses
                sheet = DataSheet(current_course)
                # create student
                # Gender is not passed to document
                current_student = Student(row[0], "Unknown", sheet, row[6])
                students.append(current_student)
    return students


students_result = read_students(os.getcwd()+'/output/students.csv')

# 8.a) loop through the list and print each student with name, img_url and avg_grade.
# for student in students_result:
#     print(
#         f'Student name:{student._name}\n Student image:{student._image_url} \n Student average grade:{student.get_avg_grade()} \n')

# 8.b) sort the list by avg_grade


def sort_students_by_grade(students: list, order_descending: bool = True):
    """
    Sorts a list of students by their average grade. \n
    By default the list will be sorted descending.
    """
    students_sorted = sorted(
        students, key=lambda student: student.get_avg_grade(), reverse=order_descending)
    return students_sorted


# sorted_students_result = sort_students_by_grade(students_result)  # , False
# for student in sorted_students_result:
#     print(f'SORTED- Name: {student._name} \t Grade: {student.get_avg_grade()}')


# 8.c) create a bar chart with student_name on x and avg_grade on y-axis
def student_average_barchart(students: list):
    """
    Creates and displays a bar chart of students names and their average grade.
    """
    names_and_grades = {student._name: student.get_avg_grade()
                        for student in students}  # dictionary comprehension  name:grade
    plt.figure()

    # set up labels
    plt.title('Students & average grade sorted')
    plt.xlabel('Student name')
    plt.ylabel('Student avg. grade')

    # set up chart
    plt.bar(names_and_grades.keys(), names_and_grades.values(),
            width=0.2, color=['g', 'g', 'g', 'r', 'r'])  # only works for current loaded data, where results are 12,7,6,1,-3 (last two are below treshhold of 2)
    plt.ylim(-3, 12)  # grade scales on the y-axis (min/max)
    # plt.show() #enable to show


# student_average_barchart(sorted_students_result)

# 9) Make a method on Student class that can show progression of the study in %
# (add up ECTS from all passed courses divided by total of 150 total points (equivalent to 5 semesters))
# for student in sorted_students_result:
#     print(
#         f'Completion by ECTS- Name: {student._name} \t Course completion in %: {student.get_progression()}')

# 10) Show a bar chart of distribution of
# study progression on x-axis and number of students in each category on y-axis.
# (e.g. make 10 categories from 0-100%)


def student_progression_barchart(students: list):
    #student_progression = {f'{value}' for value in range(0, 100, 10)}
    student_progress = {}
    for student in students:
        student_progress[student._name] = student.get_progression()
    # sort by progress
    #sorted_progress = {k: v for k, v in sorted(student_progress.items(), key=lambda item: item[1], reverse=True)}
    # print(student_progress)
    # print(sorted_progress)
    plt.figure()
    # set up labels
    plt.title('Students/Progression')
    plt.xlabel('Student Name')
    plt.ylabel('Current Progression')
    # set up chart
    plt.ylim(0, 100)
    plt.plot(list(student_progress.keys()), list(student_progress.values()))
    # plt.show() #enable to show
    # I didn't do this properly. Weird assignment imo. A lot of hardcoded stuff or what?


# student_progression_barchart(sorted_students_result)

# Extra: Make the Datasheet class iterable so that next(data_sheet) will return the next course in the list
# student_of_interest = sorted_students_result[0]
# print('Testing next(datasheet) of student. Full datasheet:')
# print(student_of_interest._data_sheet)
# print('next')
# print(next(student_of_interest._data_sheet))
# print('next')
# print(next(student_of_interest._data_sheet))
# print('next')
# print(next(student_of_interest._data_sheet))
# print('next')
# print(next(student_of_interest._data_sheet)) # throws exception
