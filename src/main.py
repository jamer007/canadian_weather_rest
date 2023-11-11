import asyncio
import json
import os

from flask import Flask

from ec_weather import ECWeather

app = Flask(__name__)


@app.route('/<coord>')
def get_weather(coord=None):
    if coord:
        coord = coord.split(',')

        if len(coord) < 2:
            print('Coordinate must be geodesic format, ex: 45.512333,-73.587011')
            return {}
        return get_cw_current_weather(float(coord[0]), float(coord[1]))
    else:
        print('Please provide coordinate')
        return {}


# @app.route('/accuweather/<coord>')
# def get_accuweather_current(coord=None):
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     sample_good_input_data_file_path = "accuweather_sample.json"
#     with open(os.path.join(dir_path, sample_good_input_data_file_path)) as file:
#         json_data = json.load(file)
#
#         print(json_data)
#
#     return json_data


def get_cw_current_weather(lat: float, lon: float) -> dict:
    ec_en = ECWeather(coordinates=(lat, lon))
    asyncio.run(ec_en.update())
    current = ec_en.conditions

    if current.get('temperature', {}).get('value') is not None:
        temp_f = (1.8 * current.get('temperature').get('value')) + 32
        return {'temp_c': current.get('temperature').get('value'), 'temp_f': temp_f}


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0', port=5001)
