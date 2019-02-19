# 190218_DublinBikeScraper.py

from requests import get
from json import loads
import sqlalchemy as sql
import csv

# URL for scraping
url = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=64f0cdd31dc5e915c6e192810317fb7971958fd3"

# Convert json to python object (list of dictionaries)
api_info = loads(get(url).text)

# Create SQL engine
# String:"mysql+pymysql://username:password@computer/database"
engine = sql.create_engine("mysql+pymysql://root:Jm30079!@localhost/test")

# Connect to SQL
connection = engine.connect()

# Create static and Dynamic Tables
create_static = "CREATE TABLE DbStaticInfo (number int primary key, " \
               "name varchar(50), address varchar(50), lat float(8,6), lng float(7,6), " \
                "bikestands int)"

create_dynamic = "CREATE TABLE DbDynamicInfo (id int primary key auto_increment, " \
                 "number int, status varchar(20), " \
                 "available_bike_stands int, available_bikes int, last_update datetime, " \
                 "CONSTRAINT FK_number FOREIGN KEY (number) REFERENCES DbStaticInfo(number))"

connection.execute(create_static)
connection.execute(create_dynamic)

# Iterate over api_info, build SQL insert
for i in api_info:
    insert = 'INSERT INTO DbStaticInfo VALUES (%d,"%s","%s",%.6f,%.6f,%d)' \
             % (i["number"],i["name"],i["address"],i["position"]["lat"],i["position"]["lng"],
                i["bike_stands"])

    # Execute SQL command
    connection.execute(insert)

# Back up to csv file
with open("DbStaticInfoBackUp.csv", "a") as csv_file:
    writer = csv.writer(csv_file)
    writer = csv.writer(csv_file)
    for i in api_info:
        writeRow = [i["number"],i["name"],i["address"],i["position"]["lat"],\
                i["position"]["lng"],i["bike_stands"]]
        writer.writerow(writeRow)

# Close sql connection
connection.close()