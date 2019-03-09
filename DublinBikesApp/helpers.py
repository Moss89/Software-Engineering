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


def get_dynamic_data(static_table, dynamic_table):

    results = {"available_bikes": [], "address": []}
    for i in range(0,113):
        results["address"].append(static_table[i].address)
        results["available_bikes"].append(dynamic_table[i].available_bikes)
    return results


def get_date_time():

    date =  request.form['date'];
    time = request.form['time'];
    return jsonify(date, time)
