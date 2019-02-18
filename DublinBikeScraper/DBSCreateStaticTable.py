# 190218_DublinBikeScraper.py

from requests import get
from json import loads
import sqlalchemy as sql
import csv

# URL for scraping
url = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=64f0cdd31dc5e915c6e192810317fb7971958fd3"

# Convert json to python object (list of dictionaries)
apiInfo = loads(get(url).text)

# Create SQL engine
# String:"mysql+pymysql://username:password@computer/database"
engine = sql.create_engine("mysql+pymysql://root:Jm30079!@localhost/test")

# Connect to SQL
connection = engine.connect()

# Iterate over api_info, build SQL insert
for i in apiInfo:
    insert = 'INSERT INTO DbStaticInfo VALUES (%d,"%s","%s",%.6f,%.6f)' \
             % (i["number"],i["name"],i["address"],i["position"]["lat"],i["position"]["lng"])

    # Execute SQL command
    connection.execute(insert)

# Back up to csv file
with open("DbStaticInfoBackUp.csv", "a") as csv_file:
    writer = csv.writer(csv_file)
    writer = csv.writer(csv_file)
    for i in apiInfo:
        writeRow = [i["number"],i["name"],i["address"],i["position"]["lat"],\
                i["position"]["lng"]]
        print(writeRow)
        writer.writerow(writeRow)

# Close sql connection
connection.close()