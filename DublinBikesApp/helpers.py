from flask import request
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


def get_date_time():
    date = request.json['date']
    time = request.json['time']
    date_time = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]), int(time[0:2]), int(time[3:5]))
    weekday = date_time.weekday()
    return date_time, weekday


def get_lat_lng():
    # Rounded to 6 decimal points to match with database lat and lng data entry.
    lat = round(request.json['lat'], 7)
    lng = round(request.json['lng'], 7)
    return lat, lng


def getWeather(t):

    # Scrape weather API
    r = get(
        "https://api.openweathermap.org/data/2.5/forecast/?q=dublin&APPID=718d1e3d695907c31b9a4b710e8348f5&units=metric&cnt=200&mode=json").text
    # Convert scrape to python dict
    r = loads(r)

    # Iterate over weather info and get relevant weather
    for i in range(1, len(r["list"])):
        if r["list"][i - 1]["dt"] < t < r["list"][i]["dt"]:
            return r["list"][i]

    # Used if search up to 3 hours from current
    return r["list"][0]


def formatWeatherInfo(weather, date_time, day):
    # Dictionaries for converting weather strings to numeric representation
    descriptionDict = {'broken clouds': 0,
                       'scattered clouds': 1,
                       'few clouds': 2,
                       'clear sky': 3,
                       'mist': 4,
                       'fog': 5,
                       'light rain': 6,
                       'moderate rain': 7,
                       'heavy intensity rain': 8,
                       'very heavy rain': 9,
                       'snow': 10,
                       'light intensity shower rain': 11,
                       'shower rain': 12,
                       'light intensity drizzle': 13,
                       'shower sleet': 14,
                       'light intensity drizzle rain': 15,
                       'drizzle': 16,
                       'overcast clouds': 17}

    overviewDict = {'Rain': 0,
                    'Clouds': 1,
                    'Fog': 2,
                    'Snow': 3,
                    'Clear': 4,
                    'Mist': 5,
                    'Drizzle': 6}

    # Formatting info for passing to model
    overview = weather["weather"][0]["main"]
    description = weather["weather"][0]["description"]
    temp = weather["main"]["temp"]
    windSpeed = weather["wind"]["speed"]
    clouds = weather["clouds"]["all"]
    info = [date_time, day, overview, description, temp, windSpeed, clouds]

    # In case weather unknown at the time encountered use this
    if overview not in overviewDict.keys():
        info[2] = 20
    else:
        info[2] = overviewDict[info[2]]
    if description not in descriptionDict.keys():
        info[3] = 20
    else:
        info[3] = descriptionDict[info[3]]

    return info


def formatDateTime(date_time):
    day = date_time[1]
    date_time = int(date_time[0].strftime('%s'))

    return date_time, day