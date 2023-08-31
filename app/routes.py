from app import app
from flask import render_template, abort
from flask_sqlalchemy import SQLAlchemy 
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "tutoring.db")
db.init_app(app)

import app.models as models


@app.route('/')
def home():
    return render_template('home.html', page_title='The Website')


@app.route('/level/<int:level>')
def show_level(level):
    if level < 1 or level > 3:
        abort(404)
    subject_in_level = models.Subject.query.all()
    for result in subject_in_level:
        if result.levels == level:
            print(result) 


    return render_template('levels.html', page_title='LEVEL', subject_in_level=subject_in_level, level=level)
  

@app.route('/tutors/<subject>/<int:level>')
def tutor_subject(subject,level):
    subjects = models.Subject.query.all()
    for results in subjects:
        if results.name == subject and results.levels[0].id == level:
            print(results.tutors)

    return render_template('tutor_for_level.html', page_title='TUTOR', subject = subject, subjects=subjects, level=level)


@app.route('/all_tutors')
def all_tutors():
    tutor_name = models.Tutor.query.all()
    for result in tutor_name:
        print(result)
        
    return render_template('all_tutors.html', page_title='ALL_TUTORS', tutor_name=tutor_name)


@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='CONTACTS')


if __name__ == "__main__":
    app.run(debug=True)