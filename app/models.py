from app.routes import db


class Times(db.Model):
    __tablename__ = "Times"
    id = db.Column(db.Integer, primary_key = True)
    day_of_week = db.Column(db.String())
    time_in_day = db.Column(db.Integer())

SubjectLevel = db.Table('SubjectLevel', db.Model.metadata, 
    db.Column('Subject_id', db.Integer, db.ForeignKey('Subject.id')),
    db.Column('Level_id', db.Integer, db.ForeignKey('Level.id'))
    )

SubjectTutor = db.Table('SubjectTutor', db.Model.metadata,
    db.Column('Subject_id', db.Integer, db.ForeignKey('Subject.id')),
    db.Column('Tutor_id', db.Integer, db.ForeignKey('Tutor.id'))
    )

class Level(db.Model):
    __tablename__='Level'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    description = db.Column(db.Text)

    subject = db.relationship('Subject', secondary=SubjectLevel, back_populates='levels')

class Subject(db.Model):
    __tablename__ = "Subject"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    description = db.Column(db.String())

    levels = db.relationship('Level', secondary=SubjectLevel, back_populates='subjects')
    tutors = db.relationship('Tutor', secondary=SubjectTutor, back_populates='tutors')


class Tutors(db.Model):
    __tablename__ = "Tutors"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    
    subject = db.relationship('Subject', secondary=SubjectTutor, back_populates='subjects')
