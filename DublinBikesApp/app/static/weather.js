/*
########################################################
# Author: Tomas Murphy                                 #
# Description: Javascript for the weather and          #
# date-time picker.                                    #
########################################################
*/

// Function called on page load to get weather XML from openweatherdata
function currentWeather() {

            var currentxhttp = new XMLHttpRequest();
            currentxhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    currentW(this);
                }
            };
            currentxhttp.open("GET", "https://api.openweathermap.org/data/2.5/weather?q=dublin&APPID=718d1e3d695907c31b9a4b710e8348f5&units=metric&cnt=200&mode=xml", false);
            currentxhttp.send();
        }

// Extract data from XML and pass data to weather widget
        function currentW(xml) {
            var xmlDoc = xml.responseXML;

            myX = xmlDoc.getElementsByTagName("symbol");

            var x = xmlDoc.getElementsByTagName("current")[0];

            var temp = x.childNodes[1];
            var temperature = temp.getAttribute('value');
            // Update the inner HTML of the weather widget.
            document.getElementById("temp").innerHTML = temperature;

            var wind = x.childNodes[4].childNodes[0];
            var windspeed = wind.getAttribute('value');
            document.getElementById("wind").innerHTML = windspeed;

            var precip = x.childNodes[7];
            var precipitation = precip.getAttribute('value');
            if (precipitation == null) {
                precipitation = 0;
            }
            document.getElementById("precip").innerHTML = precipitation;

            var weather = x.childNodes[8];
            var overview = weather.getAttribute('value');

            weatherIcons(overview);

        }

// Called upon clicking the submit button to get openweathermap's forecast XML.

function futureWeather() {
    var xhttp = new XMLHttpRequest();
    // Taking weather and date values from the input sections of the website.
    var date = document.getElementById("date").value;
    var time = document.getElementById("time").value;

    // Formatting a date time string to match the openweathermap XML format.
    var dateTime = date.toString() + "T" + time.toString()
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // Pass the date time string.
            futureW(this,dateTime);
        }
    };
    xhttp.open("GET", "https://api.openweathermap.org/data/2.5/forecast/?q=dublin&APPID=718d1e3d695907c31b9a4b710e8348f5&units=metric&cnt=200&mode=xml", false);
    xhttp.send();
}
        // Used to find future weather at a specified day/time and update the weather widget.
        function futureW(xml, dateTime) {

            var xmlDoc = xml.responseXML;

            /* The weather forecast only gives the forecast in 3 hour chunks (00:00, 03:00, 06:00 etc.)
                and thus the user inputted time needs to be formatted and rounded to match the closest forecast time.
                For example, any times from 23:00 to 01:00 are made to equal 00:00, any times from 17:00 to 19:00
                are made equal to 18:00 and so on.
            */
            var pos = dateTime.search("T");
            var formatDate = dateTime.slice(0,pos);

            var formatTime = dateTime.slice(pos+1,pos+3);
            newString = "";
            // Getting the hour, and assigning it to the closest 3 hour block
            switch(formatTime) {
              case "23": case "00": case "01":
                newString = ""+ formatDate + "T" + "00:00:00"
                break;
              case "02": case "03": case "04":
                newString = ""+ formatDate + "T" + "03:00:00"
                break;
              case "05": case "06": case "07":
                  newString = ""+ formatDate + "T" + "06:00:00"
                  break;
              case "08": case "09": case "10":
                  newString = ""+ formatDate + "T" + "09:00:00"
                  break;
              case "11": case "12": case "13":
                  newString = ""+ formatDate + "T" + "12:00:00"
                  break;
              case "14": case "15": case "16":
                  newString = ""+ formatDate + "T" + "15:00:00"
                  break;
              case "17": case "18": case "19":
                  newString = ""+ formatDate + "T" + "18:00:00"
                  break;
              case "20": case "21": case "22":
                  newString = ""+ formatDate + "T" + "21:00:00"
                                break;
              default:
              // Fancy looking alert box for errors
                 swal({
                      title:"Whoops!",
                      text: "This website can predict bike availability up to exactly 5 days from this current time! \n\n Please enter a date and time within a 5 day period from now :)",
                      icon: "warning"})

                break;
            }


            // Check if the date and time are in the forecast
            myX = xmlDoc.getElementsByTagName("symbol");
            var found = false;
            for (i = 0; i < myX.length; i++) {

                var x = xmlDoc.getElementsByTagName("forecast")[0];
                var y = x.childNodes[i];
                var time = y.getAttribute('from');

                // If the date time is present, then update the weather widget
                if (newString == time) {
                    found = true;
                    var weather = x.childNodes[i].childNodes[0];
                    var overview = weather.getAttribute('name');


                    var temp = x.childNodes[i].childNodes[4];
                    var temperature = temp.getAttribute('value');
                    document.getElementById("temp").innerHTML =
                        temperature;

                    var wind = x.childNodes[i].childNodes[3];
                    var windspeed = wind.getAttribute('mps');
                    document.getElementById("wind").innerHTML = Number.parseFloat(windspeed).toFixed(1);

                    var precip = x.childNodes[i].childNodes[1];
                    var precipitation = precip.getAttribute('value');
                    if (precipitation == null) {
                        precipitation = 0;
                    }
                    var pointNum = parseFloat(precipitation);
                    document.getElementById("precip").innerHTML = Number.parseFloat(precipitation).toFixed(2);


                    var clouds = x.childNodes[i].childNodes[7];
                    var cloudspeed = clouds.getAttribute('value');

                    weatherIcons(overview);

                         break;
                }


            }
            // If not found, then show the fancy alert message
            if (found == false){
                swal({
                      title:"Whoops!",
                      text: "This website can predict bike availability up to exactly 5 days from this current time! \n\n Please enter a date and time within a 5 day period from now :)",
                      icon: "warning"})
            }
        }
                // The type of weather that is returned as part of the overview decides the weather icon used in the weather widget.
                    function weatherIcons(overview){
                    if (overview.includes("thunderstorm")) {
                        document.getElementById("image").innerHTML = "<i class='fas fa-bolt' style='font-size:84px;'></i>";
                    } else if (overview.includes("drizzle")) {
                        document.getElementById("image").innerHTML = "<i class='fas fa-cloud-rain' style='font-size:84px;'></i>";
                    } else if (overview.includes("snow") || overview.includes("sleet")) {
                        document.getElementById("image").innerHTML = "<i class='far fa-snowflake' style='font-size:84px;'></i>";
                    } else if (overview == "light rain") {
                        document.getElementById("image").innerHTML = "<i class='fas fa-cloud-sun-rain' style='font-size:84px;'></i>";
                    } else if (overview.includes("rain")) {
                        document.getElementById("image").innerHTML = "<i class='fas fas fa-cloud-showers-heavy' style='font-size:84px;'></i>";
                    } else if (overview == "clear sky") {
                        document.getElementById("image").innerHTML = "<i class='fas fa-sun' style='font-size:84px;'></i>";
                    } else if (overview.includes("clouds")) {
                        document.getElementById("image").innerHTML = "<i class='fas fa-cloud-sun' style='font-size:84px;'></i>";

                    } else {
                        document.getElementById("image").innerHTML = "<i class='fas fa-smog' style='font-size:84px;'></i>";
                    }

        }
        // Current weather info is used to populate the weather widget on page load.
        window.onload = currentWeather;
