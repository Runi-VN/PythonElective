#!flask/bin/python
import re
from flask import Flask, jsonify, abort, request
import exercise1_2 as facade

"""
"Lav en flask server, hvor du åbner minimum 2 endpoints:
- GET : returner data omkring antallet af crimes i en given periode
(giv to datoer med som query-param i URL'en)
- POST : returner den totale mængde af ""burglaries"" i januar, men returner kun data,
hvis request.body indeholder et json objekt med key-value {""key"":""secret""}"
"""


app = Flask(__name__)


@app.route('/api/crimes/', methods=['GET'])
def get_crime_daterange():
    try:
        startday = request.args.get('start')  # no need to parse int apparently
        endday = request.args.get('end')
        # could have probably just checked value between 1 and 31..
        check_day = re.compile('(0[1-9]|[12]\d|3[01])')
        if (check_day.match(startday) and check_day.match(endday)):
            result = facade.exercise2(startday, endday)['date_crimes']
            return jsonify({f'Amount of crimes between 2006-01-{startday} & 2006-01-{endday}': result})
        return jsonify({"message": "Error: Wrong parameters (01-31 only)"}), 400
    except:
        return jsonify({"message": "Something went wrong. Parameters are start & end."}), 404


@app.route('/api/crimes/', methods=['POST'])
def get_burglaries():
    if (request.json['key'] == 'secret'):
        result = facade.exercise2()['burglaries']
        return jsonify({'Total amount of burglaries': result}), 201
    return jsonify({'message': 'Something went wrong'}), 404


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
