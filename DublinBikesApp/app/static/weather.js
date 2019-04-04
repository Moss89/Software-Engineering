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



        function currentW(xml) {
            var xmlDoc = xml.responseXML;

            myX = xmlDoc.getElementsByTagName("symbol");

            var x = xmlDoc.getElementsByTagName("current")[0];

            var temp = x.childNodes[1];
            var temperature = temp.getAttribute('value');
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


function searchXML() {
    var xhttp = new XMLHttpRequest();
    var date = document.getElementById("date").value;
    var time = document.getElementById("time").value;

    var dateTime = date.toString() + "T" + time.toString()
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myFunction(this,dateTime);
        }
    };
    xhttp.open("GET", "https://api.openweathermap.org/data/2.5/forecast/?q=dublin&APPID=718d1e3d695907c31b9a4b710e8348f5&units=metric&cnt=200&mode=xml", false);
    xhttp.send();
}

        function myFunction(xml, dateTime) {

            var xmlDoc = xml.responseXML;

            var pos = dateTime.search("T");
            var formatDate = dateTime.slice(0,pos);

            var formatTime = dateTime.slice(pos+1,pos+3);
            newString = "";

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
                alert("An error has occurred; please try again")
                break;
            }



            myX = xmlDoc.getElementsByTagName("symbol");
            for (i = 0; i < myX.length; i++) {

                var x = xmlDoc.getElementsByTagName("forecast")[0];
                var y = x.childNodes[i];
                var time = y.getAttribute('from');
                if (newString == time) {
                    var weather = x.childNodes[i].childNodes[0];
                    var overview = weather.getAttribute('name');


                    var temp = x.childNodes[i].childNodes[4];
                    var temperature = temp.getAttribute('value');
                    document.getElementById("temp").innerHTML =
                        temperature;

                    var wind = x.childNodes[i].childNodes[3];
                    var windspeed = wind.getAttribute('mps');
                    document.getElementById("wind").innerHTML =
                        windspeed;

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
        }


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
        window.onload = currentWeather;
