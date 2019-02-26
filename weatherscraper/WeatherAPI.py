#################################
#  Author: Tomas Murphy         #
#  Date:   19/02/19             #
#  Function: Openweathermaps    #
#            API scraper.       #
#################################

from requests import get
from json import loads
import sqlalchemy as sql
import csv
from time import sleep
from datetime import datetime
import traceback

# Openweathermap API URL & key
url = "http://api.openweathermap.org/data/2.5/weather?q=Dublin&APPID=718d1e3d695907c31b9a4b710e8348f5"

# Connect to database
engine = sql.create_engine("mysql+pymysql://tomM:comp30830tj@dbbikes.ca8jj5ksuurt.eu-west-1.rds.amazonaws.com:3306/dbbikes")
connection = engine.connect()

# Create weather table if it doesn't exist
create_table = "CREATE TABLE IF NOT EXISTS weather (number int primary key auto_increment, " \
                "datetime varchar(50), overview varchar(50), description varchar(50), temperature float(6,3)," \
                "humidity float(4,2), wind_speed float (5,2), clouds float(5,2))"

connection.execute(create_table)

# Close connection
connection.close()

def writesql():
    connection = engine.connect()

    #Get API data
    api_info = loads(get(url).text)
    print(api_info)

    # Convert timestamp into human readable time
    time = datetime.utcfromtimestamp(api_info["dt"]).strftime("%Y-%m-%d %H:%M:%S")

    # Insert data into table
    insert = 'INSERT INTO weather (datetime, overview, description, temperature, humidity, wind_speed, clouds)' \
                 'VALUES ("%s","%s","%s",%d,%d,%d,%d)' \
                 % (time,api_info["weather"][0]["main"],api_info["weather"][0]["description"], api_info["main"]["temp"],
                    api_info["main"]["humidity"], api_info["wind"]["speed"], api_info["clouds"]["all"])

    connection.execute(insert)

    connection.close()

    # Write data to a test csv
    with open("weather.csv", "a", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writeRow = [time, api_info["weather"][0]["main"],api_info["weather"][0]["description"],
                    api_info["main"]["temp"], api_info["main"]["humidity"], api_info["wind"]["speed"], api_info["clouds"]["all"]]
        writer.writerow(writeRow)

# Run code ever 10 minutes
while True:
    try:
        writesql()
        sleep(10*60)

    except:
        print(traceback.format_exc())

