# 190226_FlaskSQL.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Jm30079!@localhost/test"

db = SQLAlchemy(app)

class DbStaticInfo(db.Model):
    __tablename__ = "DbStaticInfo"

    number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    lat = db.Column(db.Float()) #8,6
    lng = db.Column(db.Float()) #7,6
    bikestands = db.Column(db.Integer)

    def __repr__(self):
        return "<DbStaticInfo %r>" % self.name

@app.route("/")
def index():
    test = DbStaticInfo.query.filter_by()

    #return "<h1>Hello</h1>"

if __name__ == "__main__":
    app.run(debug=True)

