from flask import Flask
import mysql.connector
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def connect_to_database():
    """Function queries an sql database and returns a list of items"""
    
    cnx = mysql.connector.connect(user='JohnH', password='comp30830tj',
                                  host='dbbikes.ca8jj5ksuurt.eu-west-1.rds.amazonaws.com',
                                  port = '3306',
                                  database='dbbikes')
    #Create a cursor object to query database
    cursor = cnx.cursor()
    #Create some basic sql commands.
    sql = "Select address,lat,lng from DbStaticInfo"
    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        lat = []
        lng = []
        address = []
        for i in range(len(results)):
            #Obtaining the relevant information
            address.append(results[i][0]) 
            lat.append(results[i][1])
            lng.append(results[i][2])  
        return render_template('index.html',len=len(lat), lat=lat, lng=lng, address=address)
    except:
        print("Error:unable to fetch data.")
    cnx.close()
if __name__ == '__main__':
    app.run(debug=True)