import math
import Exercise1 as ex1
import matplotlib.pyplot as plt
import secrets
import os

# Ex 3 Plotting
students_data = ex1.read_students(os.getcwd()+'/output/students.csv')


genders = ['Male', 'Female']


def assignGenders(students: list):
    """
    re-assign genders as they were never written and therefore unable to be read.
    """
    for student in students:
        student._gender = secrets.choice(genders)
    return students


# Create a function that can take a list of students
# and show a pie chart of how students are distributed in ECTS percentage categories (10%, 20%, ...)


def create_studentECTS_piechart(students: list):
    data = {}
    for student in students:
        data[student._name] = student.get_progression()
    # k,v | name, progression
    print('data', data)

    percentage = {}
    for progress in data.values():
        # get 10th percent rounded up. e.g. (43.3/10) = 4.3 (round up (int) = 5) => (5 * 10) = 50%
        result = int(math.ceil(progress / 10.0)) * 10
        percentage[result] = percentage.get(result, 0) + 1
        # default value = 0 if_not_exist else increment by 1
    # k, v | percentage, count of occurences
    print(percentage)
    fig1, ax1 = plt.subplots()
    ax1.pie(percentage.values(), labels=percentage.items(), autopct='%1.1f%%')
    ax1.set_aspect('equal')
    plt.show()


# create_studentECTS_piechart(students_data)


# create a function that can take a list of students and show how many students have taken each course (bar chart)
# create a method on student that can return a list of courses
def create_student_course_barchart(students: list):
    course_data = {}
    for student in students:
        for course in student.get_datasheet_courses():
            course_data[course._name] = course_data.get(course._name, 0) + 1
            # default value = 0 if_not_exist, increment by 1
    # plt.figure()
    plt.xlabel('Course')
    plt.ylabel('No. of students')
    plt.title('Ex3.2 - Courses & count')
    plt.bar(course_data.keys(), course_data.values(), 0.5)
    plt.show()


# create_student_course_barchart(students_data)


# make the figure show males and females in different colors for each course (display 2 datasets in same figure)
# Out of scope imo. There is no longer gender tied to the students as they were written to file without.
def create_student_course_barchart_genderfied(students: list):
    students = assignGenders(students)

    female_courses = {}
    male_courses = {}
    for student in students:
        print(student._gender + '\t', student.get_datasheet_courses())
        for course in student.get_datasheet_courses():
            if (student._gender == 'Male'):
                male_courses[course._name] = male_courses.get(
                    course._name, 0) + 1
            else:
                female_courses[course._name] = female_courses.get(
                    course._name, 0) + 1
    print(female_courses, '\n')
    print(male_courses)

    import numpy as np
    all_courses = set({**female_courses, **male_courses}.keys())
    ypos = np.arange(len(all_courses))
    plt.xlabel('Course')
    plt.ylabel('No. of students')
    plt.title('Ex3.2 - Courses & count')
    plt.xticks(ypos, all_courses)
    plt.bar(ypos-0.2, male_courses.values(), width=0.4)
    plt.bar(ypos+0.2, female_courses.values(), width=0.4)
    plt.show()


# create_student_course_barchart_genderfied(students_data)
