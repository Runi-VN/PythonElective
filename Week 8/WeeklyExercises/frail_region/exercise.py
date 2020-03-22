import pymysql

from collections import OrderedDict


def exercise1():
    """
    "Brug test.sql scriptet (pythondemo):
    Hent følgende data:
    Navn på de personer som har en salary der er højere end 50.000
    Navn på dem som har efternavnet Juhlborg"
    -----
    returns two lists, first is salaries, second is based on the name 'Juhlborg'
    """
    query_salary = """SELECT firstname, lastname FROM test.pythondemo WHERE salary > 50000;"""
    query_lastname = """SELECT firstname, lastname FROM test.pythondemo WHERE lastname = 'Juhlborg';"""

    connection = pymysql.connect(user='dev', password='ax2',
                                 host='127.0.0.1', port=3307, db='test')  # vagrant
    result_salaries = []
    result_name = []
    # query salary
    with connection.cursor() as cursor_salary:
        cursor_salary.execute(query_salary)
        for (firstname, lastname) in cursor_salary:
            result_salaries.append({firstname, lastname})
    # query lastname
    with connection.cursor() as cursor_lastname:
        cursor_lastname.execute(query_lastname)
        for (firstname, lastname) in cursor_lastname:
            result_name.append({firstname, lastname})

    connection.close()
    return result_salaries, result_name


salaries, names = exercise1()
print('Persons with salaries above 50k:', salaries)
print('Persons with the lastname \'Juhlborg\':', names)
