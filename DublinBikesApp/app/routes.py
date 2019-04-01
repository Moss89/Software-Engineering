from flask import render_template, jsonify
from app import app
from app.models import DbStaticInfo, DbDynamicInfo
import helpers
import requests
import datetime
import time
import json
from sqlalchemy.sql.expression import func
from sqlalchemy.sql import select
from sqlalchemy import and_
from _datetime import date
from alembic.command import current
from jedi.evaluate import dynamic
from flask.globals import request


"""
Create the different routes here
"""

@app.route("/")
@app.route("/index", methods=['POST'])
def index():
    try:
        static_table = DbStaticInfo.query.all()
        static_info = helpers.get_static_data(static_table)
        max_value = select([func.max(DbDynamicInfo.last_update)])
        dynamic_table = DbDynamicInfo.query.join(DbStaticInfo, (DbDynamicInfo.number == DbStaticInfo.number)).filter(DbDynamicInfo.last_update == max_value).all()
        dynamic_info = helpers.get_dynamic_data(static_table, dynamic_table)
        lat, lng, address, bikestands, available_bikes = ([] for i in range(5))
        lat = static_info['lat']
        lng = static_info['lng']
        address = static_info['address']
        bikestands = static_info['bikestands']
        available_bikes = dynamic_info['available_bikes']
        return render_template("index.html",
                               len = len(lat),
                               lat = lat,
                               lng = lng,
                               address = address,
                               bikestands = bikestands,
                               available_bikes = available_bikes)
    except:
        return "Error: unable to fetch data."


@app.route("/get_bike_info", methods=["POST"])
def get_bike_info():
    #Code works after 24/02/2019 at 5am. Possible issues with database.
    try:
        date_time = helpers.get_date_time().get_data(as_text=True)
        year = int(date_time[2:6])
        month = int(date_time[7:9])
        day = int(date_time[10:12])
        hour = int(date_time[15:17])
        minute = int(date_time[18:20])
        current_dt = datetime.datetime(year,month,day,hour,minute)
        #The max value selected is the largest value less than the date time entered by the user
        max_values = select([func.max(DbDynamicInfo.last_update)]).where(DbDynamicInfo.last_update <=current_dt)
        dynamic_table = DbDynamicInfo.query.join(DbStaticInfo, (DbDynamicInfo.number == DbStaticInfo.number)).filter(DbDynamicInfo.last_update == max_values).all()
        dynamic_bikes = helpers.get_dynamic_data(DbStaticInfo.query.all(),dynamic_table)
        dynamic_bikes = jsonify(dynamic_bikes)
        return dynamic_bikes
    except:
        return "Error: unable to fetch dynamic data."
    
@app.route("/infoWindow", methods=['POST'])
def infoWindow():
    try:
        #Rounding is used here as the lat and lng in the database has 6 decimal points but request.json['lng'] was giving more than that
        lat = round(request.json['lat'],7)
        lng = round(request.json['lng'],7)
        static_row = DbStaticInfo.query.filter(DbStaticInfo.lat == lat).filter(DbStaticInfo.lng == lng).all()
        static_info = helpers.get_static_data(static_row)
        max_value = select([func.max(DbDynamicInfo.last_update)]).where(DbDynamicInfo.number == static_info['number'][0])
        dynamic_table = DbDynamicInfo.query.join(DbStaticInfo, (DbDynamicInfo.number == static_info['number'][0])).filter(DbDynamicInfo.last_update == max_value).all()
        dynamic_info = helpers.get_dynamic_data(static_row, dynamic_table)
        address, bikestands, available_bikes = ([] for i in range(3))
        address = static_info['address']
        bikestands = static_info['bikestands']
        available_bikes = dynamic_info['available_bikes']
        results = json.dumps({"address":address,"bikestands":bikestands,"available_bikes":available_bikes})
        return results
    except:
        return "Error: unable to fetch data."
