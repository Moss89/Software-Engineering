from app import db

# Models for orm sql stuff
# IDE sometimes says app stuff doesn't exist but works


class DbStaticInfo(db.Model):
    __tablename__ = "DbStaticInfo"

    number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    lat = db.Column(db.Float())
    lng = db.Column(db.Float())
    bikestands = db.Column(db.Integer)

    def __repr__(self):
        return "<DbStaticInfo {}>".format(self.name)


class DbDynamicInfo(db.Model):
    __tablename__ = "DbDynamicInfo"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, db.ForeignKey("DbStaticInfo.number"))
    status = db.Column(db.String(20))
    available_bike_stands = db.Column(db.Integer)
    available_bikes = db.Column(db.Integer)
    last_update = db.Column(db.DateTime)
    weekday = db.Column(db.Integer)

    def __repr__(self):
        return "<DbStaticInfo {}>".format(self.id)