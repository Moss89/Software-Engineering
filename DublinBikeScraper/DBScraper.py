# 190218_DublinBikeScraper.py

from requests import get
from json import loads
import sqlalchemy as sql
import csv
from time import sleep
import traceback

url = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=64f0cdd31dc5e915c6e192810317fb7971958fd3"

engine = sql.create_engine("mysql+pymysql://root:Jm30079!@localhost/test")


def writesql():


    api_info = loads(get(url).text)

    connection = engine.connect()

    for i in api_info:
        insert = 'INSERT INTO DbDynamicInfo (number, status, bikestands, available_bike_stands, available_bikes, last_update) ' \
                 'VALUES (%d,"%s",%d,%d,%d,%d)' \
                 % (i["number"],i["status"],i["bike_stands"],i["available_bike_stands"],
                    i["available_bikes"],i["last_update"])

        connection.execute(insert)

    connection.close()

    with open("DbDynamicInfoBackUp.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        writer = csv.writer(csv_file)
        for i in api_info:
            writeRow = [i["number"],i["status"],i["bike_stands"],i["available_bike_stands"],
                    i["available_bikes"],i["last_update"]]
            writer.writerow(writeRow)


while True:
    try:
        writesql()
        sleep(5*60)
    except:
        print(traceback.format_exc())

