from app.routes import db

SubjectLevel = db.Table('SubjectLevel', db.Model.metadata, 
    db.Column('sid', db.Integer, db.ForeignKey('Subject.id')),
    db.Column('lid', db.Integer, db.ForeignKey('Level.id'))
    )

SubjectTutor = db.Table('SubjectTutor', db.Model.metadata,
    db.Column('sid', db.Integer, db.ForeignKey('Subject.id')),
    db.Column('tid', db.Integer, db.ForeignKey('Tutor.id'))
    )

TutorTime = db.Table('TutorTime', db.Model.metadata, 
    db.Column('tuid', db.Integer, db.ForeignKey('Tutor.id')),
    db.Column('tiid', db.Integer, db.ForeignKey('Time.id'))
    )

#linking the many to many tables in the database to the code?
# derived from Mr Dunford's Replit page. 


class Time(db.Model):
    __tablename__ = "Time"
    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.String())
    time_in_day = db.Column(db.String())

    tutors = db.relationship('Tutor', secondary=TutorTime, back_populates='times')


class Level(db.Model):
    __tablename__ = 'Level'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    subjects = db.relationship('Subject', secondary=SubjectLevel, back_populates='levels')




class Subject(db.Model):
    __tablename__ = "Subject"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    levels = db.relationship('Level', secondary=SubjectLevel, back_populates='subjects')
    tutors = db.relationship('Tutor', secondary=SubjectTutor, back_populates='subjects')


class Tutor(db.Model):
    __tablename__ = "Tutor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    
    subjects = db.relationship('Subject', secondary=SubjectTutor, back_populates='tutors')
    times = db.relationship('Time', secondary=TutorTime, back_populates='tutors')

    def __repr__(self):
        return self.name