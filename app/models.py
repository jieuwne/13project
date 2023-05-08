from app.routes import db

class Tutors(db.Model):
    __tablename__ = "Tutors"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    Times = db.Column(db.Integer, db.ForeignKey("Times.id"))
    Times_day_of_week = db.relationship("Times", backref = "Tutors")

class Times(db.Model):
    __tablename__ = "Times"
    id = db.Column(db.Integer, primary_key = True)
    day_of_week = db.Column(db.String())
    time_in_day = db.Column(db.Integer())

class Subject(db.Model):
    __tablename__ = "Subject"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    level = db.Column(db.Integer())


