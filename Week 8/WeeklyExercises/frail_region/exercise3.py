from flask import Flask
import pandas as pd
from sqlalchemy import create_engine

"""
Lav en restfull webservice (flask) som kan vise dataen fra befkbhalderstatkode.csv 
"""
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_stats():
    """
    Instead of the .csv, I am going to serve the database contents to the endpoint. Other solution:
    df = pd.read_csv("./befkbhalderstatkode.csv")
    return df.to_html()
    ----
    It is quite slow (~30 seconds)...Understandably, as we got a SQL table -> dataframe -> HTML table with 542.517 rows!

    """
    con_str = 'mysql+pymysql://dev:ax2@localhost:3307/Week8_FrailRegion'
    engine = create_engine(con_str)
    df = pd.read_sql_table('statskode', con=engine)
    return df.to_html()


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
