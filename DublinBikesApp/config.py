import os
basedir = os.path.abspath(os.path.dirname(__file__))

"""
Config file for setting up database stuff
"""

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://JohnH:comp30830tj@dbbikes.ca8jj5ksuurt.eu-west-1.rds.amazonaws.com:3306/dbbikes"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
