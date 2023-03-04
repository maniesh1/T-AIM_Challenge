import csv
import datetime
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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
            heatwaves_value = int(data[day_of_year-1][city])
        except KeyError:
            return {"error": "Invalid city specified"}, 400

        # Return heat waves value as JSON response
        return {"heat waves": heatwaves_value}, 200

api.add_resource(heat_waves, '/api/heat_waves/<string:city>/<string:date>')

if __name__ == '__main__':
    app.run(debug=True)