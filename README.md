# Table Of Contents
- Introduction
- Features
- Documentation
- Prerequisites
- Install
- Contributions
- License

## Introduction

Find A Bike Dublin is a web application designed to allow users to find the best Dublin Bikes Station in their vicinity to either rent out a bike or leave a bike back.  To launch an instance, just clone it, navigate to the DublinBIkesApp folder and type flask run.  Due to our repsonsive design, the application is easily viewable on all device from laptops to phones and everything in between.

## Features

- __Real time bike info:__ Find information both on how many bikes are available at each bikestand and how many bike stands are also available. 

- __Map showing bike stand locations:__ Not only does the app provide information on the number of bikes and bikestands available, through google maps integration, it also displays their location on a map, allowing the user to quickly locate the nearest bike station suitable for their needs.

- __Expertly crafted GUI:__ The GUI has been crafted to be both easy to understand and intuitive to use.  It's design has been kept as minimal as possible so that the user can access information about the various bike stations dotted around Dublin as quickly as possible.

## Documentation

- Comprehensive documentation on the use of the app is available to each user via a separate webpage present in the app

- Other documentation can also be found in the quick start guide and FAQ also available on git hub.

## Prerequisites

### Flask

Find A Bike Dublin requires flask 1.0.2 or above. It also makes use of several flask expansions which are listed below:

- flask-sqlalchemy 2.3.2
- flask-migrate 2.4.0
- flask-wtf 0.14.2

### SQLAlchemy

Find A Bike Dublin also requires sqlalchemy 1.3.0 for sql operations.

### Anaconda Virtual Environment

Find A Bike Dublin makes use of Conda virtual environments, the version used is 4.6.2.

## Installation

1. Clone the git hub repository with the following url:
        $ git clone https://github.com/Moss89/DublinBikesProject.git
2. Navigate to the DublinBikesApp folder:
        $ cd /DublinBikesProject/DublinBikesApp
3. Pip install the requirements.txt file:
        $ pip install -r requirements.txt
4. Run the flask app:
        $ flask run

## Contributions

- John Hackett
- Tomas Murphy
- John McLoughlin

## License

The license is GPL3 for all parts specific to Find A Bike Dublin, this includes:

- The core files
- The documentaion
