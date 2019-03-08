from flask import request, jsonify

"""
Functions for the routes go here
"""

def get_static_data(table):

    results = {"lat": [], "lng": [], "address": []}
    for i in range(len(table)):
        results["lat"].append(table[i].lat)
        results["lng"].append(table[i].lng)
        results["address"].append(table[i].address)
    return results


def get_dynamic_data(table):

    results = {"available_bikes": [], "available_bike_stands": []}
    for i in range(len(table)):
        results["available_bike_stands"].append(table[i].available_bike_stands)
    return results


def get_datetime():
    if request.method == "POST":
        submitted_datetime = request.get_json()
        print(submitted_datetime)
    return submitted_datetime