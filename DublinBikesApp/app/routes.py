from flask import render_template, jsonify
from app import app
from app.models import DbStaticInfo, DbDynamicInfo
import helpers
import requests
import datetime
import time
from sqlalchemy.sql.expression import func, distinct
from sqlalchemy.sql import select
from sqlalchemy import and_
from _datetime import date
from alembic.command import current
from jedi.evaluate import dynamic


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
        available_bikes = helpers.get_dynamic_data(DbStaticInfo.query.all(),dynamic_table)
        return str(available_bikes)
    except:
        return "Error: unable to fetch dynamic data."