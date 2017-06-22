from flask import Flask, render_template
# from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/getWeatherData', methods=['POST'])
def getWeatherData():
    latitude, longitude, cityName = request.form.get("latitude",None), request.form.get("longitude",None), request.form.get("cityName",None)
    return "none"
@app.route('/')
def index():
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
