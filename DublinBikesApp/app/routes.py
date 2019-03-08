from flask import render_template
from app import app
from app.models import DbStaticInfo
import helpers

"""
Create the different routes here
"""

@app.route("/")
@app.route("/index")
def index():
    try:
        static_info = helpers.get_static_data(DbStaticInfo.query.all())
        return render_template("index.html", len=len(static_info["lat"]),
                               lat=static_info["lat"],
                               lng=static_info["lng"],
                               address=static_info["address"])
    except:
        return "Error: unable to fetch data"