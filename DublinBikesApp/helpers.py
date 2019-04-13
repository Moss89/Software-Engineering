from flask import request, jsonify
import datetime
from requests import get
from json import loads

"""
Functions for the routes go here
"""

def get_static_data(table):

    results = {"number": [], "lat": [], "lng": [], "address": [], "bikestands": []}
    for i in range(len(table)):
        results["number"].append(table[i].number)
        results["lat"].append(table[i].lat)
        results["lng"].append(table[i].lng)
        results["address"].append(table[i].address)
        results["bikestands"].append(table[i].bikestands)
    return results


def get_dynamic_data(static_table, dynamic_table):

    results = {"available_bikes": [], "address": []}
    for i in range(len(dynamic_table)):
        results["address"].append(static_table[i].address)
        results["available_bikes"].append(dynamic_table[i].available_bikes)
    return results


def get_date_time():
    date = request.json['date']
    time = request.json['time']
    date_time = datetime.datetime(int(date[0:4]),int(date[5:7]),int(date[8:10]),int(time[0:2]),int(time[3:5]))
    weekday = date_time.weekday()
    return (date_time,weekday)

def get_lat_lng():
    #Rounded to 6 decimal points to match with database lat and lng data entry.
    lat = round(request.json['lat'],7)
    lng = round(request.json['lng'],7)
    return (lat,lng)

def getWeather(t):

    # Scrape weather API
    r = get(
        "https://api.openweathermap.org/data/2.5/forecast/?q=dublin&APPID=718d1e3d695907c31b9a4b710e8348f5&units=metric&cnt=200&mode=json").text
    # Convert scrape to python dict
    r = loads(r)
    print("s", t)
    i = 1
    # Find correct weather info
    while t < r["list"][i]["dt"]:
        print(i)
        r["list"][i]["main"]["temp"]
        i += 1
    print(r["list"][i])
    return r["list"][i]
    
    
