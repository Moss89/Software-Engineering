from flask import render_template
from app import app
from app.models import DbStaticInfo, DbDynamicInfo
import helpers
import pickle
import json
from sqlalchemy import desc

# IDE sometimes says app stuff doesn't exist but worksS

# Opens model
with open("./app/static/data_model.pkl", "rb") as handle:
    model = pickle.load(handle)

"""
Create the different routes here
"""


@app.route("/")
@app.route("/index", methods=['POST'])
def index():
    # Static info results in a list of rows ordered by number
    static_table = DbStaticInfo.query.all()
    static_info = helpers.get_static_data(static_table)
    # Dynamic row results in a list of rows ordered by desc id. This is not in the same order as above
    dynamic_rows = DbDynamicInfo.query.order_by(desc(DbDynamicInfo.id)).limit(113).all()
    # lat, lng, address,available_bikes, bikestands,number = ([] for i in range(6))
    bikes = {}
    bikestands = static_info['bikestands']
    lat = static_info['lat']
    lng = static_info['lng']
    address = static_info['address']
    number = static_info['number']
    # Iterating through the list of dynamic bike data
    # Adding it to a dictonary
    # Using its number as a key and bike availability as a value
    for i in range(len(dynamic_rows)):
        bikes[dynamic_rows[i].number] = dynamic_rows[i].available_bikes
    # Sorting the bike list to be ordered by number
    sorted_bikes = sorted(bikes.items())
    # Appending the value of each key to a list with a list comprehension
    available_bikes = [i[1] for i in sorted_bikes]
    return render_template("index.html",
                           len=len(lat),
                           lat=lat,
                           lng=lng,
                           address=address,
                           bikestands=bikestands,
                           number=number,
                           available_bikes=available_bikes)

@app.errorhandler(500)
def internal_error(error):
    return "Sorry, there seems to be an error with our database, please try again later"

@app.errorhandler(404)
def not_found(error):
    return "Sorry, a resource couldn't be loaded"


@app.route("/get_bike_info", methods=["POST"])
def get_bike_info():
    # Get and format date and time
    date_time = helpers.get_date_time()
    date_time = helpers.formatDateTime(date_time)

    # Get address
    static_row = DbStaticInfo.query.all()
    static_info = helpers.get_static_data(static_row)
    address = static_info['address']

    # Get weather, format info for prediction
    weather = helpers.getWeather(date_time[0])
    info = helpers.formatWeatherInfo(weather, date_time[0], date_time[1])

    # Running model for all stations
    bikePredictions = []
    for i in sorted(model.keys()):
        # Note: info needs to be a list in a list because model takes array
        bikePredictions += [int(model[i].predict([info])[0])]

    results = json.dumps({"bikes": bikePredictions, "address": address})

    return results



@app.route("/infoWindow", methods=['POST'])
def infoWindow():
    lat_lng = helpers.get_lat_lng()
    # Returns a tuple containing lat and lng as two 6 decimal floats
    lat = lat_lng[0]
    lng = lat_lng[1]
    # FInding the specific row in DbStaticInfo relating to the lat and lng provided
    static_row = DbStaticInfo.query.filter(DbStaticInfo.lat == lat).filter(DbStaticInfo.lng == lng).all()
    static_info = helpers.get_static_data(static_row)
    # Ordering the Dynamic Info to get the past weeks occupancy
    limited_rows = DbDynamicInfo.query.filter(DbDynamicInfo.number == static_info['number'][0]).order_by(desc(DbDynamicInfo.id)).limit(2016).all()
    address = static_info['address']
    bikestands = static_info['bikestands']
    available_bikes = limited_rows[0].available_bikes
    # Selecting all available bikes and times for past week.
    station_history = list(map(lambda x: x.available_bikes, limited_rows))
    # Times are returned as hrs and minutes.

    time = list(map(lambda x: x.last_update.strftime("%H:%M"), limited_rows))
    results = json.dumps({"address": address, "bikestands": bikestands, "available_bikes":available_bikes, "station_history": station_history, "time": time})
    return results



@app.route("/prediction_day", methods=["POST"])
def prediction_day():
    # Getting a days result from a bike station
    # Get date and time
    result = helpers.get_date_time()
    # aDDING 2 to make python .weekday method match with mysql's weekdays
    # Monday in mysql is 2 and 0 in python
    weekday = (result[1] + 1) % 7 + 1
    lat_lng = helpers.get_lat_lng()
    # Returns a tuple containing lat and lng as two 6 decimal floats
    lat = lat_lng[0]
    lng = lat_lng[1]
    # FInding the specific row in DbStaticInfo relating to the lat and lng provided
    static_row = DbStaticInfo.query.filter(DbStaticInfo.lat == lat).filter(DbStaticInfo.lng == lng).all()
    static_info = helpers.get_static_data(static_row)
    address = static_info['address']
    # Getting the previous weeks result
    limited_rows = DbDynamicInfo.query.filter(DbDynamicInfo.number == static_info['number'][0]).filter(DbDynamicInfo.weekday == weekday).order_by(desc(DbDynamicInfo.id)).limit(288).all()
    day_results = list(map(lambda x: x.available_bikes, limited_rows))
    time = list(map(lambda x: x.last_update.strftime("%H:%M"), limited_rows))
    results = json.dumps({"address": address, "day_results": day_results, "time": time, 'day': weekday})
    return results