from flask import render_template, jsonify
from app import app
from app.models import DbStaticInfo, DbDynamicInfo
import helpers
import requests

import time
import json
from sqlalchemy.sql.expression import func,select
from sqlalchemy import and_,desc,asc
from alembic.command import current
from jedi.evaluate import dynamic
from flask.globals import request
from tkinter.constants import LAST
from mysqlx.protobuf.mysqlx_crud_pb2 import Limit
from _operator import add
from scipy.constants.constants import dyn


"""
Create the different routes here
"""

@app.route("/")
@app.route("/index", methods=['POST'])
def index():
    try:
        #Static info results in a list of rows ordered by number
        static_table = DbStaticInfo.query.all()
        static_info = helpers.get_static_data(static_table)
        #Dynamic row results in a list of rows ordered by desc id. This is not in the same order as above
        dynamic_rows = DbDynamicInfo.query.order_by(desc(DbDynamicInfo.id)).limit(113).all()    
        lat, lng, address,available_bikes, bikestands,number = ([] for i in range(6))
        bikes = {}
        bikestands = static_info['bikestands']
        lat = static_info['lat']
        lng = static_info['lng']
        address = static_info['address']
        number = static_info['number']
        #Iterating through the list of dynamic bike data and adding it to a dictonary using its number as a key and bike availability as a value
        for i in range(len(dynamic_rows)):
            bikes[dynamic_rows[i].number] = dynamic_rows[i].available_bikes
        #Sorting the bike list to be ordered by number
        sorted_bikes = sorted(bikes.items())
        #Appending the value of each key to a list with a list comprehension 
        available_bikes = [i[1] for i in sorted_bikes]
        return render_template("index.html",
                                len = len(lat),
                                lat = lat,
                                lng = lng,
                                address = address,
                                bikestands = bikestands,
                                number = number,
                                available_bikes = available_bikes)
    except:
        return "Error: unable to fetch data."


@app.route("/get_bike_info", methods=["POST"])
def get_bike_info():
    try:
        result = helpers.get_date_time()
        date_time = int(result[0].strftime('%s')
        print(date_time)
        weekday = result[1]
        
        static_row = DbStaticInfo.query.all()
        static_info = helpers.get_static_data(static_row)
        numbers = static_info['number']
        address = static_info['address']
        #Model prediction comes in
        #bikes = 
        
            
        #The max value selected is the largest value less than the date time entered by the user
        
        max_values = select([func.max(DbDynamicInfo.last_update)]).where(DbDynamicInfo.last_update <= date_time)
        ordered = DbDynamicInfo.query.filter(DbDynamicInfo.last_update >= max_values).order_by(DbDynamicInfo.last_update).limit(113).all()
        dynamic_bikes = helpers.get_dynamic_data(DbStaticInfo.query.all(),ordered)
        results = json.dumps({'bikes':dynamic_bikes['available_bikes'],'address':dynamic_bikes['address']})
        return results
    except:
        return "Error: unable to fetch dynamic data."
    
    
@app.route("/infoWindow", methods=['POST'])
def infoWindow():
    try:
        lat_lng = helpers.get_lat_lng()
        #Returns a tuple containing lat and lng as two 6 decimal floats
        lat = lat_lng[0]
        lng = lat_lng[1]
        #FInding the specific row in DbStaticInfo relating to the lat and lng provided
        static_row = DbStaticInfo.query.filter(DbStaticInfo.lat == lat).filter(DbStaticInfo.lng == lng).all()
        static_info = helpers.get_static_data(static_row)
        #Ordering the Dynamic Info database to get the last 113 rows (all the stations at the most recent time)
        limited_rows = DbDynamicInfo.query.filter(DbDynamicInfo.number == static_info['number'][0]).order_by(desc(DbDynamicInfo.id)).limit(2016).all()
        station_history = []
        address = static_info['address']
        bikestands = static_info['bikestands']
        available_bikes = limited_rows[0].available_bikes
        #Selecting all available bikes and times for past week.
        station_history = list(map(lambda x: x.available_bikes,limited_rows))
        #Times are returned as hrs and minutes.
        time = list(map(lambda x: x.last_update.strftime("%H:%M"),limited_rows))
        results = json.dumps({"address":address,"bikestands":bikestands,"available_bikes":available_bikes,"station_history":station_history,"time":time})
        return results
        
    except:
        return "Error: unable to fetch data."