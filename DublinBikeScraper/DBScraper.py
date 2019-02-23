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
engine = sql.create_engine("mysql+pymysql://jmcl:Jm30079!@dbbikes.ca8jj5ksuurt.eu-west-1.rds.amazonaws.com:3306/test")


def probe_api():

    """
    Queries Dublin Bikes API
    Returns API info:list of dictionaries
    """

    info = loads(get(url).text)
    return info


def create_sql_write(api):

    """
    Takes API info as input
    Returns SQL inserts:list
    """

    inserts = []

    for info in api:
        time: str = datetime.utcfromtimestamp(info["last_update"]/1000).strftime("%Y-%m-%d %H:%M:%S")
        inserts.append('INSERT INTO DbDynamicInfo (number, status, available_bike_stands, '
                       'available_bikes, last_update) '
                       'VALUES (%d,"%s",%d,%d,"%s")'
                       % (info["number"], info["status"], info["available_bike_stands"],
                          info["available_bikes"], time))

    return inserts


def write_to_database(info):
    """
    Takes SQL write as input
    Executes SQL write on database
    """

    inserts = create_sql_write(info)

    connection = engine.connect()
    for insert in inserts:
        connection.execute(insert)
    connection.close()


def build_csv_write(api):
    """
    Takes API info, creates CSV write
    Returns CSV write:list
    """

    write_rows = []
    for info in api:
        time = datetime.utcfromtimestamp(info["last_update"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
        write_rows.append([info["number"], info["status"], info["available_bike_stands"],
                           info["available_bikes"], time])

    return write_rows


def write_to_csv_backup(api_info):
    """
    Backs up API info to csv file
    """

    rows = build_csv_write(api_info)

    with open("DbDynamicInfoBackUp.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        for i in rows:
            writer.writerow(i)


# Main loop
while True:
    # try and except in case api down
    try:
        api_info = probe_api()
        write_to_database(api_info)
        #write_to_csv_backup(api_info)
        sleep(5*60)
    except:
        print(traceback.format_exc())