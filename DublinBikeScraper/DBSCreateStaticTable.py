# 190218_DublinBikeScraper.py

from requests import get
from json import loads
import sqlalchemy as sql
import csv

url = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=64f0cdd31dc5e915c6e192810317fb7971958fd3"

apiInfo = loads(get(url).text)

engine = sql.create_engine("mysql+pymysql://root:Jm30079!@localhost/test")

connection = engine.connect()
"""
for i in apiInfo:
    insert = 'INSERT INTO DbStaticInfo VALUES (%d,"%s","%s",%.6f,%.6f)' \
             % (i["number"],i["name"],i["address"],i["position"]["lat"],i["position"]["lng"])

    connection.execute(insert)
"""
with open("DbStaticInfoBackUp.csv", "a") as csv_file:
    writer = csv.writer(csv_file)
    writer = csv.writer(csv_file)
    for i in apiInfo:
        writeRow = [i["number"],i["name"],i["address"],i["position"]["lat"],\
                i["position"]["lng"]]
        print(writeRow)
        writer.writerow(writeRow)

connection.close()