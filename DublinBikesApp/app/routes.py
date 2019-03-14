from flask import render_template, jsonify
from app import app
from app.models import DbStaticInfo, DbDynamicInfo
import helpers
import requests
from sqlalchemy.sql.expression import func
from sqlalchemy.sql import select

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
        query = (str(date_time[2:12]) + " " + str(date_time[15:20]))
        available_bikes = helpers.get_dynamic_data(DbStaticInfo.query.join(DbDynamicInfo, (DbDynamicInfo.number == DbStaticInfo.number)).filter(DbDynamicInfo.last_update >= query), DbDynamicInfo.query.filter(DbDynamicInfo.last_update >= query))
        return str(available_bikes)
    except:
        return "Error: unable to fetch dynamic data."