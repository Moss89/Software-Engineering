# 190218_DublinBikeScraper.py

"""
Needed to run script in background
Need to chmod +x script for this to work
Execute script with python3
Send to background with ctrl+z
Run in background with bg cmd
Note file path may be different depending on how env is set up

"""
#!//home/ubuntu/anaconda3/envs/comp30830/bin python3.7

from requests import get
from json import loads
import sqlalchemy as sql
import csv
from time import sleep
from datetime import datetime
import traceback


# URL for scraping
url = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=64f0cdd31dc5e915c6e192810317fb7971958fd3"

# Create SQL engine
# String:"mysql+pymysql://username:password@computer/database"
engine = sql.create_engine("mysql+pymysql://root:Jm30079!@localhost/test")

# Method to write to sql database
def writesql():
    """
    Writes rows to SQL table
    Takes no input, output is new rows in SQL table
    """

    # Convert json to python object (list of dictionaries)
    api_info = loads(get(url).text)

    # Connect to SQL
    connection = engine.connect()



    # Iterate over api_info, build SQL insert
    for i in api_info:
        time = datetime.utcfromtimestamp(i["last_update"]/1000).strftime("%Y-%m-%d %H:%M:%S")
        insert = 'INSERT INTO DbDynamicInfo (number, status, available_bike_stands, ' \
                 'available_bikes, last_update) ' \
                 'VALUES (%d,"%s",%d,%d,"%s")' \
                 % (i["number"],i["status"],i["available_bike_stands"],\
                    i["available_bikes"], \
                    time)

        # Execute SQL command
        connection.execute(insert)

    # Close sql connection
    connection.close()

    # Back up to csv file
    with open("DbDynamicInfoBackUp.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        writer = csv.writer(csv_file)
        for i in api_info:
            time = datetime.utcfromtimestamp(i["last_update"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
            writeRow = [i["number"],i["status"],i["available_bike_stands"],
                    i["available_bikes"],time]
            writer.writerow(writeRow)

# Main loop
while True:
    # try and except in case api down
    try:
        writesql()
        sleep(5*60)
    except:
        print(traceback.format_exc())

