from flask import render_template, jsonify
from app import app
from app.models import DbStaticInfo, DbDynamicInfo
import helpers
import requests

"""
Create the different routes here
"""

@app.route("/")
@app.route("/index", methods=['POST'])
def index():
    try:
        static_info = helpers.get_static_data(DbStaticInfo.query.all())
        return render_template("index.html", len=len(static_info["lat"]),
                               lat=static_info["lat"],
                               lng=static_info["lng"],
                               address=static_info["address"])
    except:
        return "Error: unable to fetch data"


@app.route("/get_bike_info", methods=["POST"])
def get_bike_info():
    date_time = helpers.get_date_time().get_data(as_text=True)
    query = (str(date_time[2:12]) + " " + str(date_time[15:20]))
    available_bikes = helpers.get_dynamic_data(DbStaticInfo.query.join(DbDynamicInfo, (DbDynamicInfo.number == DbStaticInfo.number)).filter(DbDynamicInfo.last_update >= query), DbDynamicInfo.query.filter(DbDynamicInfo.last_update >= query))
    return str(available_bikes)