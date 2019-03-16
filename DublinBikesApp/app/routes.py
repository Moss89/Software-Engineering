from flask import render_template, jsonify
from app import app
from app.models import DbStaticInfo, DbDynamicInfo
import helpers
import requests
import datetime
import time
from sqlalchemy.sql.expression import func
from sqlalchemy.sql import select
from sqlalchemy import and_
from _datetime import date
from alembic.command import current


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
        #The date time is passed as text which is then sliced and turned into epoch time.
        date_time = helpers.get_date_time().get_data(as_text=True)
        year = int(date_time[2:6])
        month = int(date_time[7:9])
        day = int(date_time[10:12])
        hour = int(date_time[15:17])
        minute = int(date_time[18:20])
        #Each row in the database is correct to a five minute period. The below code sets up the range between the entered time and date and five minutes later
        current_dt = str(datetime.datetime(year,month,day,hour,minute))
        #If statements not complete. Might change to unix time to simplify process
        #if(minute >= 55):
        #    hour += 1
        #    minute = minute - 55
        #    if (hour == 24):
        #        day += 1
        #        hour -= 24
        #        month +=1
        five_minutes_dt = str(datetime.datetime(year,month,day,hour,minute+5))
        #The code below joins a table which contains all the stations between the two time ranges which should gives one result per station
        #This code takes a while and doesn't seem to work at times from hr:55 to hr:59. Overflow will need to be implemented
        table_1 = DbDynamicInfo.query.join(DbStaticInfo, (DbDynamicInfo.number == DbStaticInfo.number)).filter(and_(DbDynamicInfo.last_update >= current_dt,DbDynamicInfo.last_update < five_minutes_dt))
        available_bikes = helpers.get_dynamic_data(DbStaticInfo.query.all(),table_1)
        return str(available_bikes)
    except:
        return "Error: unable to fetch dynamic data."