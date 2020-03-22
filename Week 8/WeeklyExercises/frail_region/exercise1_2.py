from flask import Flask, jsonify, abort, request
from sqlalchemy import create_engine
import pandas as pd
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
        #result_salaries = cursor_salary.fetchall()
        for (firstname, lastname) in cursor_salary:
            result_salaries.append({firstname, lastname})

        # query lastname
    with connection.cursor() as cursor_lastname:
        cursor_lastname.execute(query_lastname)
        #result_name = cursor_lastname.fetchall()
        for (firstname, lastname) in cursor_lastname:
            result_name.append({firstname, lastname})

    connection.close()
    return result_salaries, result_name


# salaries, names = exercise1()
# print('Persons with salaries above 50k:', salaries)
# print('Persons with the lastname \'Juhlborg\':', names)


def exercise2():
    """
    "Anvend filen: befkbhalderstatkode.csv
    Lav denne fil om til en mysql table med navnet statskode"
    """
    # read csv to dataframe
    df = pd.read_csv('./befkbhalderstatkode.csv')
    # set up database connection (pandas prefer sqlalchemy)
    con_str = 'mysql+pymysql://dev:ax2@localhost:3307/'
    engine = create_engine(con_str)
    engine.execute('DROP DATABASE IF EXISTS Week8_FrailRegion;')
    engine.execute('CREATE DATABASE Week8_FrailRegion;')
    engine.execute('USE Week8_FrailRegion;')
    # dataframe to sql
    df.to_sql('statskode', engine, if_exists='replace', index=False)


# exercise2()


