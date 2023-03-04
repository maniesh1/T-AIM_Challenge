import csv
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
import datetime



app = Flask(__name__)
api = Api(app)
CORS(app)
class AQI(Resource):
    def get(self, city, month):
        # Open CSV file and read data into a list of dictionaries
        with open("aqi_data.csv", "r") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]

        # Find the row for the specified month and the column index for the specified city
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        try:
            index = months.index(month)
        except ValueError:
            return jsonify({'error': 'Invalid month specified'})
        try:
            aqi_value = round(float(data[index][city]))
        except KeyError:
            return {"error": "Invalid city specified"}, 400

        # Return AQI value as JSON response
        return {"aqi": aqi_value}, 200

class AQIs(Resource): 
    def get(self):
        with open("aqi_data.csv", "r") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
            months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

            # Get the current date
            # /now = datetime.datetime.now()

            # Get the current month
            month = datetime.datetime.now().strftime("%B")

            index = months.index(month)
            aqi_values = data[index]

            return  aqi_values, 200
        
class heat_waves(Resource):
    def get(self, city, date):
        # Open CSV file and read data into a list of dictionaries
        with open("heatwaves_data.csv", "r") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]

        # Find the row for the specified date and the column index for the specified city
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')

        # Get the day of the year from the datetime object
        try:
            day_of_year = date_obj.timetuple().tm_yday
        except ValueError:
            return jsonify({'error': 'Invalid date specified'})
        try:
            heatwaves_value = int(data[day_of_year][city])
        except KeyError:
            return {"error": "Invalid city specified"}, 400

        # Return heat waves value as JSON response
        return {"heat waves": heatwaves_value}, 200

api.add_resource(heat_waves, '/api/heat_waves/<string:city>/<string:date>')

api.add_resource(AQI, '/api/aqi/<string:city>/<string:month>')
api.add_resource(AQIs, '/api/aqis')

if __name__ == '__main__':
    app.run(debug=True)