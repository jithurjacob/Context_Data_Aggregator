from flask import Flask, render_template, jsonify, request
# from flask_cors import CORS, cross_origin
import holidayapi, time
from datetime import datetime
import requests
hapi = holidayapi.v1('5605610e-feb0-490b-b32b-b32184c13c89')
app = Flask(__name__)


@app.route('/getWeatherData', methods=['POST'])
def getWeatherData():
    latitude, longitude, cityName = request.form.get("latitude",None), request.form.get("longitude",None), request.form.get("cityName",None)
    return "none"

@app.route('/getHolidayData', methods=['POST'])
def getHolidayData():
    countryCode = request.form.get("countryCode",None)
    parameters = {
        # Required
        'country': countryCode,
        'year':    2016,
        # Optional
        # 'month':    7,
        # 'day':      4,
        # 'previous': True,
        # 'upcoming': True,
        # 'public':   True,
        # 'pretty':   True,
    }
    holidays = hapi.holidays(parameters)["holidays"]
    # holidays = [[holiday,(datetime.strptime(holiday.replace("2016","2017"), "%Y-%M-%d").date()) , datetime.today().date(),(datetime.strptime(holiday.replace("2016","2017"), "%Y-%m-%d").date()) >= datetime.today().date()] for holiday,value in holidays.items() if (datetime.strptime(holiday.replace("2016","2017"), "%Y-%M-%d").date()) < datetime.today().date()]
    # for holiday_date, val in holidays.items():
    #     print(holiday_date,val)
    #     t1 = datetime.strptime(holiday_date.replace("2016","2017"), "%Y-%m-%d").date()
    #     t2 = datetime.today().date()
    #     print(t1, t2, t1 >= t2)
    #     if
    holidays = [{holiday.replace("2016","2017"):value[0]["name"]} for holiday,value in holidays.items() if (datetime.strptime(holiday.replace("2016","2017"), "%Y-%m-%d").date()) >= datetime.today().date()]
        
    return jsonify(holidays =holidays)

@app.route('/proxy')
def proxy():
    url = request.args.get("url").replace("$","&")
    print(url)
    return jsonify(requests.get(url).json())

@app.route('/')
def index():
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
