import pandas as pd
#import pymysql
from sqlalchemy import create_engine

con_str = 'mysql+pymysql://dev:ax2@localhost:3307/'


def exercise1():
    """
    Download data fra linket og gem det i en dataframe 
    og gem det i en mysql database
    """
    # I have saved the file locally
    df = pd.read_csv('./SacramentocrimeJanuary2006.csv')
    engine = create_engine(con_str)
    engine.execute('DROP DATABASE IF EXISTS Week8;')
    engine.execute('CREATE DATABASE Week8;')
    engine.execute('USE Week8;')
    df.to_sql('crimestats', con=engine, if_exists='replace', index=False)
    print('If no error, we succeeded lol')


# exercise1()


def exercise2(start_day=None, end_day=None):
    """
    Lav en funktion der returnerer en dict med minimum følgende data:
    - Find antallet af crimes mellem to givne datoer i 2006 (givet som parameter til funktionen)
    - Find den totale mængde af ""burglary"" i januar
    """
    engine = create_engine(con_str + 'Week8')
    df = pd.read_sql_table('crimestats', con=engine, parse_dates=[
                           'cdatetime'], columns=['cdatetime', 'crimedescr'])
    if (start_day and end_day):
        start_date = '2006-01-'+start_day
        end_date = '2006-01-'+end_day
        date_specific_crimes = df.loc[(df['cdatetime'] >= start_date)
                                      & (df['cdatetime'] <= end_date)]
        return {'date_crimes': len(date_specific_crimes)}

    amount_of_burglaries = df[df['crimedescr'].str.contains('BURGLARY')]
    return {'burglaries': len(amount_of_burglaries)}


#print(exercise2('01', '02'))
# print(exercise2())
